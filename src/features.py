"""
src/features.py
Fixed feature pipeline for LoRa preamble I/Q data.

Accepts (n_packets, preamble_len, 2) float32 or complex array.
Returns (n_packets, n_features) float64 array + feature name list.

Features computed:
  I/Q stats     : mean_I, std_I, skew_I, kurt_I, mean_Q, std_Q, skew_Q, kurt_Q,
                  IQ_corr, IQ_imbalance
  Phase stats   : mean_phase_unwrapped, std_phase_unwrapped,
                  mean_phase_detrended, std_phase_detrended
  Amplitude     : mean_amp, std_amp, skew_amp, kurt_amp   (if include_amplitude_stats)
  FFT features  : normalised magnitude vector (fft_n_bins bins),
                  sub-band energies (fft_subbands),
                  top-M dominant bin indices (fft_top_m_bins),
                  centroid, spread, flatness, entropy

Saves per-device feature matrices to data/features/ as parquet.

Usage:
    python src/features.py   (runs determinism self-test)
"""
from __future__ import annotations

import hashlib
from pathlib import Path
from typing import List, Optional, Tuple

import numpy as np
import pandas as pd
from scipy.stats import kurtosis, skew

from src.config import CFG
from src.utils import ensure_dir, get_logger

LOG = get_logger(__name__)


# ---------------------------------------------------------------------------
# Single-packet feature extraction
# ---------------------------------------------------------------------------

def _to_complex(iq: np.ndarray) -> np.ndarray:
    """Convert (L,2) or (L,) complex to (L,) complex128."""
    if np.iscomplexobj(iq):
        return iq.astype(np.complex128)
    if iq.ndim == 2 and iq.shape[1] == 2:
        return (iq[:, 0] + 1j * iq[:, 1]).astype(np.complex128)
    raise ValueError(f"Cannot convert IQ with shape {iq.shape} to complex.")


