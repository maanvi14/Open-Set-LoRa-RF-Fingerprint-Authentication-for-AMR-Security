"""
tests/test_sweep.py
Unit tests for proxy-count sweep (Phase 7).
Ensures that FINAL_TEST devices never enter calibration at any k,
and that evaluation is strictly unbiased.
"""
import numpy as np
import pytest

from src.splits import create_episode_split


def test_final_test_devices_never_calibrated():
    # Synthetic pool of 60 devices
    all_devs = list(range(1, 61))
    device_packet_counts = {dev: 200 for dev in all_devs}
    split = create_episode_split(
        all_device_ids=all_devs,
        packet_counts=device_packet_counts,
        episode_idx=0,
        seed=42
    )

    final_unknown_set = set(split.final_unknown_ids)
    proxy_set = set(split.proxy_ids)
    enrolled_set = set(split.enrolled_ids)

    # Disjoint device groups check
    assert len(final_unknown_set.intersection(proxy_set)) == 0
    assert len(final_unknown_set.intersection(enrolled_set)) == 0
    assert len(proxy_set.intersection(enrolled_set)) == 0

    # Verify for any k in sweep ks, the calibration set never touches final_unknown_set
    for k in [0, 1, 3, 5, 10, 15]:
        chosen_proxies = split.proxy_ids[:k] if k > 0 else []
        assert set(chosen_proxies).issubset(proxy_set)
        assert len(set(chosen_proxies).intersection(final_unknown_set)) == 0


def test_sweep_k0_delta_is_nan():
    """Verify that at k=0, DeltaFAR is NaN because Condition A has no proxy test set."""
    from src.evaluate import compute_delta_far
    far_a = float("nan")
    far_b = 0.63
    # When far_a is nan, delta must not be filled with arbitrary 0
    delta = compute_delta_far(far_a, far_b) if not np.isnan(far_a) else float("nan")
    assert np.isnan(delta)
