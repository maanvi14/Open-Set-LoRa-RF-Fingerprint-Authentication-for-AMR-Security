"""Generate the data-driven Fig. 2 joint threshold and burst-fusion figure.

Episode index convention: 0-indexed (episode IDs 0..19); Ep 4 is the fifth row.
Blue is tau_Youden, orange is tau_robust. Panel (b) uses solid FAR_B and dashed FRR.
"""
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path
import sys

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


ROOT = Path(__file__).resolve().parent.parent
TABLES = ROOT / "results" / "tables"
EPISODES = ROOT / "results" / "episodes"
OUT_DIR = ROOT / "paper" / "figures"
COLORS = {"youden": "#0072B2", "robust": "#D55E00"}
LS = [1, 3, 5]


def stop_if(condition, message):
    if condition:
        print(f"FAIL: {message}")
        print("STOPPING before figure or caption output.")
        sys.exit(1)


def pct(value):
    return float(value) * 100


def one_decimal(value):
    """Display data-derived percentages to one decimal using decimal half-up."""
    return Decimal(str(value)).quantize(Decimal("0.1"), rounding=ROUND_HALF_UP)


def label(value):
    return f"{one_decimal(value):.1f}%"


# Load source data. All checks below run before creating or replacing any output.
agg = pd.read_csv(TABLES / "burst_aggregation_summary.csv")
rob = pd.read_csv(TABLES / "burst_robust_summary.csv")
rob_ep = pd.read_csv(TABLES / "burst_robust_results.csv")
agg_ep = pd.read_csv(TABLES / "burst_aggregation_results.csv")
trade = pd.read_csv(TABLES / "threshold_tradeoff.csv")

print("DATA CHECK (a): tau_Youden summary equals burst_aggregation_summary.csv")
youden = (rob[rob.threshold == "youden"].sort_values("burst_length").reset_index(drop=True))
agg = agg.sort_values("burst_length").reset_index(drop=True)
cols = ["burst_length", "FAR_A", "FAR_B", "FRR", "DeltaFAR", "AUROC"]
same = youden[cols].equals(agg[cols])
for col in cols:
    if col == "burst_length":
        print(f"  {col}: {'EXACT' if np.array_equal(youden[col], agg[col]) else 'DIFF'}")
    else:
        equal = np.array_equal(youden[col].to_numpy(), agg[col].to_numpy())
        print(f"  {col}: {'EXACT' if equal else 'DIFF'}")
stop_if(not same, "tau_Youden rows do not reproduce burst_aggregation_summary.csv exactly")

print("\nDATA CHECK (b): tau_robust L=1 expected rates")
r1 = rob[(rob.threshold == "robust") & (rob.burst_length == 1)]
stop_if(len(r1) != 1, "expected one tau_robust L=1 summary row")
r1 = r1.iloc[0]
got_b = (pct(r1.FAR_A), pct(r1.FAR_B), pct(r1.FRR))
print(f"  FAR_A={got_b[0]:.6f}% FAR_B={got_b[1]:.6f}% FRR={got_b[2]:.6f}%")
stop_if(not all(abs(x-y) < 0.0051 for x, y in zip(got_b, (3.97, 4.43, 30.08))),
        "tau_robust L=1 does not round to 3.97%, 4.43%, 30.08%")
print("  PASS")

