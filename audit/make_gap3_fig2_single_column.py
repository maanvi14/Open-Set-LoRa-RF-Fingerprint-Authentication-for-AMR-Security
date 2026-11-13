"""Create readable one-column versions of the approved Fig. 2 panels."""
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.legend_handler import HandlerTuple


ROOT = Path(__file__).resolve().parent.parent
TABLES = ROOT / "results" / "tables"
OUT = ROOT / "paper" / "figures"
BLUE, ORANGE, GREY = "#0072B2", "#D55E00", "#888888"
LS = [1, 3, 5]


def p(value):
    return float(value) * 100


def pct(value):
    return f"{Decimal(str(value)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP):.1f}%"


summary = pd.read_csv(TABLES / "burst_robust_summary.csv")
episodes = pd.read_csv(TABLES / "burst_robust_results.csv")
trade = pd.read_csv(TABLES / "threshold_tradeoff.csv")


def means(threshold, metric):
    return np.array([p(summary.loc[(summary.threshold == threshold) &
                                  (summary.burst_length == L), metric].iloc[0]) for L in LS])


def sems(threshold, metric):
    out = []
    for L in LS:
        vals = episodes.loc[(episodes.threshold == threshold) &
                            (episodes.burst_length == L), metric]
        if len(vals) != 20:
            raise ValueError(f"Expected 20 episode values for {threshold}, L={L}; got {len(vals)}")
        out.append(vals.std(ddof=1) / np.sqrt(len(vals)) * 100)
    return np.array(out)


fy, ry = means("youden", "FAR_B"), means("youden", "FRR")
fo, ro = means("robust", "FAR_B"), means("robust", "FRR")
se_fy, se_ry = sems("youden", "FAR_B"), sems("youden", "FRR")
se_fo, se_ro = sems("robust", "FAR_B"), sems("robust", "FRR")
ox = trade.FRR_robust.to_numpy() * 100
oy = trade.FAR_true_robust.to_numpy() * 100
bx = trade.FRR_youden.to_numpy() * 100
by = trade.FAR_true_youden.to_numpy() * 100
offscale = np.flatnonzero((ox > 40) | (bx > 40))


# Panel (a), independently rendered at one-column physical size.
fig, ax = plt.subplots(figsize=(3.5, 4.15))
fig.subplots_adjust(left=0.19, right=0.97, top=0.91, bottom=0.25)
ax.scatter(bx[bx <= 40], by[bx <= 40], s=16, alpha=0.25, color=BLUE, zorder=2)
ax.scatter(ox[ox <= 40], oy[ox <= 40], s=16, alpha=0.25, color=ORANGE, zorder=2)
pts = [
    (ry[0], fy[0], BLUE, "o"), (ry[2], fy[2], BLUE, "D"),
    (ro[0], fo[0], ORANGE, "o"), (ro[2], fo[2], ORANGE, "D"),
]
arrows = [((ry[0], fy[0]), (ry[2], fy[2]), BLUE, "-", 1.5),
          ((ro[0], fo[0]), (ro[2], fo[2]), ORANGE, "-", 1.5),
          ((ry[0], fy[0]), (ro[0], fo[0]), GREY, "--", 1.2)]
for start, end, color, style, width in arrows:
    ax.annotate("", xy=end, xytext=start,
                arrowprops=dict(arrowstyle="-|>", color=color, linestyle=style,
                                lw=width, mutation_scale=10), zorder=5)
for x, y, color, marker in pts:
    ax.scatter(x, y, s=120, marker=marker, color=color, edgecolor="white",
               linewidth=0.9, zorder=12)
ax.text(6.5, 14.8,
        "stricter threshold", color="#777777", fontsize=6.5,
        ha="center", va="bottom", bbox=dict(fc="white", ec="none", alpha=0.85, pad=0.6))

# Short two-line mean labels and leader lines fit the narrower column layout.
label_specs = [
    (ry[0], fy[0], f"Baseline L=1\nFAR$_B$ {pct(fy[0])}, FRR {pct(ry[0])}", BLUE, (12.0, 18.8), "left"),
    (ry[2], fy[2], f"Baseline L=5\nFAR$_B$ {pct(fy[2])}, FRR {pct(ry[2])}", BLUE, (0.5, 6.4), "left"),
    (ro[0], fo[0], f"Strict L=1\nFAR$_B$ {pct(fo[0])}, FRR {pct(ro[0])}", ORANGE, (29.0, 2.3), "right"),
    (ro[2], fo[2], f"Strict L=5\nFAR$_B$ {pct(fo[2])}, FRR {pct(ro[2])}", ORANGE, (19.0, 13.0), "left"),
]
labels = []
for x, y, txt, color, pos, ha in label_specs:
    labels.append(ax.annotate(txt, xy=(x, y), xytext=pos, textcoords="data",
                              ha=ha, va="center", fontsize=6.5, fontweight="bold",
                              color=color, arrowprops=dict(arrowstyle="-", color=color, lw=0.65),
                              bbox=dict(boxstyle="round,pad=0.18", fc="white", ec="#cccccc", alpha=0.96),
                              zorder=10))
ax.text(0.98, 0.985,
        "Off-scale strict FRR: " + ", ".join(
            f"Ep {int(trade.iloc[i].episode)} {pct(ox[i])}" for i in offscale),
        transform=ax.transAxes, ha="right", va="top", fontsize=6.1, color="#555555")
