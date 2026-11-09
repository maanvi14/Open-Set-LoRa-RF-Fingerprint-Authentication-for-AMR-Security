"""
src/episodes.py
Multi-episode orchestration (Phase 4–6).

For each of N=20 episodes:
  1. Load pre-computed features from data/features/
  2. Create EpisodeSplit
  3. Train model on enrolled_train
  4. Calibrate frozen threshold using known_val + PROXY_CAL
  5. Condition A: FAR on PROXY_TEST at frozen tau
  6. Condition B: FAR on FINAL_TEST at frozen tau
  7. FRR on known_test (assert identical in A and B)
  8. AUROC for both conditions
  9. Per-device FAR for proxy and final-unknown
  10. DeltaFAR

Results saved to results/episodes/episode_NNN.json and
results/tables/episode_summary.csv.

Usage:
    python scripts/03_run_episodes.py [--smoke]
"""
from __future__ import annotations

import json
import time
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import numpy as np
import pandas as pd
from tqdm import tqdm

from src.config import CFG
from src.evaluate import (
    assert_frr_identical,
    compute_auroc,
    compute_delta_far,
    compute_far,
    compute_frr,
    per_device_far,
)
from src.features import load_all_features
from src.model import build_xy, evaluate_closed_set, predict_scores, save_model, train_model
from src.splits import EpisodeSplit, assert_no_leakage, create_episode_split
from src.threshold import FrozenThreshold, calibrate_threshold
from src.utils import ensure_dir, get_logger, save_json

LOG = get_logger(__name__)


# ---------------------------------------------------------------------------
# Data helpers
# ---------------------------------------------------------------------------

def _get_feature_cols(df: pd.DataFrame) -> List[str]:
    """Return feature column names (all columns except metadata)."""
    meta_cols = {"device_id", "packet_idx", "source_file"}
    return [c for c in df.columns if c not in meta_cols]


def _subset_df(
    df: pd.DataFrame,
    device_ids: List[int],
    idx_dict: Dict[int, np.ndarray],
) -> pd.DataFrame:
    """
    Extract rows for the given device_ids and packet indices.

    idx_dict[dev] contains the packet_idx values (original position in device array).
    """
    parts = []
    for dev_id in device_ids:
        if dev_id not in idx_dict:
            continue
        pkt_indices = idx_dict[dev_id]
        dev_df = df[df["device_id"] == dev_id].copy()
        dev_df = dev_df.sort_values("packet_idx").reset_index(drop=True)
        # pkt_indices are positional within this device's sorted array
        if len(pkt_indices) == 0:
            continue
        pkt_indices_clipped = pkt_indices[pkt_indices < len(dev_df)]
        sub = dev_df.iloc[pkt_indices_clipped]
        parts.append(sub)
    if not parts:
        return pd.DataFrame(columns=df.columns)
    return pd.concat(parts, ignore_index=True)


# ---------------------------------------------------------------------------
# Episode runner
# ---------------------------------------------------------------------------