# Every summary rate is based on the corresponding per-episode rows; SE is
# calculated across the paired episode outcomes (sample SD / sqrt(n)).
rows = {}
print("\nDATA CHECK (c): unrounded rates (%) and SEs for both thresholds")
head = f"{'threshold':<9} {'L':>2} {'FAR_B':>12} {'FRR':>12} {'FAR_A':>12} {'DeltaFAR':>12} {'SE FAR_B':>10} {'SE FRR':>10} {'SE FAR_A':>10} {'SE DeltaFAR':>12}"
print(head)
print("-" * len(head))
for threshold in ("youden", "robust"):
    for L in LS:
        summary = rob[(rob.threshold == threshold) & (rob.burst_length == L)]
        ep = rob_ep[(rob_ep.threshold == threshold) & (rob_ep.burst_length == L)]
        stop_if(len(summary) != 1 or len(ep) != 20, f"expected one summary and 20 episode rows for {threshold}, L={L}")
        s = summary.iloc[0]
        n = len(ep)
        se = {m: ep[m].std(ddof=1) / np.sqrt(n) * 100 for m in ("FAR_B", "FRR", "FAR_A", "DeltaFAR")}
        rows[threshold, L] = {m: pct(s[m]) for m in ("FAR_B", "FRR", "FAR_A", "DeltaFAR")}
        rows[threshold, L].update({f"SE_{m}": se[m] for m in se})
        print(f"{threshold:<9} {L:>2} {rows[threshold,L]['FAR_B']:12.8f} {rows[threshold,L]['FRR']:12.8f} {rows[threshold,L]['FAR_A']:12.8f} {rows[threshold,L]['DeltaFAR']:12.8f} {se['FAR_B']:10.4f} {se['FRR']:10.4f} {se['FAR_A']:10.4f} {se['DeltaFAR']:12.4f}")

# Verify total raw transmissions by counting the per-packet feature rows from
# the 60 device tables (each row is one raw packet transmission).
feature_files = sorted((ROOT / "data" / "features").glob("device_*_features.parquet"))
stop_if(len(feature_files) != 60, f"expected 60 per-device feature files, found {len(feature_files)}")
device_counts = [len(pd.read_parquet(path)) for path in feature_files]
N = sum(device_counts)
print(f"\nDATA CHECK N: {len(feature_files)} device tables, per-device packet rows sum to {N:,}")
stop_if(N != 26000, f"expected N=26,000 raw transmissions, observed {N:,}")

# Outlier uses the same 0-indexed episode convention as the audit CSV.
stop_if(len(trade) != 20, f"expected 20 episodes in threshold_tradeoff.csv, found {len(trade)}")
outlier_idx = int(trade["FRR_robust"].idxmax())
stop_if(outlier_idx != 4, f"expected Ep 4 outlier, found Ep {outlier_idx}")
outlier_frr = pct(trade.loc[outlier_idx, "FRR_robust"])
outlier_farb = pct(trade.loc[outlier_idx, "FAR_true_robust"])
stop_if(abs(outlier_frr - 84.6) >= 0.05 or abs(outlier_farb - 4.3) >= 0.05,
        "Ep 4 values do not round to FRR 84.6%, FAR_B 4.3%")

# Data-driven plotted labels and explicit comparisons with rounded CSV rates.
print("\nDATA CHECK (d): plotted labels vs rounded CSV values")
label_mismatches = []
print(f"{'label':<29} {'unrounded CSV (%)':>20} {'rounded label':>16}")
print("-" * 69)
for threshold in ("youden", "robust"):
    for L in LS:
        csvrow = rob[(rob.threshold == threshold) & (rob.burst_length == L)].iloc[0]
        for metric in ("FAR_B", "FRR"):
            actual = one_decimal(pct(csvrow[metric]))
            plotted = one_decimal(rows[threshold, L][metric])
            ok = plotted == actual
            shown = f"{plotted:.1f}%"
            print(f"  {threshold} L={L} {metric}: {pct(csvrow[metric]):20.8f} {shown:>16} [{'OK' if ok else 'MISMATCH'}]")
            if not ok:
                label_mismatches.append(f"{threshold} L={L} {metric}: {shown} != {actual:.1f}%")
stop_if(label_mismatches, "one or more plotted labels differ from the rounded CSV value")
print("  Figure label mismatch list: none")


# Figure starts only after all requested data checks pass.
farb_y = np.array([rows["youden", L]["FAR_B"] for L in LS])
frr_y = np.array([rows["youden", L]["FRR"] for L in LS])
farb_r = np.array([rows["robust", L]["FAR_B"] for L in LS])
frr_r = np.array([rows["robust", L]["FRR"] for L in LS])
se_farb_y = np.array([rows["youden", L]["SE_FAR_B"] for L in LS])
se_frr_y = np.array([rows["youden", L]["SE_FRR"] for L in LS])
se_farb_r = np.array([rows["robust", L]["SE_FAR_B"] for L in LS])
se_frr_r = np.array([rows["robust", L]["SE_FRR"] for L in LS])

