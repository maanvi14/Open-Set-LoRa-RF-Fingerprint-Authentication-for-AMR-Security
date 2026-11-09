"""
src/model.py
Random Forest open-set identification pipeline.

Pipeline: StandardScaler → RandomForestClassifier(n_estimators=300,
           class_weight='balanced', random_state=seed)

Score = max class probability (confidence that the sample belongs to ANY enrolled class).
"""
from __future__ import annotations

from pathlib import Path
from typing import Dict, List, Optional, Tuple

import joblib
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from src.config import CFG
from src.evaluate import compute_macro_f1
from src.utils import ensure_dir, get_logger

LOG = get_logger(__name__)


# ---------------------------------------------------------------------------
# FrozenThreshold wrapper (references threshold.FrozenThreshold but is model-side)
# ---------------------------------------------------------------------------

class ModelScoreError(RuntimeError):
    """Raised when score computation fails."""


# ---------------------------------------------------------------------------
# Pipeline construction
# ---------------------------------------------------------------------------

def build_pipeline(seed: int) -> Pipeline:
    """Create a fresh (unfitted) sklearn Pipeline."""
    rf = RandomForestClassifier(
        n_estimators=CFG.rf_n_estimators,
        class_weight=CFG.rf_class_weight,
        random_state=seed,
        n_jobs=CFG.rf_n_jobs,
    )
    pipe = Pipeline([
        ("scaler", StandardScaler()),
        ("rf", rf),
    ])
    return pipe


# ---------------------------------------------------------------------------
# Training
# ---------------------------------------------------------------------------

def train_model(
    X_train: np.ndarray,
    y_train: np.ndarray,
    seed: int,
) -> Pipeline:
    """
    Train the pipeline on enrolled_train data only.

    Parameters
    ----------
    X_train : (n_samples, n_features)  — enrolled_train feature matrix
    y_train : (n_samples,)             — device labels (integer)
    seed    : episode seed

    Returns
    -------
    Fitted Pipeline.
    """
    if X_train.shape[0] == 0:
        raise ValueError("X_train is empty — cannot train model.")
    unique_classes = np.unique(y_train)
    if len(unique_classes) < 2:
        raise ValueError(
            f"Training requires at least 2 classes; got {len(unique_classes)}."
        )
    LOG.info(
        "Training RF on %d samples, %d features, %d classes …",
        X_train.shape[0], X_train.shape[1], len(unique_classes),
    )
    pipe = build_pipeline(seed)
    pipe.fit(X_train, y_train)
    LOG.info("Training complete.")
    return pipe


# ---------------------------------------------------------------------------
# Scoring
# ---------------------------------------------------------------------------

def predict_scores(pipe: Pipeline, X: np.ndarray) -> np.ndarray:
    """
    Return max-class probability score for each sample in X.

    Score ∈ [0, 1]. Higher means the classifier is more confident the sample
    belongs to some enrolled device.

    Parameters
    ----------
    pipe : fitted Pipeline
    X    : (n_samples, n_features)

    Returns
    -------
    scores : (n_samples,) float64
    """
    if X.shape[0] == 0:
        return np.array([], dtype=np.float64)
    proba = pipe.predict_proba(X)   # (n_samples, n_classes)
    scores = proba.max(axis=1)
    return scores.astype(np.float64)


def predict_classes(pipe: Pipeline, X: np.ndarray) -> np.ndarray:
    """Return predicted class labels."""
    if X.shape[0] == 0:
        return np.array([], dtype=np.int64)
    return pipe.predict(X).astype(np.int64)


# ---------------------------------------------------------------------------
# Closed-set evaluation on cal_val
# ---------------------------------------------------------------------------

def evaluate_closed_set(
    pipe: Pipeline,
    X_cal: np.ndarray,
    y_cal: np.ndarray,
) -> Dict[str, float]:
    """
    Closed-set metrics on the cal_val partition (for diagnostics only).

    Returns dict with 'macro_f1' and 'accuracy'.
    """
    if X_cal.shape[0] == 0:
        return {"macro_f1": float("nan"), "accuracy": float("nan")}
    y_pred = predict_classes(pipe, X_cal)
    macro_f1 = compute_macro_f1(y_cal, y_pred)
    accuracy = float(np.mean(y_pred == y_cal))
    LOG.info("Closed-set cal_val: macro_F1=%.4f  accuracy=%.4f", macro_f1, accuracy)
    return {"macro_f1": macro_f1, "accuracy": accuracy}


# ---------------------------------------------------------------------------
# Save / load
# ---------------------------------------------------------------------------

def model_path(episode_idx: int) -> Path:
    return CFG.path_results / "models" / f"model_ep{episode_idx:03d}.joblib"


def save_model(pipe: Pipeline, episode_idx: int) -> Path:
    p = model_path(episode_idx)
    ensure_dir(p.parent)
    joblib.dump(pipe, p)
    LOG.debug("Model saved → %s", p)
    return p


def load_model(episode_idx: int) -> Pipeline:
    p = model_path(episode_idx)
    if not p.exists():
        raise FileNotFoundError(f"Model not found: {p}")
    return joblib.load(p)


# ---------------------------------------------------------------------------
# Convenience: build feature matrix from DataFrame split
# ---------------------------------------------------------------------------

def build_xy(
    df,
    feature_cols: List[str],
    label_col: str = "device_id",
) -> Tuple[np.ndarray, np.ndarray]:
    """Extract (X, y) from a pandas DataFrame."""
    X = df[feature_cols].values.astype(np.float64)
    y = df[label_col].values.astype(np.int64)
    return X, y


if __name__ == "__main__":
    import logging
    logging.basicConfig(level=logging.INFO)

    rng = np.random.default_rng(42)
    n_cls = 10
    n_per = 50
    n_feat = 20
    X = rng.standard_normal((n_cls * n_per, n_feat))
    y = np.repeat(np.arange(n_cls), n_per)

    pipe = train_model(X, y, seed=0)
    scores = predict_scores(pipe, X[:5])
    print("Scores (first 5):", scores)

    metrics = evaluate_closed_set(pipe, X, y)
    print("Closed-set metrics:", metrics)
    print("model.py self-test PASSED.")