def run_one_episode(
    df_all: pd.DataFrame,
    episode_idx: int,
    seed: Optional[int] = None,
    save_model_flag: bool = False,
) -> dict:
    """
    Run a single episode and return a results dict.

    Parameters
    ----------
    df_all       : combined feature DataFrame for ALL devices
    episode_idx  : 0-based episode index
    seed         : explicit seed (default: CFG.episode_seed(episode_idx))
    save_model_flag : whether to persist the trained model

    Returns
    -------
    dict with episode results
    """
    if seed is None:
        seed = CFG.episode_seed(episode_idx)

    all_device_ids = sorted(df_all["device_id"].unique().tolist())
    packet_counts = {
        dev: int((df_all["device_id"] == dev).sum())
        for dev in all_device_ids
    }

    # --- 1. Create split ---
    split = create_episode_split(all_device_ids, packet_counts, episode_idx, seed)
    assert_no_leakage(split)

    feat_cols = _get_feature_cols(df_all)

    # --- 2. Train model ---
    df_train = _subset_df(df_all, split.enrolled_ids, split.enrolled_train_idx)
    X_train, y_train = build_xy(df_train, feat_cols)
    pipe = train_model(X_train, y_train, seed)

    # --- 3. Cal_val (closed-set) ---
    df_cal = _subset_df(df_all, split.enrolled_ids, split.enrolled_cal_val_idx)
    X_cal, y_cal = build_xy(df_cal, feat_cols)
    closed_metrics = evaluate_closed_set(pipe, X_cal, y_cal)

    # --- 4. Calibrate frozen threshold ---
    # Positive: enrolled cal_val scores (known validation)
    scores_known_val = predict_scores(pipe, X_cal)

    # Negative: proxy_cal scores
    df_pcal = _subset_df(df_all, split.proxy_ids, split.proxy_cal_idx)
    X_pcal, _ = build_xy(df_pcal, feat_cols, label_col="device_id")
    scores_proxy_cal = predict_scores(pipe, X_pcal)

    ft: FrozenThreshold = calibrate_threshold(
        scores_known_val, scores_proxy_cal, method="youden"
    )
    tau = ft.tau
    LOG.info("Episode %03d: tau=%.4f (Youden's J=%.4f)",
             episode_idx, tau, ft.calibration_stats["youden_j"])

    # --- 5. Known test scores (identical for cond A and B) ---
    df_ktest = _subset_df(df_all, split.enrolled_ids, split.enrolled_known_test_idx)
    X_ktest, _ = build_xy(df_ktest, feat_cols, label_col="device_id")
    scores_known_test = predict_scores(pipe, X_ktest)
    frr = compute_frr(scores_known_test, tau)

    # --- 6. Condition A: PROXY_TEST ---
    df_ptest = _subset_df(df_all, split.proxy_ids, split.proxy_test_idx)
    X_ptest, _ = build_xy(df_ptest, feat_cols, label_col="device_id")
    scores_proxy_test = predict_scores(pipe, X_ptest)
    far_a = compute_far(scores_proxy_test, tau)
    auroc_a = compute_auroc(scores_known_test, scores_proxy_test)

    # Per-device FAR (A)
    pdev_far_a: Dict[str, float] = {}
    for dev_id in split.proxy_ids:
        df_dev = _subset_df(df_all, [dev_id], {dev_id: split.proxy_test_idx.get(dev_id, np.array([]))})
        if len(df_dev) == 0:
            continue
        Xd, _ = build_xy(df_dev, feat_cols, label_col="device_id")
        pdev_far_a[str(dev_id)] = compute_far(predict_scores(pipe, Xd), tau)

    # --- 7. Condition B: FINAL_TEST ---
    df_ftest = _subset_df(df_all, split.final_unknown_ids, split.final_test_idx)
    X_ftest, _ = build_xy(df_ftest, feat_cols, label_col="device_id")
    scores_final_test = predict_scores(pipe, X_ftest)
    far_b = compute_far(scores_final_test, tau)
    auroc_b = compute_auroc(scores_known_test, scores_final_test)

    # FRR must be identical (same known_test set, same tau)
    frr_b = compute_frr(scores_known_test, tau)
    assert_frr_identical(frr, frr_b)

    # Per-device FAR (B)
    pdev_far_b: Dict[str, float] = {}
    for dev_id in split.final_unknown_ids:
        df_dev = _subset_df(df_all, [dev_id], {dev_id: split.final_test_idx.get(dev_id, np.array([]))})
        if len(df_dev) == 0:
            continue
        Xd, _ = build_xy(df_dev, feat_cols, label_col="device_id")
        pdev_far_b[str(dev_id)] = compute_far(predict_scores(pipe, Xd), tau)

    delta_far = compute_delta_far(far_a, far_b)

    result = {
        "episode_idx": episode_idx,
        "seed": int(seed),
        "tau": float(tau),
        "FAR_A": float(far_a),
        "FAR_B": float(far_b),
        "FRR": float(frr),
        "DeltaFAR": float(delta_far),
        "AUROC_A": float(auroc_a),
        "AUROC_B": float(auroc_b),
        "macro_F1": float(closed_metrics["macro_f1"]),
        "accuracy": float(closed_metrics["accuracy"]),
        "calibration_stats": ft.calibration_stats,
        "per_device_FAR_A": pdev_far_a,
        "per_device_FAR_B": pdev_far_b,
        "enrolled_ids": split.enrolled_ids,
        "proxy_ids": split.proxy_ids,
        "final_unknown_ids": split.final_unknown_ids,
    }

    if save_model_flag:
        save_model(pipe, episode_idx)

    return result


# ---------------------------------------------------------------------------
# Episode summary
# ---------------------------------------------------------------------------

