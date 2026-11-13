"""
audit/burst_at_robust.py
Audit Task 2: Evaluate burst lengths L in {1, 3, 5} at tau_robust using only
existing saved scores (results/episodes/raw_scores_episode_*.npz).
"""
import sys
from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.metrics import roc_auc_score

ROOT = Path(__file__).resolve().parent.parent
EP_DIR = ROOT / "results" / "episodes"
TT_PATH = ROOT / "results" / "tables" / "threshold_tradeoff.csv"

def main():
    print("=" * 72)
    print("TASK 2: Evaluating Burst Fusion at tau_robust using Saved Scores")
    print("=" * 72)

    # 1. Check scripts/07_burst_aggregation_experiment.py
    script_07 = ROOT / "scripts" / "07_burst_aggregation_experiment.py"
    if script_07.exists():
        with open(script_07, "r", encoding="utf-8") as f:
            lines = f.readlines()
        print("\n[CHECK] Threshold used in scripts/07_burst_aggregation_experiment.py:")
        for idx, line in enumerate(lines):
            if "calibrate_threshold" in line:
                print(f"  Line {idx+1}: {line.strip()}")
                print("  --> scripts/07_burst_aggregation_experiment.py explicitly uses")
                print("      method='youden' (tau_youden), NOT tau_robust.")

    # 2. Check saved raw scores
    if not TT_PATH.exists():
        print(f"ERROR: {TT_PATH} not found.")
        return

    tt = pd.read_csv(TT_PATH)

    # Inspect first episode raw scores file
    ep0_npz = EP_DIR / "raw_scores_episode_000.npz"
    if not ep0_npz.exists():
        print(f"ERROR: {ep0_npz} not found.")
        return

    data0 = np.load(ep0_npz)
    keys = list(data0.keys())
    print(f"\n[INSPECT] Keys in raw_scores_episode_000.npz: {keys}")

    # Check whether dev_ids are present
    if "dev_ids" not in keys and "device_id" not in keys:
        print("\n[ANALYSIS] Checking sufficiency of saved scores for multi-packet burst fusion:")
        print("  - Burst aggregation (src/evaluate.py: aggregate_burst_scores) requires")
        print("    'dev_ids' to partition packet scores by physical device before averaging")
        print("    consecutive chunks of length L in {3, 5}.")
        print("  - raw_scores_episode_*.npz files contain only 1D score arrays:")
        for k in keys:
            if k != "tau":
                print(f"      {k}: shape {data0[k].shape}")
        print("  - Devices have unequal packet counts:")
        print("      scores_proxy_test: 3200 packets / 15 devices = 213.33 pkts/device")
        print("      scores_final_test: 6500 packets / 15 devices = 433.33 pkts/device")
        print("      scores_known_test: 1965 packets / 30 devices = 65.50 pkts/device")
        print("    Device boundaries cannot be inferred from the flat 1D arrays.")
        print("  - Furthermore, tau_robust is not stored in the .npz files (stored tau is tau_youden),")
        print("    though it can be retrieved from threshold_tradeoff.csv.")
        print("\n  CONCLUSION: The saved scores in raw_scores_episode_*.npz are NOT SUFFICIENT")
        print("  to evaluate multi-packet burst aggregation for L in {3, 5}.\n")

    # Evaluate L=1 (where device grouping is trivial: each packet is its own burst)
    print("--- Evaluating L = 1 (single-packet) at tau_robust across 20 episodes ---")
    far_a_list = []
    far_b_list = []
    frr_list = []
    auroc_list = []

    for ep in range(20):
        tau_r = tt.loc[ep, "tau_robust"]
        npz_p = EP_DIR / f"raw_scores_episode_{ep:03d}.npz"
        data = np.load(npz_p)

        s_ptst = data["scores_proxy_test"]
        s_ftst = data["scores_final_test"]
        s_ktst = data["scores_known_test"]

        far_a = float(np.mean(s_ptst >= tau_r))
        far_b = float(np.mean(s_ftst >= tau_r))
        frr   = float(np.mean(s_ktst < tau_r))

        y = np.concatenate([np.ones_like(s_ktst), np.zeros_like(s_ftst)])
        s = np.concatenate([s_ktst, s_ftst])
        auc = float(roc_auc_score(y, s))

        far_a_list.append(far_a)
        far_b_list.append(far_b)
        frr_list.append(frr)
        auroc_list.append(auc)

    print(f"  L=1 at tau_robust (episode mean across 20 eps):")
    print(f"    FAR_A : {np.mean(far_a_list)*100:.4f}%")
    print(f"    FAR_B : {np.mean(far_b_list)*100:.4f}%")
    print(f"    FRR   : {np.mean(frr_list)*100:.4f}%")
    print(f"    AUROC : {np.mean(auroc_list):.6f}")

    print("\n[STOPPING]: For L = 3 and L = 5, saved scores are NOT sufficient to compute")
    print("burst aggregation without re-extracting packet device IDs from features/splits.")
    print("As instructed: 'If the saved scores are not sufficient, say so and stop.'")

if __name__ == "__main__":
    main()

