import pandas as pd
import numpy as np
from pathlib import Path

TABLES = Path('results/tables')

tt   = pd.read_csv(TABLES/'threshold_tradeoff.csv')
bas  = pd.read_csv(TABLES/'burst_aggregation_summary.csv', index_col='burst_length')
ss   = pd.read_csv(TABLES/'stats_summary.csv')
ep   = pd.read_csv(TABLES/'episode_summary.csv')

def g(metric):
    return ss[ss['metric']==metric].iloc[0]

print('=== ALL VERIFIED NUMBERS ===')
row = g('FAR_A')
print(f"FAR_A device-level mean: {row['mean']*100:.4f}%  CI:[{row['ci_lower_95']*100:.2f}%, {row['ci_upper_95']*100:.2f}%]")
row = g('FAR_B')
print(f"FAR_B device-level mean: {row['mean']*100:.4f}%  CI:[{row['ci_lower_95']*100:.2f}%, {row['ci_upper_95']*100:.2f}%]")
row = g('FRR')
print(f"FRR   episode mean:       {row['mean']*100:.4f}%  CI:[{row['ci_lower_95']*100:.2f}%, {row['ci_upper_95']*100:.2f}%]")
row = g('AUROC_B')
print(f"AUROC_B episode mean:     {row['mean']:.4f}  CI:[{row['ci_lower_95']:.4f}, {row['ci_upper_95']:.4f}]")
row = g('AUROC_A')
print(f"AUROC_A episode mean:     {row['mean']:.4f}  CI:[{row['ci_lower_95']:.4f}, {row['ci_upper_95']:.4f}]")
row = g('macro_F1')
print(f"macro_F1 episode mean:    {row['mean']*100:.4f}%  CI:[{row['ci_lower_95']*100:.4f}%, {row['ci_upper_95']*100:.4f}%]")
row = g('DeltaFAR')
print(f"DeltaFAR episode mean:    {row['mean']*100:.4f}%  CI:[{row['ci_lower_95']*100:.4f}%, {row['ci_upper_95']*100:.4f}%]")

print()
print(f"FAR_B robust ep mean:   {tt['FAR_true_robust'].mean()*100:.4f}%")
print(f"FRR_robust ep mean:     {tt['FRR_robust'].mean()*100:.4f}%")
peak_ep = tt['FRR_robust'].idxmax()
print(f"FRR_robust peak:        {tt['FRR_robust'].max()*100:.4f}% (episode {peak_ep})")
print(f"FAR_B baseline ep mean: {tt['FAR_true_youden'].mean()*100:.4f}%")
print(f"FRR baseline ep mean:   {tt['FRR_youden'].mean()*100:.4f}%")

print()
for L in [1, 3, 5]:
    r = bas.loc[L]
    print(f"Burst L={L}: FAR_A={r['FAR_A']*100:.4f}%  FAR_B={r['FAR_B']*100:.4f}%  FRR={r['FRR']*100:.4f}%  DeltaFAR={r['DeltaFAR']*100:.4f}%  AUROC={r['AUROC']:.6f}")

print()
md_path = TABLES / 'matched_device_evaluation.csv'
if md_path.exists():
    md = pd.read_csv(md_path)
    dev_agg = md.groupby('device_id')['delta_far_matched'].mean()
    print(f"Device-matched DeltaFAR (dev-level mean): {dev_agg.mean()*100:.4f}%")
    print(f"  n devices: {len(dev_agg)}")

print()
print(f"Episode summary columns: {list(ep.columns)}")
print(f"ep AUROC_A mean: {ep['AUROC_A'].mean():.4f}")
print(f"ep AUROC_B mean: {ep['AUROC_B'].mean():.4f}")
print(f"ep macro_F1 mean: {ep['macro_F1'].mean()*100:.4f}%")
print(f"ep DeltaFAR mean: {ep['DeltaFAR'].mean()*100:.4f}%")
print(f"ep FAR_A mean: {ep['FAR_A'].mean()*100:.4f}%")
print(f"ep FAR_B mean: {ep['FAR_B'].mean()*100:.4f}%")
print(f"ep FRR mean: {ep['FRR'].mean()*100:.4f}%")

# Check proxy sweep
import os
sw_path = Path('results/sweep')
if sw_path.exists():
    files = list(sw_path.glob('*.csv'))
    print(f"\nSweep files: {[f.name for f in files]}")
    for f in files:
        df_sw = pd.read_csv(f)
        print(f"  {f.name} cols: {list(df_sw.columns)}")
        print(df_sw.to_string())

