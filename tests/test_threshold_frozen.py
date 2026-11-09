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
