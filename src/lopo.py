"""
src/lopo.py
Leave-One-Proxy-Out (LOPO) calibration analysis (Phase 8B).

Uses ONLY PROXY_CAL packets of the 15 proxy devices.
Never uses PROXY_TEST, FINAL_TEST, or enrolled_known_test for fitting.

Outputs:
  results/tables/lopo_bias.csv
  results/tables/threshold_tradeoff.csv
"""
from __future__ import annotations

from pathlib import Path
from typing import Dict, List, Optional, Tuple

import numpy as np
import pandas as pd
from tqdm import tqdm

from src.config import CFG
from src.episodes import _get_feature_cols, _subset_df
from src.evaluate import compute_far, compute_frr
from src.features import load_all_features
from src.model import build_xy, predict_scores, train_model
from src.splits import EpisodeSplit, assert_no_leakage, create_episode_split
from src.threshold import FrozenThreshold, calibrate_threshold
from src.utils import ensure_dir, get_logger, save_json

LOG = get_logger(__name__)


# ---------------------------------------------------------------------------
# LOPO for one episode
# ---------------------------------------------------------------------------

def run_lopo_episode(
    df_all: pd.DataFrame,
    episode_idx: int,
    seed: Optional[int] = None,
    alpha: Optional[float] = None,
    percentile: Optional[int] = None,
) -> dict:
    """
    Run LOPO analysis for one episode.

    Returns dict with per-fold estimates and aggregated bias metrics.
    """
    if seed is None:
        seed = CFG.episode_seed(episode_idx)
    if alpha is None:
        alpha = CFG.lopo_alpha
    if percentile is None:
        percentile = CFG.lopo_percentile

    all_device_ids = sorted(df_all["device_id"].unique().tolist())
    packet_counts = {dev: int((df_all["device_id"] == dev).sum())
                     for dev in all_device_ids}
    split = create_episode_split(all_device_ids, packet_counts, episode_idx, seed)
    assert_no_leakage(split)

    feat_cols = _get_feature_cols(df_all)

    # Train model (enrolled_train only)
    df_train = _subset_df(df_all, split.enrolled_ids, split.enrolled_train_idx)
    X_train, y_train = build_xy(df_train, feat_cols)
    pipe = train_model(X_train, y_train, seed)

    # Known val scores
    df_calval = _subset_df(df_all, split.enrolled_ids, split.enrolled_cal_val_idx)
    X_calval, _ = build_xy(df_calval, feat_cols)
    scores_known_val = predict_scores(pipe, X_calval)

    # Gather PROXY_CAL scores per device
    proxy_cal_scores: Dict[int, np.ndarray] = {}
    for dev_id in split.proxy_ids:
        df_pc = _subset_df(df_all, [dev_id], {dev_id: split.proxy_cal_idx[dev_id]})
        if len(df_pc) == 0:
            proxy_cal_scores[dev_id] = np.array([])
            continue
        Xd, _ = build_xy(df_pc, feat_cols)
        proxy_cal_scores[dev_id] = predict_scores(pipe, Xd)

    # FINAL_TEST scores (reference truth — never used for fitting)
    df_ftest = _subset_df(df_all, split.final_unknown_ids, split.final_test_idx)
    X_ftest, _ = build_xy(df_ftest, feat_cols)
    scores_final_all = predict_scores(pipe, X_ftest)

    # KNOWN_TEST scores (for FRR evaluation — never used for fitting)
    df_ktest = _subset_df(df_all, split.enrolled_ids, split.enrolled_known_test_idx)
    X_ktest, _ = build_xy(df_ktest, feat_cols)
    scores_known_test = predict_scores(pipe, X_ktest)

    # Gather PROXY_TEST scores per proxy device (for matched-device analysis)
    proxy_test_scores: Dict[int, np.ndarray] = {}
    for dev_id in split.proxy_ids:
        df_pt = _subset_df(df_all, [dev_id], {dev_id: split.proxy_test_idx[dev_id]})
        if len(df_pt) > 0:
            X_pt, _ = build_xy(df_pt, feat_cols)
            proxy_test_scores[dev_id] = predict_scores(pipe, X_pt)
        else:
            proxy_test_scores[dev_id] = np.array([])

    # --- Full-data tau (for resubstitution and naive packet-disjoint) ---
    all_proxy_cal_scores = np.concatenate(list(proxy_cal_scores.values()))
    if len(all_proxy_cal_scores) == 0:
        raise ValueError("No proxy_cal scores available for LOPO.")
    ft_full = calibrate_threshold(scores_known_val, all_proxy_cal_scores, method="youden")
    tau_full = ft_full.tau

    # Resubstitution: FAR on PROXY_CAL at tau_full
    far_resub = compute_far(all_proxy_cal_scores, tau_full)

    # Naive packet-disjoint (Condition A): PROXY_TEST at tau_full
    all_proxy_test_scores = np.concatenate(list(proxy_test_scores.values()))
    far_naive = compute_far(all_proxy_test_scores, tau_full)

    # True stranger FAR at tau_full (FINAL_TEST reference)
    far_true_full = compute_far(scores_final_all, tau_full)

    # --- LOPO folds and Matched Device Evaluation ---
    lopo_folds = []
    matched_device_rows = []
    held_out_devices = split.proxy_ids  # 15 devices

    for j, held_id in enumerate(held_out_devices):
        # Assertion: held_id is a proxy device (never final_unknown)
        assert held_id not in split.final_unknown_ids, \
            f"LOPO fold {j}: held-out device {held_id} is a FINAL_UNKNOWN device!"

        # Calibrate on the OTHER 14 proxy devices' PROXY_CAL
        other_ids = [pid for pid in held_out_devices if pid != held_id]

        other_scores = np.concatenate(
            [proxy_cal_scores[pid] for pid in other_ids if len(proxy_cal_scores[pid]) > 0]
        )
        if len(other_scores) == 0:
            LOG.warning("LOPO fold %d: no other proxy_cal scores; skipping.", j)
            continue

        ft_j = calibrate_threshold(scores_known_val, other_scores, method="youden")
        tau_j = ft_j.tau

        # est_j: fraction of held-out PROXY_CAL accepted at tau_j (unfamiliar to tau_j)
        hd_scores = proxy_cal_scores[held_id]
        est_j = compute_far(hd_scores, tau_j) if len(hd_scores) > 0 else float("nan")

        # truth_j: FAR on FINAL_TEST at tau_j (evaluation only, not fitting)
        truth_j = compute_far(scores_final_all, tau_j)

        # Device-matched evaluation on held-out device's PROXY_TEST packets:
        # Same physical device and same test packets evaluated at:
        # 1) tau_full: familiar (device participated in calibration of tau_full)
        # 2) tau_j: unfamiliar (device was strictly excluded from calibration of tau_j)
        pt_scores = proxy_test_scores.get(held_id, np.array([]))
        if len(pt_scores) > 0:
            far_familiar_pt = compute_far(pt_scores, tau_full)
            far_unfamiliar_pt = compute_far(pt_scores, tau_j)
            matched_device_rows.append({
                "episode": episode_idx,
                "device_id": held_id,
                "tau_familiar": float(tau_full),
                "tau_unfamiliar": float(tau_j),
                "far_familiar": float(far_familiar_pt),
                "far_unfamiliar": float(far_unfamiliar_pt),
                "delta_far_matched": float(far_unfamiliar_pt - far_familiar_pt),
            })

        lopo_folds.append({
            "fold": j,
            "held_device": held_id,
            "tau_j": float(tau_j),
            "est_j": float(est_j),
            "truth_j": float(truth_j),
            "bias_j": float(est_j - truth_j) if not np.isnan(est_j) else float("nan"),
            "abs_error_j": float(abs(est_j - truth_j)) if not np.isnan(est_j) else float("nan"),
        })

    if not lopo_folds:
        LOG.warning("Episode %d: no LOPO folds produced.", episode_idx)
        return {}

    df_folds = pd.DataFrame(lopo_folds)
    lopo_est  = float(df_folds["est_j"].dropna().mean())
    lopo_truth = float(df_folds["truth_j"].dropna().mean())
    lopo_bias  = float(lopo_est - lopo_truth)
    lopo_abs   = float(abs(lopo_est - lopo_truth))
    lopo_var   = float(df_folds["bias_j"].dropna().var())

    # --- Robust threshold: smallest tau such that worst/90th-pctile held-out FAR <= alpha ---
    tau_robust = _compute_tau_robust(
        scores_known_val, proxy_cal_scores, held_out_devices, alpha, percentile
    )

    # Evaluate FAR_B and FRR at tau_robust and tau_full
    far_true_robust = compute_far(scores_final_all, tau_robust) if tau_robust is not None else float("nan")
    frr_youden = compute_frr(scores_known_test, tau_full)
    frr_robust = compute_frr(scores_known_test, tau_robust) if tau_robust is not None else float("nan")

    result = {
        "episode_idx": episode_idx,
        "tau_full": float(tau_full),
        "tau_robust": float(tau_robust) if tau_robust is not None else None,
        "far_resub": float(far_resub),
        "far_naive": float(far_naive),
        "far_true_full": float(far_true_full),
        "far_true_robust": float(far_true_robust),
        "frr_youden": float(frr_youden),
        "frr_robust": float(frr_robust),
        "lopo_est": float(lopo_est),
        "lopo_truth": float(lopo_truth),
        "lopo_bias": float(lopo_bias),
        "lopo_abs_error": float(lopo_abs),
        "lopo_variance": float(lopo_var),
        "folds": lopo_folds,
        "matched_device_rows": matched_device_rows,
    }
    return result


