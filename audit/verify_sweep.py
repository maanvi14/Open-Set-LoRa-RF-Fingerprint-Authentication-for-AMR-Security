import pandas as pd, numpy as np
from pathlib import Path

sw = pd.read_csv(Path('results/sweep/sweep_results.csv'))

print("=== PROXY SWEEP k=1 numbers ===")
k1 = sw[sw['k']==1]
print(f"k=1 FAR_A mean (20 eps): {k1['FAR_A'].mean()*100:.4f}%")
print(f"k=1 FAR_B mean (20 eps): {k1['FAR_B'].mean()*100:.4f}%")
print(f"k=1 DeltaFAR mean:       {k1['DeltaFAR'].mean()*100:.4f}%")
print(f"k=1 FRR mean:            {k1['FRR'].mean()*100:.4f}%")

print()
print("=== ALL k values ===")
for k in [0,1,3,5,10,15]:
    sub = sw[sw['k']==k]
    fa = sub['FAR_A'].mean()*100
    fb = sub['FAR_B'].mean()*100
    df = sub['DeltaFAR'].mean()*100
    print(f"k={k:>2}: FAR_A={fa:>8.4f}%  FAR_B={fb:>8.4f}%  DeltaFAR={df:>8.4f}%")

print()
# k=1: single-proxy distortion gap — README says +19.41%, FAR_A=2.67%, FAR_B=22.08%
print("README claims k=1: FAR_A=2.67%, FAR_B=22.08%, gap=+19.41%")
print(f"Recomputed k=1: FAR_A={k1['FAR_A'].mean()*100:.2f}%, FAR_B={k1['FAR_B'].mean()*100:.2f}%, DeltaFAR={k1['DeltaFAR'].mean()*100:.2f}%")

