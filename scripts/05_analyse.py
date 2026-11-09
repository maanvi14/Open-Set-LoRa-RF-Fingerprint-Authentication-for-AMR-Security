#!/usr/bin/env python
"""
scripts/05_analyse.py
Phase 8 + 8B — Statistics, LOPO, neighbours, groups.

Usage:
    python scripts/05_analyse.py [--smoke]
"""
import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.config import CFG
from src.groups import run_group_analysis
from src.lopo import run_lopo_all
from src.neighbours import run_neighbour_analysis
from src.stats import compute_stats, per_device_far_ranking
from src.utils import get_logger

LOG = get_logger("05_analyse")


def main() -> None:
    parser = argparse.ArgumentParser(description="Phase 8 + 8B analysis.")
    parser.add_argument("--smoke", action="store_true",
                        help="Run reduced smoke test (2 episodes).")
    parser.add_argument("--skip-lopo", action="store_true",
                        help="Skip LOPO analysis (slow).")
    args = parser.parse_args()

    n_ep = 2 if args.smoke else None

    LOG.info("=== Phase 8: Statistics ===")
    try:
        df_stats = compute_stats()
        print("\n=== Stats Summary ===")
        print(df_stats.to_string(index=False))
    except FileNotFoundError as e:
        LOG.warning("Stats skipped (run episodes first): %s", e)

    LOG.info("=== Phase 8: Per-device FAR ranking ===")
    try:
        df_rank = per_device_far_ranking(n_episodes=n_ep)
        print(f"\nTop 10 devices by FAR_B:\n{df_rank.head(10).to_string(index=False)}")
    except Exception as e:
        LOG.warning("Per-device ranking skipped: %s", e)

    LOG.info("=== Phase 8B: LOPO ===")
    if not args.skip_lopo:
        try:
            df_bias, df_tradeoff = run_lopo_all(n_episodes=n_ep, smoke=args.smoke)
            print(f"\nLOPO bias:\n{df_bias.groupby('estimator')[['bias','abs_error']].mean().to_string()}")
        except FileNotFoundError as e:
            LOG.warning("LOPO skipped (run episodes first): %s", e)
    else:
        LOG.info("LOPO skipped (--skip-lopo).")

    LOG.info("=== Phase 8: Neighbour analysis ===")
    try:
        df_nb = run_neighbour_analysis(n_episodes=n_ep)
        if len(df_nb) > 0:
            rho = df_nb["spearman_rho"].iloc[0]
            print(f"\nSpearman rho(distance, FAR_B) = {rho:.4f}")
    except Exception as e:
        LOG.warning("Neighbour analysis skipped: %s", e)

    LOG.info("=== Phase 8: Group analysis ===")
    try:
        df_grp = run_group_analysis(n_episodes=n_ep)
        if len(df_grp) > 0:
            print(f"\nGroup analysis:\n{df_grp.groupby('shares_group_with_enrolled')['FAR_B'].mean()}")
        else:
            LOG.info("No group information available.")
    except Exception as e:
        LOG.warning("Group analysis skipped: %s", e)

    LOG.info("Phase 8 + 8B analysis complete.")


if __name__ == "__main__":
    main()
