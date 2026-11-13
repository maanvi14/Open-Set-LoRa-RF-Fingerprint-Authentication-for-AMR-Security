"""
audit/make_gap3.py
Regenerate gap3_security_availability figure from CSVs.
Outputs: audit/gap3_regenerated.png
Run from project root: python audit/make_gap3.py
"""
import sys
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyArrowPatch

ROOT = Path(__file__).resolve().parent.parent
TABLES = ROOT / "results" / "tables"
OUT_DIR = ROOT / "audit"
OUT_DIR.mkdir(exist_ok=True)

# Load data
tt  = pd.read_csv(TABLES / "threshold_tradeoff.csv")
bas = pd.read_csv(TABLES / "burst_aggregation_summary.csv", index_col="burst_length")

# --- Compute means for annotation ---
mean_frr_y  = tt["FRR_youden"].mean()   * 100
mean_farb_y = tt["FAR_true_youden"].mean() * 100
mean_frr_r  = tt["FRR_robust"].mean()   * 100
mean_farb_r = tt["FAR_true_robust"].mean() * 100

L_vals   = [1, 3, 5]
farb_L   = [bas.loc[L, "FAR_B"] * 100 for L in L_vals]
frr_L    = [bas.loc[L, "FRR"]   * 100 for L in L_vals]

print(f"Baseline: FRR={mean_frr_y:.2f}%, FAR_B={mean_farb_y:.2f}%")
print(f"Robust:   FRR={mean_frr_r:.2f}%, FAR_B={mean_farb_r:.2f}%")
print(f"L=1: FAR_B={farb_L[0]:.1f}%, FRR={frr_L[0]:.1f}%")
print(f"L=3: FAR_B={farb_L[1]:.1f}%, FRR={frr_L[1]:.1f}%")
print(f"L=5: FAR_B={farb_L[2]:.1f}%, FRR={frr_L[2]:.1f}%")

# Color scheme (colorblind-safe: use blue/red from Wong palette)
# Baseline=dodgerblue, Robust=salmon → original uses these
c_base = "#4393c3"   # blue (colorblind-safe)
c_rob  = "#d6604d"   # red  (colorblind-safe)
c_farb = "#d6604d"   # red  for FAR_B line
c_frr  = "#4dac26"   # green for FRR line

fig, axes = plt.subplots(1, 2, figsize=(12, 5))
fig.subplots_adjust(wspace=0.35)

# ===========================================================================
# Panel (a): Scatter of per-episode (FRR, FAR_B), means + arrow
# ===========================================================================
ax = axes[0]

# Per-episode scatter
ax.scatter(tt["FRR_youden"] * 100, tt["FAR_true_youden"] * 100,
           s=40, alpha=0.6, color=c_base, label="Baseline τ, per episode", zorder=3)
ax.scatter(tt["FRR_robust"] * 100, tt["FAR_true_robust"] * 100,
           s=40, alpha=0.6, color=c_rob,  label="Robust τ, per episode",   zorder=3)

# Mean dots (large)
ax.scatter(mean_frr_y, mean_farb_y, s=180, color=c_base, edgecolors="k", linewidths=1.2, zorder=5)
ax.scatter(mean_frr_r, mean_farb_r, s=180, color=c_rob,  edgecolors="k", linewidths=1.2, zorder=5)

# Arrow baseline → robust
ax.annotate("",
    xy=(mean_frr_r, mean_farb_r),
    xytext=(mean_frr_y, mean_farb_y),
    arrowprops=dict(arrowstyle="-|>", color="black", lw=1.5, mutation_scale=14),
    zorder=6)

# Annotations for means
ax.annotate(
    f"Baseline\nFAR {mean_farb_y:.1f}%, FRR {mean_frr_y:.1f}%",
    xy=(mean_frr_y, mean_farb_y),
    xytext=(mean_frr_y + 2, mean_farb_y + 1.5),
    fontsize=8.5, color=c_base,
    arrowprops=dict(arrowstyle="-", color=c_base, lw=0.8),
)
ax.annotate(
    f"Robust\nFAR {mean_farb_r:.1f}%, FRR {mean_frr_r:.1f}%",
    xy=(mean_frr_r, mean_farb_r),
    xytext=(mean_frr_r + 2.5, mean_farb_r + 2),
    fontsize=8.5, color=c_rob,
    arrowprops=dict(arrowstyle="-", color=c_rob, lw=0.8),
)

ax.set_xlabel("False rejection of legitimate meters, FRR (%)\n→ worse availability", fontsize=10)
ax.set_ylabel("True-stranger penetration, FAR_B (%)\n→ worse security", fontsize=10)
ax.set_title("(a) Stricter threshold: security gain costs availability", fontsize=10, fontweight="bold")
ax.legend(fontsize=8.5, loc="upper right")
ax.set_xlim(left=0)
ax.set_ylim(bottom=0)
ax.grid(True, alpha=0.3)

# ===========================================================================
# Panel (b): FRR and FAR_B vs burst length L
# ===========================================================================
ax2 = axes[1]

ax2.plot(L_vals, farb_L, "s-", color=c_farb, linewidth=2, markersize=8, label="FAR_B (strangers accepted)")
ax2.plot(L_vals, frr_L,  "o-", color=c_frr,  linewidth=2, markersize=8, label="FRR (legit rejected)")

# Annotate data points — offset to avoid clipping
offsets_farb = [(-.25, 0.3), (-.25, 0.3), (.1, 0.3)]
offsets_frr  = [(-.3, 0.3),  (-.3, 0.3),  (.1, 0.35)]

for i, (L, fb, fr) in enumerate(zip(L_vals, farb_L, frr_L)):
    ox_b, oy_b = offsets_farb[i]
    ox_r, oy_r = offsets_frr[i]
    ax2.annotate(f"{fb:.1f}", xy=(L, fb), xytext=(L + ox_b, fb + oy_b),
                 fontsize=8.5, color=c_farb, fontweight="bold")
    ax2.annotate(f"{fr:.1f}", xy=(L, fr), xytext=(L + ox_r, fr + oy_r),
                 fontsize=8.5, color=c_frr, fontweight="bold")

ax2.set_xlabel("Burst length L (packets fused)", fontsize=10)
ax2.set_ylabel("Rate (%)", fontsize=10)
ax2.set_title("(b) Burst fusion recovers availability at no FAR cost", fontsize=10, fontweight="bold")
ax2.set_xticks(L_vals)
ax2.legend(fontsize=8.5, loc="center right")
ax2.set_xlim(0.5, 5.8)
ax2.set_ylim(bottom=0)   # zero baseline (fix original non-zero issue)
ax2.grid(True, alpha=0.3)

fig.suptitle("Fig. gap3_regenerated — from CSVs, episode means", fontsize=10, style="italic", y=0.01)

out_path = OUT_DIR / "gap3_regenerated.png"
fig.savefig(out_path, dpi=150, bbox_inches="tight")
print(f"Saved: {out_path}")
plt.close(fig)