fig, (ax, ax2) = plt.subplots(1, 2, figsize=(14.5, 7.0), gridspec_kw={"width_ratios": [1.08, 1]})
fig.subplots_adjust(left=0.09, right=0.98, top=0.87, bottom=0.23, wspace=0.36)

# Panel (a): exclude off-scale episode dots, then show the four mean points.
base_episode_x = trade.FRR_youden.to_numpy() * 100
base_episode_y = trade.FAR_true_youden.to_numpy() * 100
strict_episode_x = trade.FRR_robust.to_numpy() * 100
strict_episode_y = trade.FAR_true_robust.to_numpy() * 100
xmax_a = 40
excluded_dots = int(np.count_nonzero(base_episode_x > xmax_a) + np.count_nonzero(strict_episode_x > xmax_a))
print(f"Episode dots excluded by panel (a) x-limit 0-{xmax_a}: {excluded_dots}")
excluded_episode_ids = np.flatnonzero((base_episode_x > xmax_a) | (strict_episode_x > xmax_a))
print("Excluded episode FRR values: " + "; ".join(
    f"Ep {int(trade.iloc[i]['episode'])}: baseline {base_episode_x[i]:.6f}%, strict {strict_episode_x[i]:.6f}%"
    for i in excluded_episode_ids))
base_visible = base_episode_x <= xmax_a
strict_visible = strict_episode_x <= xmax_a
ax.scatter(base_episode_x[base_visible], base_episode_y[base_visible], s=23, alpha=0.25,
           color=COLORS["youden"], label="Baseline episodes, L=1", zorder=2)
ax.scatter(strict_episode_x[strict_visible], strict_episode_y[strict_visible], s=23, alpha=0.25,
           color=COLORS["robust"], label="Strict episodes, L=1", zorder=2)
points = [
    (frr_y[0], farb_y[0], COLORS["youden"], "o"),
    (frr_y[2], farb_y[2], COLORS["youden"], "D"),
    (frr_r[0], farb_r[0], COLORS["robust"], "o"),
    (frr_r[2], farb_r[2], COLORS["robust"], "D"),
]
ax.annotate("", xy=(frr_y[2], farb_y[2]), xytext=(frr_y[0], farb_y[0]),
            arrowprops=dict(arrowstyle="-|>", color=COLORS["youden"], lw=2.0, mutation_scale=14), zorder=7)
ax.annotate("", xy=(frr_r[2], farb_r[2]), xytext=(frr_r[0], farb_r[0]),
            arrowprops=dict(arrowstyle="-|>", color=COLORS["robust"], lw=2.0, mutation_scale=14), zorder=7)
ax.annotate("", xy=(frr_r[0], farb_r[0]), xytext=(frr_y[0], farb_y[0]),
            arrowprops=dict(arrowstyle="-|>", color="#888888", lw=1.4, linestyle="--", mutation_scale=12), zorder=7)

labels = [
    (frr_y[0], farb_y[0], f"Baseline L=1: FAR$_B$ {label(farb_y[0])}, FRR {label(frr_y[0])}", COLORS["youden"]),
    (frr_y[2], farb_y[2], f"Baseline L=5: FAR$_B$ {label(farb_y[2])}, FRR {label(frr_y[2])}", COLORS["youden"]),
    (frr_r[0], farb_r[0], f"Strict L=1: FAR$_B$ {label(farb_r[0])}, FRR {label(frr_r[0])}", COLORS["robust"]),
    (frr_r[2], farb_r[2], f"Strict L=5: FAR$_B$ {label(farb_r[2])}, FRR {label(frr_r[2])}", COLORS["robust"]),
]
# Candidate label anchors are inside the plotting area. Choose from anchors
# whose rendered bboxes contain neither any mean/arrow endpoint nor one another.
ax.set_xlim(0, 40)
ax.set_ylim(0, 26)
ax.set_xlabel("False rejection of legitimate meters, FRR (%)\n→ worse availability", fontsize=10)
ax.set_ylabel("True-stranger penetration, FAR$_B$ (%)\n→ worse security", fontsize=10)
ax.set_title("(a) Mean operating points across threshold and burst length", fontsize=11, fontweight="bold")
ax.grid(alpha=0.22)
ax.text(0.98, 0.78, f"Ep 4 (FRR {label(outlier_frr)}, FAR$_B$ {label(outlier_farb)}) off-scale",
        transform=ax.transAxes, ha="right", va="top", fontsize=7.5, color="#555555")
