"""
scripts/07b_burst_robust.py
Multi-Packet Burst Fusion Evaluation across 20 episodes at BOTH tau_youden and tau_robust.

Evaluates how temporal multi-packet aggregation (L in {1, 3, 5} packets)
performs under both the baseline Youden threshold and the identity-robust threshold.
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
from src.evaluate import aggregate_burst_scores, compute_far, compute_frr
from src.threshold import calibrate_threshold
from src.lopo import _compute_tau_robust
from src.utils import ensure_dir, get_logger

LOG = get_logger("07b_burst_robust")

aggregate_scores_by_device = aggregate_burst_scores

def run_burst_robust_experiment(n_episodes: int = 20) -> tuple[pd.DataFrame, pd.DataFrame]:
    df_all = load_all_features()
    all_devices = sorted(df_all["device_id"].unique().tolist())
    pkt_counts = df_all.groupby("device_id")["packet_idx"].count().to_dict()
    feat_cols = _get_feature_cols(df_all)

    results = []
    Ls = [1, 3, 5]

    for ep in range(n_episodes):
        LOG.info("Processing Episode %02d/%02d...", ep + 1, n_episodes)
        split = create_episode_split(all_devices, pkt_counts, episode_idx=ep, seed=CFG.episode_seed(ep))
        
        df_val = _subset_df(df_all, split.enrolled_ids, split.enrolled_cal_val_idx)
        df_tst = _subset_df(df_all, split.enrolled_ids, split.enrolled_known_test_idx)
        df_pcal = _subset_df(df_all, split.proxy_ids, split.proxy_cal_idx)
        df_ptst = _subset_df(df_all, split.proxy_ids, split.proxy_test_idx)
        df_ftst = _subset_df(df_all, split.final_unknown_ids, split.final_test_idx)

        dev_val = df_val["device_id"].to_numpy()
        dev_pcal = df_pcal["device_id"].to_numpy()
        dev_tst = df_tst["device_id"].to_numpy()
        dev_ptst = df_ptst["device_id"].to_numpy()
        dev_ftst = df_ftst["device_id"].to_numpy()

        # Load cached raw scores if available (fast and deterministic) or train pipe
        npz_path = CFG.path_results / "episodes" / f"raw_scores_episode_{ep:03d}.npz"
        if npz_path.exists():
            data = np.load(npz_path)
            s_val_raw = data["scores_known_val"]
            s_pcal_raw = data["scores_proxy_cal"]
            s_tst_raw = data["scores_known_test"]
            s_ptst_raw = data["scores_proxy_test"]
            s_ftst_raw = data["scores_final_test"]
        else:
            df_trn = _subset_df(df_all, split.enrolled_ids, split.enrolled_train_idx)
            X_trn, y_trn = build_xy(df_trn, feat_cols)
            pipe = train_model(X_trn, y_trn, seed=CFG.episode_seed(ep))
            s_val_raw = predict_scores(pipe, build_xy(df_val, feat_cols)[0])
            s_pcal_raw = predict_scores(pipe, build_xy(df_pcal, feat_cols)[0])
            s_tst_raw = predict_scores(pipe, build_xy(df_tst, feat_cols)[0])
            s_ptst_raw = predict_scores(pipe, build_xy(df_ptst, feat_cols)[0])
            s_ftst_raw = predict_scores(pipe, build_xy(df_ftst, feat_cols)[0])

        for L in Ls:
            s_val = aggregate_scores_by_device(s_val_raw, dev_val, L)
            s_pcal = aggregate_scores_by_device(s_pcal_raw, dev_pcal, L)
            s_tst = aggregate_scores_by_device(s_tst_raw, dev_tst, L)
            s_ptst = aggregate_scores_by_device(s_ptst_raw, dev_ptst, L)
            s_ftst = aggregate_scores_by_device(s_ftst_raw, dev_ftst, L)

            # AUROC is identical across thresholds for a given L
            y_auc = np.concatenate([np.ones_like(s_tst), np.zeros_like(s_ftst)])
            s_auc = np.concatenate([s_tst, s_ftst])
            auc = float(roc_auc_score(y_auc, s_auc))

            # 1. tau_youden calibration
            tau_y = calibrate_threshold(s_val, s_pcal, method="youden").tau
            far_a_y = float(np.mean(s_ptst >= tau_y))
            far_b_y = float(np.mean(s_ftst >= tau_y))
            frr_y = float(np.mean(s_tst < tau_y))

            results.append({
                "episode": ep,
                "threshold": "youden",
                "burst_length": L,
                "tau": tau_y,
                "FAR_A": far_a_y,
                "FAR_B": far_b_y,
                "FRR": frr_y,
                "DeltaFAR": far_b_y - far_a_y,
                "AUROC": auc,
            })

            # 2. tau_robust calibration using src/lopo.py (_compute_tau_robust) on proxy_cal
            pcal_dict_L = {
                d: aggregate_scores_by_device(s_pcal_raw[dev_pcal == d], np.full((dev_pcal == d).sum(), d), L)
                for d in split.proxy_ids
            }
            tau_r = _compute_tau_robust(
                s_val, pcal_dict_L, split.proxy_ids, CFG.lopo_alpha, CFG.lopo_percentile
            )
            far_a_r = float(np.mean(s_ptst >= tau_r))
            far_b_r = float(np.mean(s_ftst >= tau_r))
            frr_r = float(np.mean(s_tst < tau_r))

            results.append({
                "episode": ep,
                "threshold": "robust",
                "burst_length": L,
                "tau": tau_r,
                "FAR_A": far_a_r,
                "FAR_B": far_b_r,
                "FRR": frr_r,
                "DeltaFAR": far_b_r - far_a_r,
                "AUROC": auc,
            })

    res_df = pd.DataFrame(results)
    out_dir = CFG.path_results / "tables"
    ensure_dir(out_dir)
    res_df.to_csv(out_dir / "burst_robust_results.csv", index=False)
    
    summary = res_df.groupby(["threshold", "burst_length"])[["FAR_A", "FAR_B", "FRR", "DeltaFAR", "AUROC"]].mean().reset_index()
    summary.to_csv(out_dir / "burst_robust_summary.csv", index=False)
    print("\n=== MULTI-PACKET BURST FUSION (YOUDEN + ROBUST) SUMMARY (20 EPISODES) ===")
    print(summary.to_string(index=False))
    return res_df, summary

if __name__ == "__main__":
    run_burst_robust_experiment()