ax.set_xlim(0, 40)
ax.set_ylim(0, 26)
ax.set_xlabel("False rejection of legitimate meters, FRR (%)", fontsize=7.4, labelpad=3)
ax.set_ylabel("True-stranger penetration, FAR$_B$ (%)", fontsize=7.4, labelpad=3)
ax.set_title("Operating points: threshold and burst length", fontsize=8.3, fontweight="bold", pad=5)
ax.grid(alpha=0.22, linewidth=0.5)
proxy_handles = [
    Line2D([], [], marker="o", linestyle="none", markersize=4, markerfacecolor=BLUE, markeredgecolor="white"),
    Line2D([], [], marker="o", linestyle="none", markersize=4, markerfacecolor=ORANGE, markeredgecolor="white"),
    (Line2D([], [], marker="o", linestyle="none", markersize=5, markerfacecolor="#555555", markeredgecolor="white"),
     Line2D([], [], marker="D", linestyle="none", markersize=5, markerfacecolor="#555555", markeredgecolor="white")),
]
ax.legend(proxy_handles, ["Baseline episodes, L=1", "Strict episodes, L=1",
                          "Mean: circle L=1, diamond L=5"],
          handler_map={tuple: HandlerTuple(ndivide=None)}, loc="upper left",
          bbox_to_anchor=(0.01, -0.22), ncol=1, fontsize=6.3,
          frameon=False, handletextpad=0.5, labelspacing=0.25)
fig.savefig(OUT / "gap3_fig2_panel_a.png", dpi=300, bbox_inches="tight")
fig.savefig(OUT / "gap3_fig2_panel_a.pdf", bbox_inches="tight")
plt.close(fig)


# Panel (b), independently rendered with the same means, +/-1 SE bands and callout.
fig, ax = plt.subplots(figsize=(3.5, 3.55))
fig.subplots_adjust(left=0.17, right=0.97, top=0.86, bottom=0.29)
series = [
    (fy, se_fy, BLUE, "s", "-", r"Baseline FAR$_B$ ($\tau_{\mathrm{Youden}}$)"),
    (ry, se_ry, BLUE, "o", "--", r"Baseline FRR ($\tau_{\mathrm{Youden}}$)"),
    (fo, se_fo, ORANGE, "s", "-", r"Strict FAR$_B$ ($\tau_{\mathrm{robust}}$)"),
    (ro, se_ro, ORANGE, "o", "--", r"Strict FRR ($\tau_{\mathrm{robust}}$)"),
]
for vals, err, color, marker, style, name in series:
    ax.errorbar(LS, vals, yerr=err, fmt=marker, linestyle=style, color=color,
                linewidth=1.35, markersize=4.3, capsize=2.5, capthick=0.8,
                label=name, zorder=4)
    ax.fill_between(LS, vals-err, vals+err, color=color, alpha=0.10, zorder=1)
for i, L in enumerate(LS):
    for vals, color, series_name in ((fy, BLUE, "baseline FAR_B"), (ry, BLUE, "baseline FRR"),
                                     (fo, ORANGE, "strict FAR_B"), (ro, ORANGE, "strict FRR")):
        offset = (4, 0)
        if L == 3 and series_name == "baseline FRR":
            offset = (4, -7)
        elif L == 3 and series_name == "strict FAR_B":
            offset = (4, 7)
        ax.annotate(pct(vals[i]), (L, vals[i]), xytext=offset, textcoords="offset points",
                    ha="left", va="center", color=color, fontsize=6.5,
                    fontweight="bold", bbox=dict(fc="white", ec="none", alpha=0.9, pad=0.5))
drop = Decimal(pct(ro[0]).replace("%", "")) - Decimal(pct(ro[2]).replace("%", ""))
rise = Decimal(pct(fo[2]).replace("%", "")) - Decimal(pct(fo[0]).replace("%", ""))
ax.text(0.98, 0.98,
        f"Strict ($\\tau_{{\\mathrm{{robust}}}}$), L=1 → 5: FRR {pct(ro[0])} → {pct(ro[2])} (-{drop:.1f} pp);\n"
        f"FAR$_B$ {pct(fo[0])} → {pct(fo[2])} (+{rise:.1f} pp)",
        transform=ax.transAxes, ha="right", va="top", fontsize=6.4, color=ORANGE,
        bbox=dict(boxstyle="round,pad=0.22", fc="white", ec=ORANGE, alpha=0.96), zorder=9)
ax.set_title("Burst fusion lowers FRR at both thresholds;\nFAR$_B$ rises modestly at strict threshold",
             fontsize=8.0, fontweight="bold", pad=5)
ax.set_xlabel("Burst length L (consecutive packets fused)", fontsize=7.4, labelpad=3)
ax.set_ylabel("Error rate (%)", fontsize=7.4, labelpad=3)
ax.set_xticks(LS)
ax.set_xlim(0.65, 6.0)
ax.set_ylim(0, 38)
ax.grid(alpha=0.22, linewidth=0.5)
ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.19), ncol=2,
          fontsize=5.7, frameon=True, framealpha=0.95, edgecolor="#cccccc",
          columnspacing=0.9, handlelength=1.6, labelspacing=0.2)
fig.savefig(OUT / "gap3_fig2_panel_b.png", dpi=300, bbox_inches="tight")
fig.savefig(OUT / "gap3_fig2_panel_b.pdf", bbox_inches="tight")
plt.close(fig)

print(f"Excluded dots with FRR > 40%: {len(offscale)} episodes: " +
      ", ".join(f"Ep {int(trade.iloc[i].episode)} ({trade.iloc[i].FRR_robust*100:.6f}%)" for i in offscale))
print("Created one-column panel assets: gap3_fig2_panel_a/b.png and .pdf")
