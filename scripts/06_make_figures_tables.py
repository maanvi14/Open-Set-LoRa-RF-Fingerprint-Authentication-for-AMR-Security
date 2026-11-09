#!/usr/bin/env python
"""
scripts/06_make_figures_tables.py
Phase 9 — Figures and LaTeX tables.

Usage:
    python scripts/06_make_figures_tables.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import pandas as pd

from src.config import CFG
from src.plots import generate_all_figures
from src.utils import ensure_dir, get_logger

LOG = get_logger("06_make_figures_tables")


def export_latex_tables() -> None:
    """Export key CSV tables as LaTeX for the paper."""
    ensure_dir(CFG.path_paper / "tables")

    tables = [
        (CFG.path_tables / "episode_summary.csv",         "tab_episode_summary"),
        (CFG.path_tables / "stats_summary.csv",           "tab_stats_summary"),
        (CFG.path_tables / "lopo_bias.csv",               "tab_lopo_bias"),
        (CFG.path_tables / "threshold_tradeoff.csv",      "tab_threshold_tradeoff"),
        (CFG.path_tables / "neighbour_analysis.csv",      "tab_neighbour_analysis"),
        (CFG.path_results / "sweep" / "sweep_results.csv", "tab_sweep_results"),
        (CFG.path_tables / "burst_aggregation_summary.csv", "tab_burst_aggregation"),
    ]

    for csv_path, label in tables:
        if not csv_path.exists():
            LOG.warning("Table not found (skipping): %s", csv_path)
            continue
        df = pd.read_csv(csv_path)
        if label == "tab_burst_aggregation":
            latex = (
                "\\begin{table}[t]\n"
                "\\centering\n"
                "\\caption{Multi-Packet Burst Decision Fusion Performance Across 20 Episodes ($N = 26{,}000$ Transmissions)}\n"
                "\\label{tab:burst_aggregation}\n"
                "\\begin{tabular}{cccccc}\n"
                "\\toprule\n"
                "\\textbf{Burst Length ($L$)} & \\textbf{$\\text{FAR}_A$} & \\textbf{$\\text{FAR}_B$} & \\textbf{FRR} & \\textbf{$\\Delta\\text{FAR}$} & \\textbf{AUROC} \\\\\n"
                "\\midrule\n"
                f"1 (Single packet) & {df.loc[df['burst_length']==1, 'FAR_A'].values[0]*100:.2f}\\% & {df.loc[df['burst_length']==1, 'FAR_B'].values[0]*100:.2f}\\% & {df.loc[df['burst_length']==1, 'FRR'].values[0]*100:.2f}\\% & +{df.loc[df['burst_length']==1, 'DeltaFAR'].values[0]*100:.2f}\\% & {df.loc[df['burst_length']==1, 'AUROC'].values[0]:.4f} \\\\\n"
                f"3 (3-packet burst) & {df.loc[df['burst_length']==3, 'FAR_A'].values[0]*100:.2f}\\% & {df.loc[df['burst_length']==3, 'FAR_B'].values[0]*100:.2f}\\% & {df.loc[df['burst_length']==3, 'FRR'].values[0]*100:.2f}\\% & +{df.loc[df['burst_length']==3, 'DeltaFAR'].values[0]*100:.2f}\\% & {df.loc[df['burst_length']==3, 'AUROC'].values[0]:.4f} \\\\\n"
                f"5 (5-packet burst) & {df.loc[df['burst_length']==5, 'FAR_A'].values[0]*100:.2f}\\% & {df.loc[df['burst_length']==5, 'FAR_B'].values[0]*100:.2f}\\% & {df.loc[df['burst_length']==5, 'FRR'].values[0]*100:.2f}\\% & +{df.loc[df['burst_length']==5, 'DeltaFAR'].values[0]*100:.2f}\\% & {df.loc[df['burst_length']==5, 'AUROC'].values[0]:.4f} \\\\\n"
                "\\bottomrule\n"
                "\\end{tabular}\n"
                "\\end{table}\n"
            )
        else:
            # Round floats for cleaner tables
            df = df.round(4)
            latex = df.to_latex(
                index=False,
                label=label,
                caption=label.replace("tab_", "").replace("_", " ").title(),
            )
        out = CFG.path_paper / "tables" / f"{label}.tex"
        out.write_text(latex, encoding="utf-8")
        LOG.info("LaTeX table saved → %s", out)


def main() -> None:
    LOG.info("=== Phase 9: Figures and Tables ===")

    LOG.info("Generating all figures …")
    generate_all_figures()
    LOG.info("All figures saved to %s", CFG.path_figures)

    LOG.info("Exporting LaTeX tables …")
    export_latex_tables()

    LOG.info("Phase 9 complete.")
    print(f"\nFigures: {CFG.path_figures}")
    print(f"Tables:  {CFG.path_tables}")


if __name__ == "__main__":
    main()
