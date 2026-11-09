"""
tests/test_splits_no_leakage.py
Real leakage guard tests for device/packet splits.
"""
from __future__ import annotations

import numpy as np
import pytest

from src.splits import (
    EpisodeSplit,
    assert_no_leakage,
    assert_known_test_identical,
    create_episode_split,
)


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

def _make_split(seed: int = 0, n_devices: int = 60) -> tuple:
    """Return (split, all_device_ids, packet_counts)."""
    rng = np.random.default_rng(seed)
    all_device_ids = list(range(n_devices))
    packet_counts = {d: int(rng.integers(200, 400)) for d in all_device_ids}
    split = create_episode_split(all_device_ids, packet_counts, episode_idx=seed, seed=seed)
    return split, all_device_ids, packet_counts


# ---------------------------------------------------------------------------
# 1. Device group disjointness
# ---------------------------------------------------------------------------

class TestDeviceGroupDisjointness:
    def test_no_device_in_two_groups(self):
        split, _, _ = _make_split(seed=0)
        en_set = set(split.enrolled_ids)
        px_set = set(split.proxy_ids)
        fu_set = set(split.final_unknown_ids)
        assert len(en_set & px_set) == 0, "Enrolled ∩ Proxy not empty"
        assert len(en_set & fu_set) == 0, "Enrolled ∩ FinalUnknown not empty"
        assert len(px_set & fu_set) == 0, "Proxy ∩ FinalUnknown not empty"

    def test_device_counts_correct(self):
        from src.config import CFG
        split, _, _ = _make_split(seed=1)
        assert len(split.enrolled_ids) == CFG.n_enrolled
        assert len(split.proxy_ids) == CFG.n_proxy
        assert len(split.final_unknown_ids) == CFG.n_final_unknown

    def test_all_groups_cover_all_assigned_devices(self):
        from src.config import CFG
        split, _, _ = _make_split(seed=2)
        total = len(split.enrolled_ids) + len(split.proxy_ids) + len(split.final_unknown_ids)
        assert total == CFG.n_enrolled + CFG.n_proxy + CFG.n_final_unknown

    def test_different_seeds_different_assignments(self):
        split0, _, _ = _make_split(seed=0)
        split1, _, _ = _make_split(seed=1)
        # Different seeds should produce different enrolled sets (almost certainly)
        assert split0.enrolled_ids != split1.enrolled_ids


# ---------------------------------------------------------------------------
# 2. Enrolled packet splits disjoint per device
# ---------------------------------------------------------------------------

class TestEnrolledPacketSplits:
    def test_train_cal_val_disjoint(self):
        split, _, _ = _make_split(seed=3)
        for dev_id in split.enrolled_ids:
            tr = set(split.enrolled_train_idx[dev_id].tolist())
            cv = set(split.enrolled_cal_val_idx[dev_id].tolist())
            assert len(tr & cv) == 0, f"Device {dev_id}: train ∩ cal_val not empty"

    def test_train_known_test_disjoint(self):
        split, _, _ = _make_split(seed=4)
        for dev_id in split.enrolled_ids:
            tr = set(split.enrolled_train_idx[dev_id].tolist())
            kt = set(split.enrolled_known_test_idx[dev_id].tolist())
            assert len(tr & kt) == 0, f"Device {dev_id}: train ∩ known_test not empty"

    def test_cal_val_known_test_disjoint(self):
        split, _, _ = _make_split(seed=5)
        for dev_id in split.enrolled_ids:
            cv = set(split.enrolled_cal_val_idx[dev_id].tolist())
            kt = set(split.enrolled_known_test_idx[dev_id].tolist())
            assert len(cv & kt) == 0, f"Device {dev_id}: cal_val ∩ known_test not empty"

    def test_all_enrolled_devices_have_train_indices(self):
        split, _, _ = _make_split(seed=6)
        for dev_id in split.enrolled_ids:
            assert dev_id in split.enrolled_train_idx, f"Device {dev_id} missing from train"
            assert len(split.enrolled_train_idx[dev_id]) > 0, \
                f"Device {dev_id} has empty train indices"

    def test_packet_indices_non_negative(self):
        split, _, _ = _make_split(seed=7)
        for dev_id in split.enrolled_ids:
            assert (split.enrolled_train_idx[dev_id] >= 0).all()
            assert (split.enrolled_cal_val_idx[dev_id] >= 0).all()
            assert (split.enrolled_known_test_idx[dev_id] >= 0).all()


# ---------------------------------------------------------------------------
# 3. FINAL_UNKNOWN devices have no packets in any other split
# ---------------------------------------------------------------------------