from matplotlib.lines import Line2D
from matplotlib.legend_handler import HandlerTuple
baseline_episode_handle = Line2D([], [], marker="o", linestyle="none", markersize=6,
                                 markerfacecolor=COLORS["youden"], markeredgecolor="white")
strict_episode_handle = Line2D([], [], marker="o", linestyle="none", markersize=6,
                               markerfacecolor=COLORS["robust"], markeredgecolor="white")
mean_handles = (
    Line2D([], [], marker="o", linestyle="none", markersize=7,
           markerfacecolor="#555555", markeredgecolor="white"),
    Line2D([], [], marker="D", linestyle="none", markersize=7,
           markerfacecolor="#555555", markeredgecolor="white"),
)
ax.legend(handles=[
    baseline_episode_handle, strict_episode_handle, mean_handles,
], labels=["Baseline episodes, L=1", "Strict episodes, L=1", "Mean; circle L=1, diamond L=5"],
   handler_map={tuple: HandlerTuple(ndivide=None)}, loc="upper right", fontsize=7, framealpha=0.92)
fig.canvas.draw()
renderer = fig.canvas.get_renderer()
candidate_positions = [
    [(11, 18), (13, 20), (9, 18)],
    [(0.8, 7), (1.0, 5), (2, 7)],
    [(16, 1), (20, 1), (16, 2.5)],
    [(19, 13), (24, 14), (15, 13)],
]
label_artists = []
occupied = []
mean_endpoints = [(x, y) for x, y, _, _ in points]
arrow_segments = [((frr_y[0], farb_y[0]), (frr_y[2], farb_y[2])),
                  ((frr_r[0], farb_r[0]), (frr_r[2], farb_r[2])),
                  ((frr_y[0], farb_y[0]), (frr_r[0], farb_r[0]))]

def segment_intersects_bbox(p0, p1, bbox):
    """Liang-Barsky line/rectangle intersection in display coordinates."""
    x0, y0 = p0
    x1, y1 = p1
    dx, dy = x1 - x0, y1 - y0
    t0, t1 = 0.0, 1.0
    for p, q in ((-dx, x0-bbox.x0), (dx, bbox.x1-x0), (-dy, y0-bbox.y0), (dy, bbox.y1-y0)):
        if p == 0:
            if q < 0:
                return False
        else:
            t = q / p
            if p < 0:
                t0 = max(t0, t)
            else:
                t1 = min(t1, t)
            if t0 > t1:
                return False
    return True

endpoint_pixels = [ax.transData.transform(point) for point in mean_endpoints]
arrow_pixels = [(ax.transData.transform(p0), ax.transData.transform(p1)) for p0, p1 in arrow_segments]
for label_index, (x, y, text, color) in enumerate(labels):
    placed = None
    # Search nearest anchors first, while keeping every label inside the axes.
    candidates_near = candidate_positions[label_index]
    for lx, ly in candidates_near:
        ann = ax.annotate(text, xy=(x, y), xytext=(lx, ly), textcoords="data",
                          fontsize=8.0, color=color, fontweight="bold",
                          arrowprops=dict(arrowstyle="-", color=color, lw=0.8),
                          bbox=dict(boxstyle="round,pad=0.25", fc="white", ec="#cccccc", alpha=0.96),
                          zorder=10)
        fig.canvas.draw()
        # Inspect the actual text box only; Annotation.get_window_extent also
        # includes its leader line and would falsely include the target marker.
        bb = ann.get_bbox_patch().get_window_extent(fig.canvas.get_renderer()).expanded(1.02, 1.05)
        gap_px = 4.0 * fig.dpi / 72.0
        bb_pad = matplotlib.transforms.Bbox.from_extents(bb.x0-gap_px, bb.y0-gap_px, bb.x1+gap_px, bb.y1+gap_px)
        contains_mean = any(bb_pad.contains(px, py) for px, py in endpoint_pixels)
        hits_arrow = any(segment_intersects_bbox(p0, p1, bb_pad) for p0, p1 in arrow_pixels)
        overlaps = any(bb_pad.overlaps(ob) for ob in occupied)
        clear = not contains_mean and not hits_arrow and not overlaps
        if clear:
            placed = ann
            occupied.append(bb_pad)
            break
        ann.remove()
    if placed is None:
        raise RuntimeError(f"Could not place panel (a) label {label_index + 1} ({text}) without covering a mean/arrow or overlapping another label")
    label_artists.append(placed)