def save_episode_result(result: dict, out_dir: Optional[Path] = None) -> Path:
    if out_dir is None:
        out_dir = CFG.path_results / "episodes"
    ensure_dir(out_dir)
    p = out_dir / f"episode_{result['episode_idx']:03d}.json"
    save_json(result, p)
    return p


SUMMARY_COLS = [
    "episode", "tau", "FAR_A", "FAR_B", "FRR", "DeltaFAR",
    "AUROC_A", "AUROC_B", "macro_F1",
]


def run_all_episodes(
    n_episodes: Optional[int] = None,
    smoke: bool = False,
    n_smoke_devices_per_group: int = 3,
    n_smoke_episodes: int = 2,
    save_models: bool = False,
) -> pd.DataFrame:
    """
    Run all episodes and return summary DataFrame.

    Parameters
    ----------
    n_episodes : int, optional (default: CFG.n_episodes)
    smoke      : bool — if True, run a reduced smoke test
    """
    if n_episodes is None:
        n_episodes = CFG.n_episodes
    if smoke:
        n_episodes = n_smoke_episodes
        LOG.info("SMOKE MODE: %d episodes, %d devices/group",
                 n_smoke_episodes, n_smoke_devices_per_group)

    # Load all features
    LOG.info("Loading features from %s …", CFG.path_features)
    df_all = load_all_features()
    LOG.info("Loaded %d rows, %d devices.", len(df_all), df_all["device_id"].nunique())

    if smoke:
        # Keep only enough devices for smoke test
        needed = n_smoke_devices_per_group * 3
        all_devs = sorted(df_all["device_id"].unique())
        if len(all_devs) > needed:
            df_all = df_all[df_all["device_id"].isin(all_devs[:needed])].copy()
        # Temporarily patch config sizes
        import src.config as _cfg_mod
        orig_en = CFG.n_enrolled
        orig_px = CFG.n_proxy
        orig_fu = CFG.n_final_unknown
        # Patch via object attribute (the dataclass is not frozen)
        object.__setattr__(CFG, "n_enrolled", n_smoke_devices_per_group)
        object.__setattr__(CFG, "n_proxy", n_smoke_devices_per_group)
        object.__setattr__(CFG, "n_final_unknown", n_smoke_devices_per_group)

    results = []
    for ep_idx in tqdm(range(n_episodes), desc="Episodes"):
        t0 = time.time()
        try:
            res = run_one_episode(df_all, ep_idx, save_model_flag=save_models)
            save_episode_result(res)
            results.append(res)
            LOG.info("Episode %03d done in %.1fs: FAR_A=%.4f FAR_B=%.4f FRR=%.4f delta=%.4f",
                     ep_idx, time.time() - t0,
                     res["FAR_A"], res["FAR_B"], res["FRR"], res["DeltaFAR"])
        except Exception as exc:
            LOG.error("Episode %03d FAILED: %s", ep_idx, exc, exc_info=True)

    if smoke:
        # Restore
        object.__setattr__(CFG, "n_enrolled", orig_en)
        object.__setattr__(CFG, "n_proxy", orig_px)
        object.__setattr__(CFG, "n_final_unknown", orig_fu)

    # Build summary CSV
    summary_rows = []
    for r in results:
        summary_rows.append({
            "episode": r["episode_idx"],
            "tau": r["tau"],
            "FAR_A": r["FAR_A"],
            "FAR_B": r["FAR_B"],
            "FRR": r["FRR"],
            "DeltaFAR": r["DeltaFAR"],
            "AUROC_A": r["AUROC_A"],
            "AUROC_B": r["AUROC_B"],
            "macro_F1": r["macro_F1"],
        })
    df_summary = pd.DataFrame(summary_rows, columns=SUMMARY_COLS)
    ensure_dir(CFG.path_tables)
    csv_path = CFG.path_tables / "episode_summary.csv"
    df_summary.to_csv(csv_path, index=False)
    LOG.info("Episode summary saved → %s", csv_path)
    return df_summary


if __name__ == "__main__":
    LOG.info("episodes.py self-test (requires extracted features) …")
    try:
        df = run_all_episodes(n_episodes=1)
        print(df)
    except FileNotFoundError as e:
        LOG.warning("No features found (expected during dev): %s", e)
    LOG.info("episodes.py self-test complete.")
