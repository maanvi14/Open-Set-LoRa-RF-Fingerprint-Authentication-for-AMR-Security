"""
src/stats.py
Statistics and explanation (Phase 8).

- Device-level bootstrap (resample devices, not packets) for 95% CIs of FAR_A, FAR_B, DeltaFAR
- Wilcoxon signed-rank test across episodes
- Fraction of episodes with DeltaFAR > 0
- Per-device FAR ranking
- Saves results/tables/stats_summary.csv
"""
from __future__ import annotations

from pathlib import Path
from typing import Dict, List, Optional, Tuple

import numpy as np
import pandas as pd
from scipy.stats import wilcoxon

from src.config import CFG
from src.utils import ensure_dir, get_logger

LOG = get_logger(__name__)


# ---------------------------------------------------------------------------
# Bootstrap CI
# ---------------------------------------------------------------------------

def bootstrap_ci(
    values: np.ndarray,
    n_boot: int = 2000,
    ci: float = 0.95,
    seed: int = 42,
) -> Tuple[float, float, float]:
    """
    Bootstrap 95% CI for the mean of `values`.

    Returns (mean, lower, upper).
    """
    rng = np.random.default_rng(seed)
    boot_means = np.array([
        np.mean(rng.choice(values, size=len(values), replace=True))
        for _ in range(n_boot)
    ])
    alpha = 1.0 - ci
    lower = float(np.percentile(boot_means, 100 * alpha / 2))
    upper = float(np.percentile(boot_means, 100 * (1 - alpha / 2)))
    return float(np.mean(values)), lower, upper


def device_bootstrap_ci(
    device_values: np.ndarray,
    n_boot: int = 2000,
    ci: float = 0.95,
    seed: int = 42,
) -> Tuple[float, float, float]:
    """
    Device-level bootstrap: resamples across the N physical devices (not episodes or packets).
    Returns (mean, lower_ci, upper_ci).
    """
    clean_vals = device_values[~np.isnan(device_values)]
    if len(clean_vals) == 0:
        return float("nan"), float("nan"), float("nan")
    rng = np.random.default_rng(seed)
    n = len(clean_vals)
    boot_means = np.array([
        np.mean(rng.choice(clean_vals, size=n, replace=True))
        for _ in range(n_boot)
    ])
    alpha = 1.0 - ci
    lower = float(np.percentile(boot_means, 100 * alpha / 2))
    upper = float(np.percentile(boot_means, 100 * (1 - alpha / 2)))
    return float(np.mean(clean_vals)), lower, upper


# ---------------------------------------------------------------------------
# Main statistics computation
# ---------------------------------------------------------------------------

