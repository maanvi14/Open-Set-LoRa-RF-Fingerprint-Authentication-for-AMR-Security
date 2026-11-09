"""
src/sweep.py
Proxy-count sweep (Phase 7).

For k ∈ [0, 1, 3, 5, 10, 15]:
  - k=0: use "tau at 95% known acceptance" (no proxy data)
  - k>0: randomly select k proxy devices' PROXY_CAL packets for calibration

Assertions:
  - FINAL_TEST devices never enter calibration at any k
  - FAR_B evaluated on same 15 FINAL_TEST devices every time

Outputs:
  results/sweep/sweep_results.csv
  results/sweep/sweep_plot.png
"""
from __future__ import annotations

import json
import time
from pathlib import Path
from typing import Dict, List, Optional

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from tqdm import tqdm

from src.config import CFG
from src.episodes import _get_feature_cols, _subset_df, run_one_episode
from src.evaluate import compute_delta_far, compute_far, compute_frr
from src.features import load_all_features
from src.model import build_xy, predict_scores, train_model
from src.splits import EpisodeSplit, assert_no_leakage, create_episode_split
from src.threshold import FrozenThreshold, calibrate_threshold
from src.utils import ensure_dir, get_logger, save_json

LOG = get_logger(__name__)

SWEEP_COLS = ["episode", "k", "tau", "FAR_A", "FAR_B", "FRR", "DeltaFAR"]


def run_sweep_episode(
    df_all: pd.DataFrame,
    episode_idx: int,
    ks: Optional[List[int]] = None,
    seed: Optional[int] = None,
) -> List[dict]:
    """
    For one episode, run the proxy-count sweep over all k values.

    Returns list of result dicts (one per k).
    """
    if ks is None:
        ks = CFG.sweep_ks
    if seed is None:
        seed = CFG.episode_seed(episode_idx)

    all_device_ids = sorted(df_all["device_id"].unique().tolist())
    packet_counts = {dev: int((df_all["device_id"] == dev).sum())
                     for dev in all_device_ids}
    split = create_episode_split(all_device_ids, packet_counts, episode_idx, seed)
    assert_no_leakage(split)

    feat_cols = _get_feature_cols(df_all)

    # Train once per episode on enrolled_train
    df_train = _subset_df(df_all, split.enrolled_ids, split.enrolled_train_idx)
    X_train, y_train = build_xy(df_train, feat_cols)
    pipe = train_model(X_train, y_train, seed)

    # Known val scores (for calibration positive class)
    df_cal = _subset_df(df_all, split.enrolled_ids, split.enrolled_cal_val_idx)
    X_cal, _ = build_xy(df_cal, feat_cols)
    scores_known_val = predict_scores(pipe, X_cal)

    # Known test scores (for FRR — identical across k)
    df_ktest = _subset_df(df_all, split.enrolled_ids, split.enrolled_known_test_idx)
    X_ktest, _ = build_xy(df_ktest, feat_cols)
    scores_known_test = predict_scores(pipe, X_ktest)

    # FINAL_TEST scores (must be constant across all k — never used in calibration)
    df_ftest = _subset_df(df_all, split.final_unknown_ids, split.final_test_idx)
    X_ftest, _ = build_xy(df_ftest, feat_cols)
    # Safety assertion: none of the final_unknown_ids appear in calibration
    for fid in split.final_unknown_ids:
        assert fid not in split.proxy_cal_idx, \
            f"ASSERTION FAILED: final_unknown device {fid} in proxy_cal!"
        assert fid not in split.proxy_test_idx, \
            f"ASSERTION FAILED: final_unknown device {fid} in proxy_test!"

    scores_final_test = predict_scores(pipe, X_ftest)

    # RNG for k-selection: generate a SINGLE permutation of proxy devices so that
    # subsets for k in [1, 3, 5, 10, 15] are nested prefixes of the same permutation
    k_rng = np.random.default_rng(seed ^ 0xDEAD)
    proxy_perm = list(split.proxy_ids)
    k_rng.shuffle(proxy_perm)

    # Reference nominal FRR target (e.g. 25% or calibrated from full proxy set)
    # to evaluate matched-FRR stranger penetration
    target_frr = 0.2588 # baseline Youden FRR operating point

    results = []
    for k in ks:
        if k == 0:
            # tau at 95% known acceptance, no proxy data
            ft = calibrate_threshold(
                scores_known_val,
                np.array([], dtype=np.float64),
                method="known_acceptance",
                target_acceptance=CFG.alternative_tau_known_acceptance,
            )
            far_a = float("nan")  # no proxy_test for k=0 estimate
            delta = float("nan")  # DeltaFAR is undefined when Condition A does not exist
        else:
            # Nested prefix: take the first k devices from the fixed permutation
            k_actual = min(k, len(proxy_perm))
            chosen_proxy = sorted(proxy_perm[:k_actual])

            # Assertion: chosen proxy devices are strictly proxy devices, never final-unknown
            for cpid in chosen_proxy:
                assert cpid not in split.final_unknown_ids, \
                    f"Sweep k={k}: chosen proxy {cpid} is a FINAL_UNKNOWN device!"

            df_pcal_k = _subset_df(df_all, chosen_proxy, split.proxy_cal_idx)
            X_pcal_k, _ = build_xy(df_pcal_k, feat_cols)
            scores_pcal_k = predict_scores(pipe, X_pcal_k)

            ft = calibrate_threshold(scores_known_val, scores_pcal_k, method="youden")

            # FAR_A: PROXY_TEST of the chosen k devices
            df_ptest_k = _subset_df(df_all, chosen_proxy, split.proxy_test_idx)
            if len(df_ptest_k) > 0:
                X_ptest_k, _ = build_xy(df_ptest_k, feat_cols)
                far_a = compute_far(predict_scores(pipe, X_ptest_k), ft.tau)
            else:
                far_a = float("nan")

            delta = compute_delta_far(far_a, compute_far(scores_final_test, ft.tau)) if not np.isnan(far_a) else float("nan")

        tau = ft.tau
        far_b = compute_far(scores_final_test, tau)
        frr   = compute_frr(scores_known_test, tau)

        # Also compute FAR_B at matched nominal FRR
        # (quantile of known_val corresponding to 1 - target_frr acceptance)
        tau_matched = float(np.quantile(scores_known_val, target_frr))
        far_b_matched_frr = compute_far(scores_final_test, tau_matched)
        frr_matched = compute_frr(scores_known_test, tau_matched)

        results.append({
            "episode": episode_idx,
            "k": k,
            "tau": float(tau),
            "FAR_A": float(far_a),
            "FAR_B": float(far_b),
            "FRR": float(frr),
            "DeltaFAR": float(delta),
            "tau_matched_frr": float(tau_matched),
            "FAR_B_matched_frr": float(far_b_matched_frr),
            "FRR_matched": float(frr_matched),
        })

    return results


