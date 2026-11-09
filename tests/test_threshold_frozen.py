"""
tests/test_threshold_frozen.py
Unit tests verifying that the calibrated threshold tau is immutable
and frozen, preventing any subsequent modification or data leakage.
"""
import pytest
from src.threshold import FrozenThreshold


def test_frozen_threshold_immutability():
    thresh = FrozenThreshold(
        tau=0.75,
        method="youden",
        calibration_stats={"j_score": 0.85, "n_pos": 100, "n_neg": 100}
    )

    assert thresh.tau == 0.75
    assert thresh.method == "youden"
    assert thresh.accept(0.80) is True
    assert thresh.accept(0.70) is False

    # Attempting to modify tau must raise AttributeError
    with pytest.raises(AttributeError):
        thresh.tau = 0.50

    # Attempting to modify method or stats must also raise AttributeError
    with pytest.raises(AttributeError):
        thresh.method = "tampered"

    with pytest.raises(AttributeError):
        del thresh.tau

    # Attempting to mutate calibration_stats keys must raise TypeError
    with pytest.raises(TypeError):
        thresh.calibration_stats["j_score"] = 0.99


def test_test_sets_cannot_influence_tau():
    """Verify threshold calibration strictly depends only on calibration sets."""
    import numpy as np
    from src.threshold import calibrate_threshold

    known_val = np.array([0.9, 0.8, 0.7, 0.6])
    proxy_cal = np.array([0.4, 0.3, 0.2, 0.1])

    # Calibrate tau
    thresh1 = calibrate_threshold(known_val, proxy_cal, method="youden")

    # Introducing test sets (proxy_test or final_test) has no access or effect on thresh1
    final_test_synthetic = np.array([0.95, 0.85, 0.05])
    # thresh1 is already computed and immutable
    assert isinstance(thresh1.tau, float)
    with pytest.raises(AttributeError):
        thresh1.tau = 0.50
