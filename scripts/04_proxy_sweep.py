#!/usr/bin/env python
"""
scripts/04_proxy_sweep.py
Phase 7 — Proxy-count sweep.

Usage:
    python scripts/04_proxy_sweep.py [--smoke]
"""
import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.config import CFG
from src.sweep import run_sweep
from src.utils import get_logger

LOG = get_logger("04_proxy_sweep")


def main() -> None:
    parser = argparse.ArgumentParser(description="Run proxy-count sweep (Phase 7).")
    parser.add_argument("--smoke", action="store_true",
                        help="Run reduced smoke test (2 episodes, ks=[0,1,3]).")
    parser.add_argument("--n-episodes", type=int, default=None,
                        help=f"Number of episodes (default: {CFG.n_episodes}).")
    parser.add_argument("--ks", type=int, nargs="+", default=None,
                        help="Proxy counts to sweep (default from config).")
    args = parser.parse_args()

    LOG.info("=== Phase 7: Proxy-count sweep ===")
    df = run_sweep(
        n_episodes=args.n_episodes,
        ks=args.ks,
        smoke=args.smoke,
    )
    print("\n=== Sweep Summary (Youden Operating Point) ===")
    print(df.groupby("k")[["FAR_A", "FAR_B", "FRR", "DeltaFAR"]].mean().to_string())
    if "FAR_B_matched_frr" in df.columns:
        print("\n=== Matched-FRR Summary (Controlled Operating Point) ===")
        print(df.groupby("k")[["tau_matched_frr", "FRR_matched", "FAR_B_matched_frr"]].mean().to_string())
    print(f"\nFull results: {CFG.path_results / 'sweep' / 'sweep_results.csv'}")


if __name__ == "__main__":
    main()
