"""
src/evaluate.py
Pure metric computation functions.

All functions are side-effect-free (no I/O, no state mutation).
"""
from __future__ import annotations

from typing import Dict

import numpy as np
from sklearn.metrics import f1_score, roc_auc_score


def compute_far(scores: np.ndarray, tau: float) -> float:
    """
    False Acceptance Rate: fraction of UNKNOWN packets accepted (score >= tau).

    Parameters
    ----------
    scores : np.ndarray  shape (N,)  scores for unknown packets
    tau    : float        decision threshold

    Returns
    -------
    FAR in [0, 1]
    """
    if len(scores) == 0:
        return float("nan")
    return float(np.mean(scores >= tau))


def compute_frr(scores: np.ndarray, tau: float) -> float:
    """
    False Rejection Rate: fraction of KNOWN packets rejected (score < tau).

    Parameters
    ----------
    scores : np.ndarray  shape (N,)  scores for known/enrolled packets
    tau    : float        decision threshold

    Returns
    -------
    FRR in [0, 1]
    """
    if len(scores) == 0:
        return float("nan")
    return float(np.mean(scores < tau))


def compute_auroc(
    scores_known: np.ndarray,
    scores_unknown: np.ndarray,
) -> float:
    """
    AUROC treating known as positive class and unknown as negative.

    Parameters
    ----------
    scores_known   : scores for genuinely enrolled packets
    scores_unknown : scores for stranger packets

    Returns
    -------
    AUROC in [0, 1]
    """
    if len(scores_known) == 0 or len(scores_unknown) == 0:
        return float("nan")
    y_true = np.concatenate([
        np.ones(len(scores_known), dtype=np.int32),
        np.zeros(len(scores_unknown), dtype=np.int32),
    ])
    y_score = np.concatenate([scores_known, scores_unknown])
    return float(roc_auc_score(y_true, y_score))


def compute_macro_f1(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """
    Macro-averaged F1 for closed-set classification.

    Parameters
    ----------
    y_true : ground-truth integer labels
    y_pred : predicted integer labels

    Returns
    -------
    macro-F1 in [0, 1]
    """
    return float(f1_score(y_true, y_pred, average="macro", zero_division=0))


def compute_delta_far(far_a: float, far_b: float) -> float:
    """
    DeltaFAR = FAR_B − FAR_A.

    Positive means FINAL_TEST is harder to reject than PROXY_TEST.
    """
    return far_b - far_a


def assert_frr_identical(frr_a: float, frr_b: float, tol: float = 1e-10) -> None:
    """
    Assert FRR_A == FRR_B within tolerance.

    Raises AssertionError if the values differ.
    FRR must be identical in conditions A and B because they share the same
    enrolled known_test packets and the same frozen threshold.
    """
    if np.isnan(frr_a) or np.isnan(frr_b):
        raise AssertionError(f"FRR values contain NaN: frr_a={frr_a}, frr_b={frr_b}")
    diff = abs(frr_a - frr_b)
    if diff > tol:
        raise AssertionError(
            f"FRR mismatch: frr_a={frr_a:.12f}, frr_b={frr_b:.12f}, diff={diff:.2e} > tol={tol}"
        )


def per_device_far(
    scores_dict: Dict[str, np.ndarray],
    tau: float,
) -> Dict[str, float]:
    """
    Compute FAR per device.

    Parameters
    ----------
    scores_dict : {device_id_str: scores array}
    tau         : frozen threshold

    Returns
    -------
    {device_id_str: FAR}
    """
    return {dev_id: compute_far(scores, tau) for dev_id, scores in scores_dict.items()}


if __name__ == "__main__":
    import logging
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    rng = np.random.default_rng(0)
    scores_known   = rng.uniform(0.5, 1.0, 200)
    scores_unknown = rng.uniform(0.0, 0.6, 200)
    tau = 0.7

    far = compute_far(scores_unknown, tau)
    frr = compute_frr(scores_known, tau)
    auroc = compute_auroc(scores_known, scores_unknown)
    delta = compute_delta_far(far, far + 0.05)

    logger.info("FAR=%.4f  FRR=%.4f  AUROC=%.4f  DeltaFAR=%.4f", far, frr, auroc, delta)

    try:
        assert_frr_identical(0.1, 0.1 + 1e-11)
        logger.info("assert_frr_identical(close) PASSED")
    except AssertionError:
        logger.error("assert_frr_identical(close) FAILED")

    try:
        assert_frr_identical(0.1, 0.2)
        logger.error("assert_frr_identical(far) should have raised")
    except AssertionError:
        logger.info("assert_frr_identical(far) correctly raised")

    logger.info("evaluate.py self-test PASSED.")
