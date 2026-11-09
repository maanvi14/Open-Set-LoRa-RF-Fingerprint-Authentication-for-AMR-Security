"""
src/threshold.py
Frozen threshold calibration using Youden's J statistic.

Threshold is calibrated ONCE from (known_val, proxy_cal) and then immutable.
Any attempt to modify the threshold after creation raises an AttributeError.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, Optional

import numpy as np


# ---------------------------------------------------------------------------
# FrozenThreshold immutable dataclass
# ---------------------------------------------------------------------------

@dataclass
class FrozenThreshold:
    """
    Immutable threshold container.

    Attributes
    ----------
    tau           : calibrated decision threshold
    method        : 'youden' or 'known_acceptance'
    calibration_stats : dict with diagnostic info
    """
    tau: float
    method: str
    calibration_stats: Dict[str, Any]

    def accept(self, score: float) -> bool:
        """Return True if score >= tau (device is accepted as enrolled)."""
        return score >= self.tau

    def accept_array(self, scores: np.ndarray) -> np.ndarray:
        """Boolean array: True where scores >= tau."""
        return scores >= self.tau

    def __setattr__(self, name: str, value: Any) -> None:
        if hasattr(self, name):
            raise AttributeError(
                f"FrozenThreshold is immutable. Cannot set '{name}'. "
                "The threshold is frozen after calibration and must never be changed using test data."
            )
        super().__setattr__(name, value)

    def __delattr__(self, name: str) -> None:
        raise AttributeError("FrozenThreshold is immutable.")


# ---------------------------------------------------------------------------
# Calibration functions
# ---------------------------------------------------------------------------

def _youden_j(
    scores_known: np.ndarray,
    scores_unknown: np.ndarray,
    n_candidates: int = 1000,
) -> tuple[float, dict]:
    """
    Find tau* = argmax_tau (TPR(tau) + TNR(tau) - 1)  =  Youden's J.

    known   → positives (enrolled)
    unknown → negatives (proxy_cal strangers)
    """
    all_scores = np.concatenate([scores_known, scores_unknown])
    candidates = np.linspace(all_scores.min(), all_scores.max(), n_candidates)

    best_j = -np.inf
    best_tau = float(candidates[0])

    j_values = []
    for tau in candidates:
        tpr = float(np.mean(scores_known >= tau))     # sensitivity
        tnr = float(np.mean(scores_unknown < tau))    # specificity
        j = tpr + tnr - 1.0
        j_values.append(j)
        if j > best_j:
            best_j = j
            best_tau = float(tau)

    j_arr = np.array(j_values)
    stats = {
        "youden_j": float(best_j),
        "n_candidates": n_candidates,
        "tpr_at_tau": float(np.mean(scores_known >= best_tau)),
        "tnr_at_tau": float(np.mean(scores_unknown < best_tau)),
        "n_known": int(len(scores_known)),
        "n_unknown": int(len(scores_unknown)),
        "score_range": [float(all_scores.min()), float(all_scores.max())],
    }
    return best_tau, stats


def _known_acceptance_tau(
    scores_known: np.ndarray,
    target_acceptance: float = 0.95,
) -> tuple[float, dict]:
    """
    Find smallest tau such that fraction of known scores >= tau equals target_acceptance.
    (i.e., the target_acceptance-th quantile from BELOW — we want 95% acceptance.)
    """
    # tau = (1 - target_acceptance)-th quantile of scores_known
    # so that P(score >= tau) = target_acceptance
    q = 1.0 - target_acceptance
    tau = float(np.quantile(scores_known, q))
    actual_acceptance = float(np.mean(scores_known >= tau))
    stats = {
        "target_acceptance": target_acceptance,
        "actual_acceptance": actual_acceptance,
        "n_known": int(len(scores_known)),
    }
    return tau, stats


# ---------------------------------------------------------------------------
# Public calibration entry point
# ---------------------------------------------------------------------------

def calibrate_threshold(
    scores_known_val: np.ndarray,
    scores_proxy_cal: np.ndarray,
    method: str = "youden",
    target_acceptance: Optional[float] = None,
) -> FrozenThreshold:
    """
    Calibrate and return a FrozenThreshold.

    Parameters
    ----------
    scores_known_val : scores for enrolled cal_val packets (positive class)
    scores_proxy_cal : scores for proxy_cal packets (negative class)
    method           : 'youden' or 'known_acceptance'
    target_acceptance: used only when method='known_acceptance'

    Returns
    -------
    FrozenThreshold (immutable)

    Notes
    -----
    The threshold is FROZEN at creation. This function may only be called
    with calibration data (never with test data).
    """
    if len(scores_known_val) == 0:
        raise ValueError("scores_known_val is empty — cannot calibrate threshold.")
    if method == "youden":
        if len(scores_proxy_cal) == 0:
            raise ValueError(
                "scores_proxy_cal is empty — cannot use Youden's J without negative examples. "
                "Use method='known_acceptance' for k=0 proxy case."
            )
        tau, stats = _youden_j(scores_known_val, scores_proxy_cal)
    elif method == "known_acceptance":
        ta = target_acceptance if target_acceptance is not None else 0.95
        tau, stats = _known_acceptance_tau(scores_known_val, ta)
    else:
        raise ValueError(f"Unknown calibration method: {method!r}. Use 'youden' or 'known_acceptance'.")

    # Also compute the alternative tau for reference (store in stats, do NOT use it)
    if method == "youden" and len(scores_known_val) > 0:
        alt_tau, alt_stats = _known_acceptance_tau(scores_known_val, 0.95)
        stats["alt_tau_known_acceptance_0.95"] = alt_tau
        stats["alt_actual_acceptance"] = alt_stats["actual_acceptance"]

    return FrozenThreshold(tau=tau, method=method, calibration_stats=stats)


if __name__ == "__main__":
    import logging
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    rng = np.random.default_rng(0)
    s_known   = rng.uniform(0.6, 1.0, 300)
    s_unknown = rng.uniform(0.0, 0.5, 200)

    ft = calibrate_threshold(s_known, s_unknown, method="youden")
    logger.info("Youden tau=%.4f  method=%s", ft.tau, ft.method)
    logger.info("Stats: %s", ft.calibration_stats)

    # Try to modify (must raise)
    try:
        ft.tau = 0.99  # type: ignore[misc]
        logger.error("ERROR: should have raised AttributeError")
    except AttributeError as e:
        logger.info("Correctly blocked modification: %s", e)

    ft2 = calibrate_threshold(s_known, s_unknown, method="known_acceptance", target_acceptance=0.95)
    logger.info("KA tau=%.4f  actual_acceptance=%.4f",
                ft2.tau, ft2.calibration_stats["actual_acceptance"])

    logger.info("threshold.py self-test PASSED.")
