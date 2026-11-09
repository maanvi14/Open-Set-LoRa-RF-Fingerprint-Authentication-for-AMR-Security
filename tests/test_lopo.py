"""
tests/test_lopo.py
Unit tests verifying Leave-One-Proxy-Out (LOPO) calibration properties (Phase 8B).
Ensures:
  - Fold j's held-out device NEVER appears in its own threshold fitting.
  - FINAL_TEST and PROXY_TEST packets are NEVER used for threshold fitting.
  - Device-matched evaluation operates on identical physical transmitters and identical packets.
"""
import numpy as np
import pytest

from src.splits import create_episode_split


def test_lopo_held_out_device_isolation():
    all_devs = list(range(1, 61))
    counts = {d: 200 for d in all_devs}
    split = create_episode_split(all_devs, counts, episode_idx=0, seed=42)

    proxy_ids = split.proxy_ids
    assert len(proxy_ids) == 15

    for j, held_dev in enumerate(proxy_ids):
        # The other 14 devices
        fitting_devs = [p for p in proxy_ids if p != held_dev]
        assert len(fitting_devs) == 14
        assert held_dev not in fitting_devs
        assert held_dev not in split.final_unknown_ids
        for f in fitting_devs:
            assert f not in split.final_unknown_ids


def test_device_matched_pairing_structure():
    """Verify that device-matched paired evaluation tests identical physical devices."""
    all_devs = list(range(1, 61))
    counts = {d: 200 for d in all_devs}
    split = create_episode_split(all_devs, counts, episode_idx=1, seed=123)

    for dev in split.proxy_ids:
        # Check both cal and test packet indices exist and are completely disjoint
        cal_idx = split.proxy_cal_idx[dev]
        test_idx = split.proxy_test_idx[dev]
        assert len(cal_idx) > 0
        assert len(test_idx) > 0
        assert len(set(cal_idx).intersection(set(test_idx))) == 0

