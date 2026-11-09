"""
scripts/make_submission_zip.py
Prepares an Overleaf-ready ZIP submission bundle containing:
- paper/main.tex
- paper/references.bib
- paper/related_work_table.tex
- paper/tables/*.tex
- all 10 vector PDF figures from results/figures/
"""
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAPER = ROOT / "paper"
FIGURES = ROOT / "results" / "figures"
OUTPUT_ZIP = ROOT / "submission_bundle.zip"

def create_bundle():
    print(f"Creating Overleaf submission bundle at: {OUTPUT_ZIP.name}")
    with zipfile.ZipFile(OUTPUT_ZIP, "w", zipfile.ZIP_DEFLATED) as z:
        # Add main paper files
        for f in ["main.tex", "references.bib", "related_work_table.tex", "literature_comparison.csv"]:
            p = PAPER / f
            if p.exists():
                z.write(p, arcname=f)
                print(f"  + Added: {f}")

        # Add LaTeX tables
        tables_dir = PAPER / "tables"
        if tables_dir.exists():
            for t in tables_dir.glob("*.tex"):
                arc = f"tables/{t.name}"
                z.write(t, arcname=arc)
                print(f"  + Added: {arc}")

        # Add PDF figures (both at root and under figures/ for 100% path compatibility)
        if FIGURES.exists():
            for fig in sorted(FIGURES.glob("*.pdf")):
                z.write(fig, arcname=fig.name)
                z.write(fig, arcname=f"figures/{fig.name}")
                print(f"  + Added figure: {fig.name}")

    print(f"\nBundle created successfully! Size: {OUTPUT_ZIP.stat().st_size / 1024:.1f} KB")
    print(f"File path: {OUTPUT_ZIP}")
    print("Upload this ZIP directly to Overleaf (New Project -> Upload Project).")

if __name__ == "__main__":
    create_bundle()