def compute_stats(
    episode_summary_path: Optional[Path] = None,
) -> pd.DataFrame:
    """
    Load episode_summary.csv and compute statistics.
    Computes both episode-level metrics and true device-level bootstrap CIs.
    """
    if episode_summary_path is None:
        episode_summary_path = CFG.path_tables / "episode_summary.csv"

    if not episode_summary_path.exists():
        raise FileNotFoundError(
            f"Episode summary not found: {episode_summary_path}. "
            "Run scripts/03_run_episodes.py first."
        )

    df = pd.read_csv(episode_summary_path)
    LOG.info("Loaded episode summary: %d rows.", len(df))

    # Collect per-device means across episodes to do genuine device-level bootstrapping
    import json
    ep_dir = CFG.path_results / "episodes"
    dev_fars_a: Dict[str, List[float]] = {}
    dev_fars_b: Dict[str, List[float]] = {}

    for ep_idx in range(len(df)):
        p = ep_dir / f"episode_{ep_idx:03d}.json"
        if p.exists():
            with open(p) as fh:
                res = json.load(fh)
            for d, f in res.get("per_device_FAR_A", {}).items():
                dev_fars_a.setdefault(d, []).append(f)
            for d, f in res.get("per_device_FAR_B", {}).items():
                dev_fars_b.setdefault(d, []).append(f)

    # Physical device averages
    dev_means_a = np.array([np.nanmean(f) for f in dev_fars_a.values()]) if dev_fars_a else np.array([])
    dev_means_b = np.array([np.nanmean(f) for f in dev_fars_b.values()]) if dev_fars_b else np.array([])

    summary_rows = []

    for metric in ["FAR_A", "FAR_B", "DeltaFAR", "FRR", "AUROC_A", "AUROC_B", "macro_F1"]:
        if metric not in df.columns:
            continue
        vals = df[metric].dropna().values
        if len(vals) == 0:
            continue

        # If metric is FAR_A or FAR_B, compute true device-level bootstrap CI across physical devices
        if metric == "FAR_A" and len(dev_means_a) > 0:
            mean, lo, hi = device_bootstrap_ci(dev_means_a)
            n_items = len(dev_means_a)
            ci_type = "device_level"
        elif metric == "FAR_B" and len(dev_means_b) > 0:
            mean, lo, hi = device_bootstrap_ci(dev_means_b)
            n_items = len(dev_means_b)
            ci_type = "device_level"
        else:
            mean, lo, hi = bootstrap_ci(vals)
            n_items = len(vals)
            ci_type = "episode_level"

        row = {
            "metric": metric,
            "ci_type": ci_type,
            "n_samples": n_items,
            "mean": mean,
            "ci_lower_95": lo,
            "ci_upper_95": hi,
            "std": float(np.std(vals)),
            "min": float(np.min(vals)),
            "max": float(np.max(vals)),
            "p_value": float("nan"),
        }
        summary_rows.append(row)

    # DeltaFAR > 0 fraction
    if "DeltaFAR" in df.columns:
        delta = df["DeltaFAR"].dropna().values
        frac_positive = float(np.mean(delta > 0))
        summary_rows.append({
            "metric": "frac_DeltaFAR_gt_0",
            "ci_type": "episode_level",
            "n_samples": len(delta),
            "mean": frac_positive,
            "ci_lower_95": float("nan"),
            "ci_upper_95": float("nan"),
            "std": float("nan"),
            "min": float("nan"),
            "max": float("nan"),
            "p_value": float("nan"),
        })

    # Device-matched paired analysis (if matched_device_evaluation.csv exists)
    matched_csv = CFG.path_tables / "matched_device_evaluation.csv"
    if matched_csv.exists():
        df_matched = pd.read_csv(matched_csv)
        # Aggregate by physical device_id first to eliminate pseudoreplication
        dev_agg = df_matched.groupby("device_id")[["far_familiar", "far_unfamiliar", "delta_far_matched"]].mean()
        diffs = dev_agg["delta_far_matched"].dropna().values
        if len(diffs) >= 5 and np.any(diffs != 0):
            w_stat, w_pval = wilcoxon(diffs)
        else:
            w_stat, w_pval = float("nan"), float("nan")

        m_mean, m_lo, m_hi = device_bootstrap_ci(diffs)
        summary_rows.append({
            "metric": "device_matched_DeltaFAR",
            "ci_type": "device_level",
            "n_samples": len(diffs),
            "mean": m_mean,
            "ci_lower_95": m_lo,
            "ci_upper_95": m_hi,
            "std": float(np.std(diffs)),
            "min": float(np.min(diffs)),
            "max": float(np.max(diffs)),
            "p_value": float(w_pval),
        })

    # Episode-level Wilcoxon signed-rank test
    if "FAR_A" in df.columns and "FAR_B" in df.columns:
        fa = df["FAR_A"].dropna()
        fb = df["FAR_B"].dropna()
        common = fa.index.intersection(fb.index)
        if len(common) >= 5:
            diff = fb.loc[common].values - fa.loc[common].values
            stat, pval = wilcoxon(diff) if np.any(diff != 0) else (0.0, 1.0)
        else:
            stat, pval = float("nan"), float("nan")

        summary_rows.append({
            "metric": "wilcoxon_FAR_B_minus_FAR_A_episodes",
            "ci_type": "episode_level",
            "n_samples": int(len(common)),
            "mean": float(stat),
            "ci_lower_95": float("nan"),
            "ci_upper_95": float("nan"),
            "std": float("nan"),
            "min": float("nan"),
            "max": float("nan"),
            "p_value": float(pval),
        })

    df_stats = pd.DataFrame(summary_rows)
    ensure_dir(CFG.path_tables)
    out_path = CFG.path_tables / "stats_summary.csv"
    df_stats.to_csv(out_path, index=False)
    LOG.info("Stats summary saved → %s", out_path)
    return df_stats


# ---------------------------------------------------------------------------
# Per-device FAR ranking from episode JSON files
# ---------------------------------------------------------------------------

def per_device_far_ranking(
    condition: str = "FAR_B",
    n_episodes: Optional[int] = None,
) -> pd.DataFrame:
    """
    Load per-device FAR from episode JSON files and rank devices.

    Returns DataFrame with columns: device_id, mean_FAR, std_FAR, rank.
    """
    import json
    if n_episodes is None:
        n_episodes = CFG.n_episodes

    ep_dir = CFG.path_results / "episodes"
    key = "per_device_FAR_B" if condition == "FAR_B" else "per_device_FAR_A"

    device_fars: Dict[str, List[float]] = {}
    for ep_idx in range(n_episodes):
        p = ep_dir / f"episode_{ep_idx:03d}.json"
        if not p.exists():
            continue
        with open(p) as fh:
            res = json.load(fh)
        pdev = res.get(key, {})
        for dev_id, far in pdev.items():
            device_fars.setdefault(dev_id, []).append(far)

    if not device_fars:
        return pd.DataFrame(columns=["device_id", "mean_FAR", "std_FAR", "rank"])

    rows = []
    for dev_id, fars in device_fars.items():
        rows.append({
            "device_id": int(dev_id),
            "mean_FAR": float(np.nanmean(fars)),
            "std_FAR": float(np.nanstd(fars)) if len(fars) > 1 else 0.0,
            "n_episodes": len(fars),
            "reliable_estimate": len(fars) >= 4,
        })
    df = pd.DataFrame(rows).sort_values("mean_FAR", ascending=False).reset_index(drop=True)
    df["rank"] = df.index + 1
    out_path = CFG.path_tables / f"per_device_far_ranking_{condition}.csv"
    ensure_dir(CFG.path_tables)
    df.to_csv(out_path, index=False)
    LOG.info("Per-device FAR ranking saved → %s", out_path)
    return df


if __name__ == "__main__":
    LOG.info("stats.py self-test …")
    rng = np.random.default_rng(0)
    vals = rng.uniform(0, 1, 20)
    mean, lo, hi = bootstrap_ci(vals)
    LOG.info("Bootstrap CI: mean=%.4f  [%.4f, %.4f]", mean, lo, hi)
    try:
        df_stats = compute_stats()
        print(df_stats)
    except FileNotFoundError as e:
        LOG.warning("No episode summary found (expected during dev): %s", e)
    LOG.info("stats.py self-test complete.")