fig.canvas.draw()
renderer = fig.canvas.get_renderer()
for i, artist in enumerate(label_artists):
    bb = artist.get_bbox_patch().get_window_extent(renderer)
    stop_if(bb.x0 < ax.bbox.x0 or bb.x1 > ax.bbox.x1 or bb.y0 < ax.bbox.y0 or bb.y1 > ax.bbox.y1,
            f"panel (a) label {i+1} falls outside axes")
    for other in label_artists[i+1:]:
        b2 = other.get_bbox_patch().get_window_extent(renderer)
        gap_px = 4.0 * fig.dpi / 72.0
        collision = bb.x0 < b2.x1 + gap_px and bb.x1 > b2.x0 - gap_px and bb.y0 < b2.y1 + gap_px and bb.y1 > b2.y0 - gap_px
        stop_if(collision, f"panel (a) text labels {i+1} overlap with less than 4 pt separation")
    expanded = matplotlib.transforms.Bbox.from_extents(bb.x0-gap_px, bb.y0-gap_px, bb.x1+gap_px, bb.y1+gap_px)
    stop_if(any(expanded.contains(px, py) for px, py in endpoint_pixels), f"panel (a) label {i+1} contains a mean-marker/arrow endpoint")
    stop_if(any(segment_intersects_bbox(p0, p1, expanded) for p0, p1 in arrow_pixels), f"panel (a) label {i+1} covers an arrow segment")

# Replot means last so all four markers sit above dots, arrows and label leaders.
for x, y, color, marker in points:
    ax.scatter(x, y, s=120, color=color, marker=marker, edgecolor="white", linewidth=1.2, zorder=14)
ax.text((frr_y[0] + frr_r[0]) / 2, (farb_y[0] + farb_r[0]) / 2 + 2.0,
        "stricter threshold", color="#777777", fontsize=7.5, ha="center", va="bottom",
        bbox=dict(fc="white", ec="none", alpha=0.75, pad=1), zorder=9)
print("Panel (a) bbox check: PASS (no label contains a mean/arrow endpoint; no pair overlaps; no label covers an arrow).")

# Panel (b): mean rates, +/- 1 SE bands, labels to the right of each marker.
for values, errors, color, marker, ls, name in [
    (farb_y, se_farb_y, COLORS["youden"], "s", "-", r"Baseline FAR$_B$ ($\tau_{\mathrm{Youden}}$)"),
    (frr_y, se_frr_y, COLORS["youden"], "o", "--", r"Baseline FRR ($\tau_{\mathrm{Youden}}$)"),
    (farb_r, se_farb_r, COLORS["robust"], "s", "-", r"Strict FAR$_B$ ($\tau_{\mathrm{robust}}$)"),
    (frr_r, se_frr_r, COLORS["robust"], "o", "--", r"Strict FRR ($\tau_{\mathrm{robust}}$)"),
]:
    ax2.errorbar(LS, values, yerr=errors, fmt=marker, linestyle=ls, color=color,
                 linewidth=2.0, markersize=6.5, capsize=3.5, capthick=1.0, label=name, zorder=4)
    ax2.fill_between(LS, values-errors, values+errors, color=color, alpha=0.10, zorder=1)

vbox = dict(boxstyle="square,pad=0.12", fc="white", ec="none", alpha=0.92)
for i, L in enumerate(LS):
    for value, color in ((farb_y[i], COLORS["youden"]), (frr_y[i], COLORS["youden"]),
                         (farb_r[i], COLORS["robust"]), (frr_r[i], COLORS["robust"])):
        ax2.annotate(label(value), (L, value), xytext=(7, 0), textcoords="offset points",
                     ha="left", va="center", color=color, fontsize=8.2, fontweight="bold",
                     bbox=vbox, zorder=8)

