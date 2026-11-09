"""
scripts/07_burst_aggregation_experiment.py
Multi-Packet Burst Fusion Evaluation across 20 episodes.

Evaluates how temporal multi-packet aggregation (L in {1, 3, 5} packets)
improves stranger discrimination and availability in AMR gateway networks.
"""
import sys
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import numpy as np
import pandas as pd
from sklearn.metrics import roc_auc_score
from src.config import CFG
from src.features import load_all_features
from src.splits import create_episode_split
from src.episodes import _subset_df, _get_feature_cols
from src.model import build_xy, predict_scores, train_model
from src.threshold import calibrate_threshold
from src.utils import ensure_dir, get_logger

LOG = get_logger("07_burst_aggregation")

def aggregate_scores_by_device(scores: np.ndarray, dev_ids: np.ndarray, L: int) -> np.ndarray:
    """Group every L consecutive packets of each device and average their scores."""
    if L == 1:
        return scores
    agg_scores = []
    for d in np.unique(dev_ids):
        d_scores = scores[dev_ids == d]
        n_chunks = len(d_scores) // L
        if n_chunks > 0:
            chunks = d_scores[:n_chunks * L].reshape(n_chunks, L).mean(axis=1)
            agg_scores.extend(chunks)
        else:
            agg_scores.append(d_scores.mean())
    return np.array(agg_scores)

def run_burst_experiment(n_episodes: int = 20) -> pd.DataFrame:
    df_all = load_all_features()
    all_devices = sorted(df_all["device_id"].unique().tolist())
    pkt_counts = df_all.groupby("device_id")["packet_idx"].count().to_dict()
    feat_cols = _get_feature_cols(df_all)

    results = []
    Ls = [1, 3, 5]

    for ep in range(n_episodes):
        LOG.info("Processing Episode %02d/%02d...", ep + 1, n_episodes)
        split = create_episode_split(all_devices, pkt_counts, episode_idx=ep, seed=CFG.episode_seed(ep))
        
        df_trn = _subset_df(df_all, split.enrolled_ids, split.enrolled_train_idx)
        df_val = _subset_df(df_all, split.enrolled_ids, split.enrolled_cal_val_idx)
        df_tst = _subset_df(df_all, split.enrolled_ids, split.enrolled_known_test_idx)
        df_pcal = _subset_df(df_all, split.proxy_ids, split.proxy_cal_idx)
        df_ptst = _subset_df(df_all, split.proxy_ids, split.proxy_test_idx)
        df_ftst = _subset_df(df_all, split.final_unknown_ids, split.final_test_idx)

        X_trn, y_trn = build_xy(df_trn, feat_cols)
        pipe = train_model(X_trn, y_trn, seed=CFG.episode_seed(ep))

        # Raw scores
        s_val_raw = predict_scores(pipe, build_xy(df_val, feat_cols)[0])
        s_pcal_raw = predict_scores(pipe, build_xy(df_pcal, feat_cols)[0])
        s_tst_raw = predict_scores(pipe, build_xy(df_tst, feat_cols)[0])
        s_ptst_raw = predict_scores(pipe, build_xy(df_ptst, feat_cols)[0])
        s_ftst_raw = predict_scores(pipe, build_xy(df_ftst, feat_cols)[0])

        dev_val = df_val["device_id"].to_numpy()
        dev_pcal = df_pcal["device_id"].to_numpy()
        dev_tst = df_tst["device_id"].to_numpy()
        dev_ptst = df_ptst["device_id"].to_numpy()
        dev_ftst = df_ftst["device_id"].to_numpy()

        for L in Ls:
            s_val = aggregate_scores_by_device(s_val_raw, dev_val, L)
            s_pcal = aggregate_scores_by_device(s_pcal_raw, dev_pcal, L)
            s_tst = aggregate_scores_by_device(s_tst_raw, dev_tst, L)
            s_ptst = aggregate_scores_by_device(s_ptst_raw, dev_ptst, L)
            s_ftst = aggregate_scores_by_device(s_ftst_raw, dev_ftst, L)

            tau = calibrate_threshold(s_val, s_pcal, method="youden").tau
            far_a = float(np.mean(s_ptst >= tau))
            far_b = float(np.mean(s_ftst >= tau))
            frr = float(np.mean(s_tst < tau))
            
            y_auc = np.concatenate([np.ones_like(s_tst), np.zeros_like(s_ftst)])
            s_auc = np.concatenate([s_tst, s_ftst])
            auc = float(roc_auc_score(y_auc, s_auc))

            results.append({
                "episode": ep,
                "burst_length": L,
                "tau": tau,
                "FAR_A": far_a,
                "FAR_B": far_b,
                "FRR": frr,
                "DeltaFAR": far_b - far_a,
                "AUROC": auc,
            })

    res_df = pd.DataFrame(results)
    out_dir = CFG.path_results / "tables"
    ensure_dir(out_dir)
    res_df.to_csv(out_dir / "burst_aggregation_results.csv", index=False)
    
    summary = res_df.groupby("burst_length")[["FAR_A", "FAR_B", "FRR", "DeltaFAR", "AUROC"]].mean()
    summary.to_csv(out_dir / "burst_aggregation_summary.csv")
    print("\n=== MULTI-PACKET BURST AGGREGATION SUMMARY (20 EPISODES) ===")
    print(summary.to_string())
    return res_df

if __name__ == "__main__":
    run_burst_experiment()