def _compute_tau_robust(
    scores_known_val: np.ndarray,
    proxy_cal_scores: Dict[int, np.ndarray],
    proxy_ids: List[int],
    alpha: float,
    percentile: int,
) -> Optional[float]:
    """
    Find smallest tau such that the percentile-th worst held-out device FAR <= alpha.

    Uses a grid search over candidate thresholds.
    """
    all_sc = np.concatenate(list(proxy_cal_scores.values()))
    if len(all_sc) == 0:
        return None
    combined = np.concatenate([scores_known_val, all_sc])
    candidates = np.linspace(combined.min(), combined.max(), 2000)

    for tau in candidates:
        held_fars = []
        for dev_id in proxy_ids:
            sc = proxy_cal_scores.get(dev_id, np.array([]))
            if len(sc) == 0:
                continue
            held_fars.append(compute_far(sc, tau))
        if not held_fars:
            continue
        worst = float(np.percentile(held_fars, percentile))
        if worst <= alpha:
            return float(tau)
    return float(candidates[-1])  # fallback: strictest threshold


# ---------------------------------------------------------------------------
# Multi-episode LOPO
# ---------------------------------------------------------------------------

def run_lopo_all(
    n_episodes: Optional[int] = None,
    smoke: bool = False,
) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Run LOPO analysis across all episodes.

    Returns (lopo_bias_df, threshold_tradeoff_df).
    """
    if n_episodes is None:
        n_episodes = CFG.n_episodes
    if smoke:
        n_episodes = 2

    LOG.info("Loading features …")
    df_all = load_all_features()

    bias_rows = []
    tradeoff_rows = []
    all_matched_device_rows = []

    for ep_idx in tqdm(range(n_episodes), desc="LOPO episodes"):
        try:
            res = run_lopo_episode(df_all, ep_idx)
            if not res:
                continue

            bias_rows.append({
                "episode": ep_idx,
                "estimator": "resubstitution",
                "estimate": res["far_resub"],
                "truth": res["far_true_full"],
                "bias": res["far_resub"] - res["far_true_full"],
                "abs_error": abs(res["far_resub"] - res["far_true_full"]),
            })
            bias_rows.append({
                "episode": ep_idx,
                "estimator": "naive_packet_disjoint",
                "estimate": res["far_naive"],
                "truth": res["far_true_full"],
                "bias": res["far_naive"] - res["far_true_full"],
                "abs_error": abs(res["far_naive"] - res["far_true_full"]),
            })
            bias_rows.append({
                "episode": ep_idx,
                "estimator": "lopo",
                "estimate": res["lopo_est"],
                "truth": res["lopo_truth"],
                "bias": res["lopo_bias"],
                "abs_error": res["lopo_abs_error"],
            })

            tradeoff_rows.append({
                "episode": ep_idx,
                "tau_youden": res["tau_full"],
                "tau_robust": res["tau_robust"],
                "FAR_true_youden": res["far_true_full"],
                "FAR_true_robust": res["far_true_robust"],
                "FRR_youden": res["frr_youden"],
                "FRR_robust": res["frr_robust"],
            })
            if "matched_device_rows" in res:
                all_matched_device_rows.extend(res["matched_device_rows"])
        except Exception as exc:
            LOG.error("LOPO episode %d FAILED: %s", ep_idx, exc, exc_info=True)

    df_bias = pd.DataFrame(bias_rows)
    df_tradeoff = pd.DataFrame(tradeoff_rows)
    df_matched = pd.DataFrame(all_matched_device_rows)

    ensure_dir(CFG.path_tables)
    df_bias.to_csv(CFG.path_tables / "lopo_bias.csv", index=False)
    df_tradeoff.to_csv(CFG.path_tables / "threshold_tradeoff.csv", index=False)
    if not df_matched.empty:
        df_matched.to_csv(CFG.path_tables / "matched_device_evaluation.csv", index=False)
    LOG.info("LOPO and Matched-Device results saved.")

    return df_bias, df_tradeoff


if __name__ == "__main__":
    LOG.info("lopo.py self-test …")
    try:
        df_bias, df_tradeoff = run_lopo_all(n_episodes=1)
        print(df_bias)
    except FileNotFoundError as e:
        LOG.warning("No features found (expected during dev): %s", e)
    LOG.info("lopo.py self-test complete.")
