#!/usr/bin/env python
"""
scripts/01_audit.py
Phase 2 — Dataset Audit.

Usage:
    python scripts/01_audit.py

Reads data/raw/, inspects every HDF5 file, writes reports/dataset_audit.md.
STOP after this phase and review the report before proceeding.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.audit import run_audit

if __name__ == "__main__":
    run_audit()
    print("\nAudit complete. Review reports/dataset_audit.md before Phase 3.")

