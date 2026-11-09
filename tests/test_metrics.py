"""
tests/test_metrics.py
Unit tests for evaluation metrics (FAR, FRR, AUROC, macro-F1, DeltaFAR).
"""
import numpy as np
import pytest

from src.evaluate import (
    compute_far,
    compute_frr,
    compute_auroc,
    compute_macro_f1,
    compute_delta_far,
    assert_frr_identical,
    per_device_far
)


def test_far_and_frr_basic():
    # Known positive scores: [0.9, 0.8, 0.7, 0.6]
    # Stranger negative scores: [0.9, 0.4, 0.3, 0.2]
    # Threshold tau = 0.65
    known_scores = np.array([0.9, 0.8, 0.7, 0.6])
    stranger_scores = np.array([0.9, 0.4, 0.3, 0.2])
    tau = 0.65

    # Known rejected: only 0.6 < 0.65 -> 1 out of 4 rejected -> FRR = 0.25
    frr = compute_frr(known_scores, tau)
    assert np.isclose(frr, 0.25)

    # Stranger accepted: only 0.9 >= 0.65 -> 1 out of 4 accepted -> FAR = 0.25
    far = compute_far(stranger_scores, tau)
    assert np.isclose(far, 0.25)


def test_delta_far():
    far_a = 0.10
    far_b = 0.35
    delta = compute_delta_far(far_a, far_b)
    assert np.isclose(delta, 0.25)


def test_assert_frr_identical():
    assert_frr_identical(0.1234567, 0.1234567)
    with pytest.raises(AssertionError):
        assert_frr_identical(0.12, 0.15)


def test_per_device_far():
    scores_dict = {
        "dev_1": np.array([0.9, 0.8, 0.1]),  # 2 accepted at tau=0.5 -> 2/3
        "dev_2": np.array([0.2, 0.3, 0.4]),  # 0 accepted at tau=0.5 -> 0.0
    }
    res = per_device_far(scores_dict, tau=0.5)
    assert np.isclose(res["dev_1"], 2.0 / 3.0)
    assert np.isclose(res["dev_2"], 0.0)


def test_auroc():
    known = np.array([0.9, 0.8, 0.7, 0.6])
    unknown = np.array([0.1, 0.2, 0.3, 0.4])
    auroc = compute_auroc(known, unknown)
    assert np.isclose(auroc, 1.0)
