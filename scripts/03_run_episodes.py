#!/usr/bin/env python
"""
scripts/03_run_episodes.py
Phase 4–6 — Multi-episode evaluation.

Usage:
    python scripts/03_run_episodes.py [--smoke]

The --smoke flag runs 2 episodes with 3 devices per group for quick testing.
"""
import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.config import CFG
from src.episodes import run_all_episodes
from src.utils import get_logger

LOG = get_logger("03_run_episodes")


def main() -> None:
    parser = argparse.ArgumentParser(description="Run multi-episode evaluation.")
    parser.add_argument("--smoke", action="store_true",
                        help="Run reduced smoke test (2 episodes, 3 devices/group).")
    parser.add_argument("--n-episodes", type=int, default=None,
                        help=f"Number of episodes (default: {CFG.n_episodes}).")
    parser.add_argument("--save-models", action="store_true",
                        help="Save fitted models to results/models/.")
    args = parser.parse_args()

    LOG.info("=== Phase 4–6: Multi-episode evaluation ===")
    if args.smoke:
        LOG.info("SMOKE MODE: 2 episodes, 3 devices/group")

    df_summary = run_all_episodes(
        n_episodes=args.n_episodes,
        smoke=args.smoke,
        save_models=args.save_models,
    )

    print("\n=== Episode Summary ===")
    print(df_summary.to_string(index=False))
    print(f"\nFull results: {CFG.path_results / 'tables' / 'episode_summary.csv'}")


if __name__ == "__main__":
    main()