# Compute change from rounded, data-derived endpoint labels so the stated pp
# change agrees with those displayed endpoints (30.1 -> 18.1 is -12.0 pp).
frr_drop = one_decimal(frr_r[0]) - one_decimal(frr_r[2])
farb_rise = one_decimal(farb_r[2]) - one_decimal(farb_r[0])
summary = (f"Strict threshold ($\\tau_{{\\mathrm{{robust}}}}$), L=1 → 5: FRR {label(frr_r[0])} → {label(frr_r[2])} (-{frr_drop:.1f} pp);\n"
           f"FAR$_B$ {label(farb_r[0])} → {label(farb_r[2])} (+{farb_rise:.1f} pp)")
ax2.text(0.98, 0.98, summary, transform=ax2.transAxes, ha="right", va="top", fontsize=8.3,
         color=COLORS["robust"], bbox=dict(boxstyle="round,pad=0.35", fc="white", ec=COLORS["robust"], alpha=0.96), zorder=9)
ax2.set_title("(b) Burst fusion lowers FRR; FAR$_B$ rises modestly at strict threshold",
              fontsize=9.8, fontweight="bold")
ax2.set_xlabel("Burst length L (consecutive packets fused)", fontsize=10)
ax2.set_ylabel("Error rate (%)", fontsize=10)
ax2.set_xticks(LS)
ax2.set_xlim(0.65, 5.9)
ax2.set_ylim(0, 38)
ax2.grid(alpha=0.22)
ax2.legend(loc="upper center", bbox_to_anchor=(0.5, -0.17), ncol=2, fontsize=7.6,
           framealpha=0.95, edgecolor="#cccccc")

# Build caption entirely from the checked data values.
caption = (
    f"Fig. 2. Joint evaluation of threshold strictness and burst length $L \\in \\{{1,3,5\\}}$ across 20 evaluation episodes. "
    f"The source dataset contains $N={N//1000}{{,}}{N%1000:03d}$ raw packet transmissions across {len(device_counts)} devices ({min(device_counts)}--{max(device_counts)} packets per device); $N$ is the dataset total, not the cumulative episode evaluation count. "
    f"(a) Mean operating points; the strict threshold $\\tau_{{\\text{{robust}}}}$ lowers $\\text{{FAR}}_B$ from {label(farb_y[0])} to {label(farb_r[0])} at the cost of raising $\\text{{FRR}}$ from {label(frr_y[0])} to {label(frr_r[0])}. "
    f"Fusing $L=5$ packets moves both operating points toward lower $\\text{{FRR}}$: $\\text{{FRR}}$ {label(frr_y[0])} $\\rightarrow$ {label(frr_y[2])} at $\\tau_{{\\text{{Youden}}}}$ ($\\text{{FAR}}_B$ {label(farb_y[0])} $\\rightarrow$ {label(farb_y[2])}) and {label(frr_r[0])} $\\rightarrow$ {label(frr_r[2])} at $\\tau_{{\\text{{robust}}}}$ ($\\text{{FAR}}_B$ {label(farb_r[0])} $\\rightarrow$ {label(farb_r[2])}). "
    f"(b) $\\text{{FAR}}_B$ (solid) and $\\text{{FRR}}$ (dashed) versus $L$. Bands show $\\pm 1$ standard error over 20 episodes. Fusion was evaluated at both thresholds on the same episodes and seeds. "
    f"Three episodes lie outside panel (a)'s x-range, including Ep 4 ($\\text{{FRR}}$ {label(outlier_frr)}, $\\text{{FAR}}_B$ {label(outlier_farb)})."
)

OUT_DIR.mkdir(parents=True, exist_ok=True)
out_png = OUT_DIR / "gap3_fig2_final.png"
out_pdf = OUT_DIR / "gap3_fig2_final.pdf"
caption_path = OUT_DIR / "caption.txt"
fig.savefig(out_png, dpi=300, bbox_inches="tight")
fig.savefig(out_pdf, bbox_inches="tight")
caption_path.write_text(caption + "\n", encoding="utf-8")
plt.close(fig)

print(f"\nGenerated: {out_png} (300 dpi)")
print(f"Generated: {out_pdf}")
print(f"Generated: {caption_path}")
print("Figure label mismatch list: none")
