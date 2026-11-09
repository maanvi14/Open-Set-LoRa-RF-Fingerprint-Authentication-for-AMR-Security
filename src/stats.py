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
    per_device_far: Dict[str, List[float]],
    n_boot: int = 2000,
    ci: float = 0.95,
    seed: int = 42,
) -> Dict[str, Tuple[float, float, float]]:
    """
    Device-level bootstrap: resample devices (not packets).

    per_device_far: {device_id: [far_ep0, far_ep1, ...]}
    Returns {metric_name: (mean, lower, upper)} for the mean FAR across devices.
    """
    device_means = np.array([np.nanmean(v) for v in per_device_far.values()])
    if len(device_means) == 0:
        return {"mean": (float("nan"), float("nan"), float("nan"))}
    rng = np.random.default_rng(seed)
    boot_means = np.array([
        np.mean(rng.choice(device_means, size=len(device_means), replace=True))
        for _ in range(n_boot)
    ])
    alpha = 1.0 - ci
    lower = float(np.percentile(boot_means, 100 * alpha / 2))
    upper = float(np.percentile(boot_means, 100 * (1 - alpha / 2)))
    return {"mean": (float(np.mean(device_means)), lower, upper)}


# ---------------------------------------------------------------------------
# Main statistics computation
# ---------------------------------------------------------------------------

def compute_stats(
    episode_summary_path: Optional[Path] = None,
) -> pd.DataFrame:
    """
    Load episode_summary.csv and compute statistics.

    Returns a DataFrame saved to results/tables/stats_summary.csv.
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

    summary_rows = []

    for metric in ["FAR_A", "FAR_B", "DeltaFAR", "FRR", "AUROC_A", "AUROC_B", "macro_F1"]:
        if metric not in df.columns:
            continue
        vals = df[metric].dropna().values
        if len(vals) == 0:
            continue
        mean, lo, hi = bootstrap_ci(vals)
        row = {
            "metric": metric,
            "n_episodes": len(vals),
            "mean": mean,
            "ci_lower_95": lo,
            "ci_upper_95": hi,
            "std": float(np.std(vals)),
            "min": float(np.min(vals)),
            "max": float(np.max(vals)),
        }
        summary_rows.append(row)

    # DeltaFAR > 0 fraction
    if "DeltaFAR" in df.columns:
        delta = df["DeltaFAR"].dropna().values
        frac_positive = float(np.mean(delta > 0))
        summary_rows.append({
            "metric": "frac_DeltaFAR_gt_0",
            "n_episodes": len(delta),
            "mean": frac_positive,
            "ci_lower_95": float("nan"),
            "ci_upper_95": float("nan"),
            "std": float("nan"),
            "min": float("nan"),
            "max": float("nan"),
        })

    # Wilcoxon signed-rank test: FAR_A vs FAR_B
    if "FAR_A" in df.columns and "FAR_B" in df.columns:
        fa = df["FAR_A"].dropna()
        fb = df["FAR_B"].dropna()
        # Align on common index
        common = fa.index.intersection(fb.index)
        if len(common) >= 5:
            diff = fb.loc[common].values - fa.loc[common].values
            if np.any(diff != 0):
                stat, pval = wilcoxon(diff)
            else:
                stat, pval = 0.0, 1.0
        else:
            stat, pval = float("nan"), float("nan")
        summary_rows.append({
            "metric": "wilcoxon_FAR_B_minus_FAR_A",
            "n_episodes": int(len(common)),
            "mean": float(stat),
            "ci_lower_95": float("nan"),
            "ci_upper_95": float("nan"),
            "std": float("nan"),
            "min": float(pval),   # p-value stored in 'min' column for convenience
            "max": float("nan"),
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
            "device_id": dev_id,
            "mean_FAR": float(np.nanmean(fars)),
            "std_FAR": float(np.nanstd(fars)),
            "n_episodes": len(fars),
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