def _extract_one(
    pkt: np.ndarray,
    include_amplitude_stats: bool,
    fft_n_bins: int,
    fft_subbands: int,
    fft_top_m_bins: int,
) -> np.ndarray:
    """Extract features from a single preamble packet (L,2) or (L,) complex."""
    cplx = _to_complex(pkt)
    I = cplx.real
    Q = cplx.imag

    # --- I/Q statistics ---
    mean_I = float(np.mean(I))
    std_I  = float(np.std(I, ddof=1)) if len(I) > 1 else 0.0
    skew_I = float(skew(I, bias=False))
    kurt_I = float(kurtosis(I, bias=False))
    mean_Q = float(np.mean(Q))
    std_Q  = float(np.std(Q, ddof=1)) if len(Q) > 1 else 0.0
    skew_Q = float(skew(Q, bias=False))
    kurt_Q = float(kurtosis(Q, bias=False))

    # Pearson correlation I,Q
    if std_I > 0 and std_Q > 0:
        IQ_corr = float(np.corrcoef(I, Q)[0, 1])
    else:
        IQ_corr = 0.0

    # I/Q imbalance = std(I)/std(Q) - 1
    IQ_imbalance = (std_I / std_Q - 1.0) if std_Q > 0 else 0.0

    feats: List[float] = [mean_I, std_I, skew_I, kurt_I,
                          mean_Q, std_Q, skew_Q, kurt_Q,
                          IQ_corr, IQ_imbalance]

    # --- Phase statistics ---
    phase = np.angle(cplx)
    phase_unwrapped = np.unwrap(phase)
    mean_pu = float(np.mean(phase_unwrapped))
    std_pu  = float(np.std(phase_unwrapped, ddof=1)) if len(phase_unwrapped) > 1 else 0.0

    # Detrend: remove linear trend
    t = np.arange(len(phase_unwrapped), dtype=np.float64)
    if len(t) > 1:
        coeffs = np.polyfit(t, phase_unwrapped, 1)
        trend = np.polyval(coeffs, t)
        phase_detrended = phase_unwrapped - trend
    else:
        phase_detrended = phase_unwrapped.copy()
    mean_pd = float(np.mean(phase_detrended))
    std_pd  = float(np.std(phase_detrended, ddof=1)) if len(phase_detrended) > 1 else 0.0

    feats += [mean_pu, std_pu, mean_pd, std_pd]

    # --- Amplitude statistics (optional) ---
    if include_amplitude_stats:
        amp = np.abs(cplx)
        mean_amp = float(np.mean(amp))
        std_amp  = float(np.std(amp, ddof=1)) if len(amp) > 1 else 0.0
        skew_amp = float(skew(amp, bias=False))
        kurt_amp = float(kurtosis(amp, bias=False))
        feats += [mean_amp, std_amp, skew_amp, kurt_amp]

    # --- FFT features (Full two-sided baseband spectrum) ---
    # For complex baseband I/Q, spectrum spans [-Fs/2, +Fs/2].
    # Compute full FFT, shift DC to center, and bin to fft_n_bins.
    n_samples = len(cplx)
    if n_samples >= fft_n_bins:
        fft_full = np.fft.fft(cplx)
        fft_shifted = np.fft.fftshift(fft_full)
        fft_mag_full = np.abs(fft_shifted)
        chunk_size = len(fft_mag_full) // fft_n_bins
        fft_mag = fft_mag_full[:chunk_size * fft_n_bins].reshape(fft_n_bins, chunk_size).mean(axis=1)
    else:
        # Zero-pad to fft_n_bins if signal is shorter
        fft_full = np.fft.fft(cplx, n=fft_n_bins)
        fft_shifted = np.fft.fftshift(fft_full)
        fft_mag = np.abs(fft_shifted)

    fft_sum  = fft_mag.sum() + 1e-12
    fft_norm = fft_mag / fft_sum                       # normalised magnitude vector

    feats += fft_norm.tolist()

    # Sub-band energies
    band_len = fft_n_bins // fft_subbands
    for b in range(fft_subbands):
        s = b * band_len
        e = s + band_len
        feats.append(float(np.sum(fft_norm[s:e])))

    # Top-M dominant bin indices (normalised to [0,1])
    top_idx = np.argsort(fft_mag)[::-1][:fft_top_m_bins]
    top_idx_sorted = np.sort(top_idx)  # deterministic ordering
    feats += (top_idx_sorted / max(fft_n_bins - 1, 1)).tolist()

    # Spectral centroid
    bins = np.arange(fft_n_bins, dtype=np.float64)
    centroid = float(np.sum(bins * fft_norm))
    feats.append(centroid)

    # Spectral spread (variance around centroid)
    spread = float(np.sum(((bins - centroid) ** 2) * fft_norm))
    feats.append(spread)

    # Spectral flatness = geometric mean / arithmetic mean of magnitude
    gm = float(np.exp(np.mean(np.log(fft_mag + 1e-12))))
    am = float(np.mean(fft_mag) + 1e-12)
    flatness = gm / am
    feats.append(flatness)

    # Spectral entropy
    p = fft_norm / (fft_norm.sum() + 1e-12)
    entropy = float(-np.sum(p * np.log(p + 1e-12)))
    feats.append(entropy)

    return np.array(feats, dtype=np.float64)


# ---------------------------------------------------------------------------
# Feature name list
# ---------------------------------------------------------------------------

def feature_names(
    include_amplitude_stats: bool,
    fft_n_bins: int,
    fft_subbands: int,
    fft_top_m_bins: int,
) -> List[str]:
    names: List[str] = [
        "mean_I", "std_I", "skew_I", "kurt_I",
        "mean_Q", "std_Q", "skew_Q", "kurt_Q",
        "IQ_corr", "IQ_imbalance",
        "mean_phase_unwrapped", "std_phase_unwrapped",
        "mean_phase_detrended", "std_phase_detrended",
    ]
    if include_amplitude_stats:
        names += ["mean_amp", "std_amp", "skew_amp", "kurt_amp"]
    names += [f"fft_bin_{i}" for i in range(fft_n_bins)]
    names += [f"fft_subband_{b}" for b in range(fft_subbands)]
    names += [f"fft_top_{m}_bin_idx" for m in range(fft_top_m_bins)]
    names += ["fft_centroid", "fft_spread", "fft_flatness", "fft_entropy"]
    return names


# ---------------------------------------------------------------------------
# Batch extraction
# ---------------------------------------------------------------------------

