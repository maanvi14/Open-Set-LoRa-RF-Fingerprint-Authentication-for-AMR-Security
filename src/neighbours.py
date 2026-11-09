"""
src/neighbours.py
Nearest-enrolled-neighbour analysis.

Computes feature-space distance from each unknown device's centroid
to the nearest enrolled device centroid, then correlates with per-device FAR.

Outputs:
  results/tables/neighbour_analysis.csv
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, List, Optional

import numpy as np
import pandas as pd
from scipy.stats import spearmanr
from sklearn.preprocessing import StandardScaler

from src.config import CFG
from src.features import load_all_features
from src.utils import ensure_dir, get_logger

LOG = get_logger(__name__)


def _compute_centroids(
    df: pd.DataFrame,
    device_ids: List[int],
    feat_cols: List[str],
) -> Dict[int, np.ndarray]:
    """Return {device_id: centroid_vector}."""
    centroids = {}
    for dev_id in device_ids:
        sub = df[df["device_id"] == dev_id][feat_cols].values
        if len(sub) == 0:
            continue
        centroids[dev_id] = sub.mean(axis=0)
    return centroids


def run_neighbour_analysis(
    n_episodes: Optional[int] = None,
) -> pd.DataFrame:
    """
    For each episode, compute distance from unknown device centroid to
    nearest enrolled device centroid, then correlate with per-device FAR.

    Returns combined DataFrame saved to results/tables/neighbour_analysis.csv.
    """
    if n_episodes is None:
        n_episodes = CFG.n_episodes

    ep_dir = CFG.path_results / "episodes"

    LOG.info("Loading features …")
    df_all = load_all_features()
    meta_cols = {"device_id", "packet_idx", "source_file"}
    feat_cols = [c for c in df_all.columns if c not in meta_cols]

    # Fit scaler on the entire dataset (for distance computation only — no labels used)
    scaler = StandardScaler()
    df_all_scaled = df_all.copy()
    df_all_scaled[feat_cols] = scaler.fit_transform(df_all[feat_cols].values)

    all_rows = []

    for ep_idx in range(n_episodes):
        p = ep_dir / f"episode_{ep_idx:03d}.json"
        if not p.exists():
            continue
        with open(p) as fh:
            res = json.load(fh)

        enrolled_ids   = [int(x) for x in res.get("enrolled_ids", [])]
        final_unk_ids  = [int(x) for x in res.get("final_unknown_ids", [])]
        pdev_far_b     = {int(k): float(v) for k, v in res.get("per_device_FAR_B", {}).items()}

        # Centroids
        en_centroids = _compute_centroids(df_all_scaled, enrolled_ids, feat_cols)
        fu_centroids = _compute_centroids(df_all_scaled, final_unk_ids, feat_cols)

        en_matrix = np.stack(list(en_centroids.values()), axis=0)  # (n_enrolled, n_feat)

        for dev_id, centroid in fu_centroids.items():
            if dev_id not in pdev_far_b:
                continue
            # Euclidean distance to each enrolled centroid
            diffs = en_matrix - centroid
            dists = np.linalg.norm(diffs, axis=1)
            nearest_dist = float(dists.min())
            nearest_enrolled = list(en_centroids.keys())[int(dists.argmin())]

            all_rows.append({
                "episode": ep_idx,
                "device_id": dev_id,
                "nearest_enrolled": nearest_enrolled,
                "nearest_dist": nearest_dist,
                "FAR_B": pdev_far_b[dev_id],
            })

    if not all_rows:
        LOG.warning("No neighbour analysis data found. Run episodes first.")
        return pd.DataFrame()

    df_nb = pd.DataFrame(all_rows)

    # To avoid pseudo-replication from repeating the same physical transmitters across 20 episodes,
    # aggregate to a single mean distance and mean FAR_B per unique physical device
    df_dev = df_nb.groupby("device_id")[["nearest_dist", "FAR_B"]].mean().reset_index()

    dist_col = df_dev["nearest_dist"].values
    far_col  = df_dev["FAR_B"].values
    if len(dist_col) >= 4:
        rho, pval = spearmanr(dist_col, far_col)
    else:
        rho, pval = float("nan"), float("nan")

    LOG.info("Device-level aggregated Spearman rho(distance, FAR_B) = %.4f  p=%.4f (n=%d unique devices)",
             rho, pval, len(df_dev))
    df_nb["device_level_rho"] = rho
    df_nb["device_level_pval"] = pval

    ensure_dir(CFG.path_tables)
    out_path = CFG.path_tables / "neighbour_analysis.csv"
    df_nb.to_csv(out_path, index=False)
    LOG.info("Neighbour analysis saved → %s", out_path)
    return df_nb


if __name__ == "__main__":
    LOG.info("neighbours.py self-test …")
    try:
        df = run_neighbour_analysis(n_episodes=1)
        print(df)
    except FileNotFoundError as e:
        LOG.warning("No data found (expected during dev): %s", e)
    LOG.info("neighbours.py self-test complete.")