def run_sweep(
    n_episodes: Optional[int] = None,
    ks: Optional[List[int]] = None,
    smoke: bool = False,
) -> pd.DataFrame:
    """
    Run the proxy-count sweep over all episodes and k values.

    Returns DataFrame with columns: episode, k, tau, FAR_A, FAR_B, FRR, DeltaFAR.
    """
    if n_episodes is None:
        n_episodes = CFG.n_episodes
    if ks is None:
        ks = CFG.sweep_ks
    if smoke:
        n_episodes = 2
        ks = [k for k in ks if k <= 3]
        LOG.info("SMOKE MODE: %d episodes, ks=%s", n_episodes, ks)

    LOG.info("Loading features …")
    df_all = load_all_features()
    LOG.info("Loaded %d rows, %d devices.", len(df_all), df_all["device_id"].nunique())

    all_rows = []
    for ep_idx in tqdm(range(n_episodes), desc="Sweep episodes"):
        try:
            ep_rows = run_sweep_episode(df_all, ep_idx, ks=ks)
            all_rows.extend(ep_rows)
        except Exception as exc:
            LOG.error("Episode %03d sweep FAILED: %s", ep_idx, exc, exc_info=True)

    df = pd.DataFrame(all_rows, columns=SWEEP_COLS)
    out_dir = CFG.path_results / "sweep"
    ensure_dir(out_dir)
    csv_path = out_dir / "sweep_results.csv"
    df.to_csv(csv_path, index=False)
    LOG.info("Sweep results saved → %s", csv_path)

    _make_sweep_plot(df, out_dir / "sweep_plot.png")
    return df


def _make_sweep_plot(df: pd.DataFrame, out_path: Path) -> None:
    """Plot FAR_A, FAR_B, DeltaFAR vs k with device-level CIs."""
    ks = sorted(df["k"].unique())
    # Drop k=0 FAR_A since it's NaN
    metrics = ["FAR_A", "FAR_B", "DeltaFAR"]
    colors = ["#0072B2", "#D55E00", "#009E73"]  # colorblind-friendly

    fig, ax = plt.subplots(figsize=(6, 4))
    for metric, color in zip(metrics, colors):
        means, lows, highs = [], [], []
        valid_ks = []
        for k in ks:
            vals = df[(df["k"] == k)][metric].dropna().values
            if len(vals) == 0:
                continue
            # 95% bootstrap CI over episodes
            rng = np.random.default_rng(42)
            boot = np.array([
                np.mean(rng.choice(vals, size=len(vals), replace=True))
                for _ in range(1000)
            ])
            means.append(float(np.mean(vals)))
            lows.append(float(np.percentile(boot, 2.5)))
            highs.append(float(np.percentile(boot, 97.5)))
            valid_ks.append(k)

        if not valid_ks:
            continue
        means_arr = np.array(means)
        lows_arr  = np.array(lows)
        highs_arr = np.array(highs)
        ax.plot(valid_ks, means_arr, marker="o", label=metric, color=color)
        ax.fill_between(valid_ks, lows_arr, highs_arr, alpha=0.2, color=color)

    ax.set_xlabel("Number of proxy devices k")
    ax.set_ylabel("Rate")
    ax.set_title("Proxy-count sweep: FAR and ΔFA R vs k")
    ax.legend()
    ax.grid(True, linestyle="--", alpha=0.5)
    plt.tight_layout()
    plt.savefig(out_path, dpi=150)
    plt.close(fig)
    LOG.info("Sweep plot saved → %s", out_path)


if __name__ == "__main__":
    LOG.info("sweep.py self-test …")
    try:
        df = run_sweep(n_episodes=1, ks=[0, 1, 3])
        print(df)
    except FileNotFoundError as e:
        LOG.warning("No features found (expected during dev): %s", e)
    LOG.info("sweep.py self-test complete.")