def extract_features(
    iq: np.ndarray,
    include_amplitude_stats: Optional[bool] = None,
    fft_n_bins: Optional[int] = None,
    fft_subbands: Optional[int] = None,
    fft_top_m_bins: Optional[int] = None,
) -> Tuple[np.ndarray, List[str]]:
    """
    Compute feature matrix for all packets.

    Parameters
    ----------
    iq : np.ndarray
        Shape (n_packets, preamble_len, 2) float or (n_packets, preamble_len) complex.
    include_amplitude_stats : bool, optional
        Whether to include amplitude stats. Reads from CFG if None.

    Returns
    -------
    X : np.ndarray  shape (n_packets, n_features)
    names : List[str]
    """
    if include_amplitude_stats is None:
        include_amplitude_stats = not getattr(CFG, "amplitude_normalised", True)
    if fft_n_bins is None:
        fft_n_bins = CFG.fft_n_bins
    if fft_subbands is None:
        fft_subbands = CFG.fft_subbands
    if fft_top_m_bins is None:
        fft_top_m_bins = CFG.fft_top_m_bins

    n_packets = iq.shape[0]
    rows: List[np.ndarray] = []
    for i in range(n_packets):
        pkt = iq[i]  # (L, 2) or (L,) complex
        rows.append(
            _extract_one(pkt, include_amplitude_stats, fft_n_bins, fft_subbands, fft_top_m_bins)
        )

    X = np.stack(rows, axis=0)
    names = feature_names(include_amplitude_stats, fft_n_bins, fft_subbands, fft_top_m_bins)
    assert X.shape[1] == len(names), (
        f"Feature count mismatch: X has {X.shape[1]} cols, names has {len(names)}"
    )
    return X, names


# ---------------------------------------------------------------------------
# Save / load feature parquet
# ---------------------------------------------------------------------------

def feature_parquet_path(device_id: int) -> Path:
    return CFG.path_features / f"device_{device_id:04d}_features.parquet"


def save_features_parquet(
    device_id: int,
    X: np.ndarray,
    names: List[str],
    source_file: str = "",
) -> Path:
    """Save feature matrix + metadata to parquet."""
    ensure_dir(CFG.path_features)
    n = X.shape[0]
    meta = {
        "device_id": np.full(n, device_id, dtype=np.int64),
        "packet_idx": np.arange(n, dtype=np.int64),
        "source_file": [source_file] * n,
    }
    df = pd.DataFrame(meta)
    feat_df = pd.DataFrame(X, columns=names)
    df = pd.concat([df, feat_df], axis=1)
    out_path = feature_parquet_path(device_id)
    df.to_parquet(out_path, index=False)
    LOG.debug("Saved features for device %d → %s (%d packets, %d feats)",
              device_id, out_path.name, n, len(names))
    return out_path


def load_features_parquet(device_id: int) -> pd.DataFrame:
    """Load feature parquet for one device."""
    p = feature_parquet_path(device_id)
    if not p.exists():
        raise FileNotFoundError(f"Feature parquet not found for device {device_id}: {p}")
    return pd.read_parquet(p)


def load_all_features(device_ids: Optional[List[int]] = None) -> pd.DataFrame:
    """Load all (or selected) device feature parquets into one DataFrame."""
    if device_ids is None:
        parquets = sorted(CFG.path_features.glob("device_*_features.parquet"))
        device_ids = [int(p.stem.split("_")[1]) for p in parquets]
    frames = [load_features_parquet(did) for did in device_ids]
    if not frames:
        raise FileNotFoundError(
            f"No feature parquets found in {CFG.path_features}. "
            "Run scripts/02_extract_features.py first."
        )
    return pd.concat(frames, ignore_index=True)


# ---------------------------------------------------------------------------
# Determinism test
# ---------------------------------------------------------------------------

def determinism_test(n_packets: int = 10, preamble_len: int = 512) -> None:
    """Assert that feature extraction is deterministic (no randomness)."""
    rng = np.random.default_rng(0)
    iq = rng.standard_normal((n_packets, preamble_len, 2)).astype(np.float32)

    X1, n1 = extract_features(iq)
    X2, n2 = extract_features(iq)

    assert n1 == n2, "Feature name lists differ between runs"
    assert np.allclose(X1, X2, atol=1e-6), "Feature matrices differ between determinism runs"
    LOG.info("Determinism test PASSED (%d packets, %d features).", n_packets, X1.shape[1])


if __name__ == "__main__":
    LOG.info("features.py self-test …")
    determinism_test()

    # Quick shape check
    rng = np.random.default_rng(99)
    iq = rng.standard_normal((5, 64, 2)).astype(np.float32)
    X, names = extract_features(iq)
    LOG.info("Shape: X=%s, n_features=%d", X.shape, len(names))
    nan_count = int(np.isnan(X).sum())
    LOG.info("NaN count: %d", nan_count)
    assert nan_count == 0, "NaN values found in features!"
    LOG.info("features.py self-test PASSED.")