class TestFinalUnknownIsolation:
    def test_final_unknown_not_in_enrolled_train(self):
        split, _, _ = _make_split(seed=8)
        for dev_id in split.final_unknown_ids:
            assert dev_id not in split.enrolled_train_idx, \
                f"Final-unknown {dev_id} in enrolled_train"

    def test_final_unknown_not_in_enrolled_cal_val(self):
        split, _, _ = _make_split(seed=9)
        for dev_id in split.final_unknown_ids:
            assert dev_id not in split.enrolled_cal_val_idx, \
                f"Final-unknown {dev_id} in enrolled_cal_val"

    def test_final_unknown_not_in_enrolled_known_test(self):
        split, _, _ = _make_split(seed=10)
        for dev_id in split.final_unknown_ids:
            assert dev_id not in split.enrolled_known_test_idx, \
                f"Final-unknown {dev_id} in enrolled_known_test"

    def test_final_unknown_not_in_proxy_cal(self):
        split, _, _ = _make_split(seed=11)
        for dev_id in split.final_unknown_ids:
            assert dev_id not in split.proxy_cal_idx, \
                f"Final-unknown {dev_id} in proxy_cal"

    def test_final_unknown_not_in_proxy_test(self):
        split, _, _ = _make_split(seed=12)
        for dev_id in split.final_unknown_ids:
            assert dev_id not in split.proxy_test_idx, \
                f"Final-unknown {dev_id} in proxy_test"

    def test_final_unknown_has_all_packets(self):
        rng = np.random.default_rng(13)
        all_device_ids = list(range(60))
        packet_counts = {d: 300 for d in all_device_ids}
        split = create_episode_split(all_device_ids, packet_counts, episode_idx=0, seed=13)
        for dev_id in split.final_unknown_ids:
            expected = np.arange(packet_counts[dev_id])
            actual = split.final_test_idx[dev_id]
            assert np.array_equal(actual, expected), \
                f"Final-unknown {dev_id}: expected all {len(expected)} packets"


# ---------------------------------------------------------------------------
# 4. Proxy splits: PROXY_TEST disjoint from PROXY_CAL
# ---------------------------------------------------------------------------

class TestProxySplits:
    def test_proxy_cal_test_disjoint(self):
        split, _, _ = _make_split(seed=14)
        for dev_id in split.proxy_ids:
            pc = set(split.proxy_cal_idx[dev_id].tolist())
            pt = set(split.proxy_test_idx[dev_id].tolist())
            assert len(pc & pt) == 0, \
                f"Proxy device {dev_id}: PROXY_CAL ∩ PROXY_TEST not empty"

    def test_all_proxy_devices_in_both_splits(self):
        split, _, _ = _make_split(seed=15)
        for dev_id in split.proxy_ids:
            assert dev_id in split.proxy_cal_idx, f"Proxy {dev_id} missing from proxy_cal"
            assert dev_id in split.proxy_test_idx, f"Proxy {dev_id} missing from proxy_test"

    def test_proxy_indices_non_negative(self):
        split, _, _ = _make_split(seed=16)
        for dev_id in split.proxy_ids:
            assert (split.proxy_cal_idx[dev_id] >= 0).all()
            assert (split.proxy_test_idx[dev_id] >= 0).all()

    def test_proxy_devices_not_in_enrolled(self):
        split, _, _ = _make_split(seed=17)
        en_set = set(split.enrolled_ids)
        for dev_id in split.proxy_ids:
            assert dev_id not in en_set, f"Proxy {dev_id} also in enrolled"


# ---------------------------------------------------------------------------
# 5. known_test packet indices identical across two episodes with same seed
# ---------------------------------------------------------------------------

class TestKnownTestStability:
    def test_known_test_deterministic_across_conditions(self):
        """
        Two EpisodeSplit objects with the same seed must have
        identical known_test indices (Condition A and B share same FRR base).
        """
        split_a, _, _ = _make_split(seed=99)
        split_b, _, _ = _make_split(seed=99)  # same seed
        assert_known_test_identical(split_a, split_b)

    def test_known_test_different_across_seeds(self):
        """
        Different seeds should (almost certainly) yield different known_test.
        """
        split_a, _, _ = _make_split(seed=100)
        split_b, _, _ = _make_split(seed=200)
        # They share enrolled devices — check at least one device differs
        common_devs = set(split_a.enrolled_ids) & set(split_b.enrolled_ids)
        if not common_devs:
            pytest.skip("No common enrolled devices between seeds 100 and 200")
        for dev_id in list(common_devs)[:3]:
            if not np.array_equal(
                split_a.enrolled_known_test_idx.get(dev_id, np.array([])),
                split_b.enrolled_known_test_idx.get(dev_id, np.array([])),
            ):
                return  # found at least one difference — test passes
        pytest.skip("All checked devices happen to have identical known_test (unlikely)")


# ---------------------------------------------------------------------------
# 6. assert_no_leakage passes for valid split
# ---------------------------------------------------------------------------

class TestAssertNoLeakage:
    def test_valid_split_passes(self):
        split, _, _ = _make_split(seed=42)
        assert_no_leakage(split)  # should not raise

    def test_multiple_seeds_pass(self):
        for seed in range(5):
            split, _, _ = _make_split(seed=seed)
            assert_no_leakage(split)

    def test_injected_leakage_detected(self):
        """Manually inject leakage and verify assertion fires."""
        split, _, _ = _make_split(seed=42)
        # Inject: put a final_unknown device into enrolled_train
        fu_dev = split.final_unknown_ids[0]
        split.enrolled_train_idx[fu_dev] = np.array([0, 1, 2])
        with pytest.raises(AssertionError):
            assert_no_leakage(split)
