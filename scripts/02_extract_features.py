#!/usr/bin/env python
"""
scripts/02_extract_features.py
Phase 3 — Feature Extraction.

Usage:
    python scripts/02_extract_features.py

Streams I/Q data device-by-device from data/raw/,
computes the fixed feature pipeline, caches to data/features/.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import numpy as np
from tqdm import tqdm

from src.config import CFG
from src.features import (
    determinism_test,
    extract_features,
    save_features_parquet,
)
from src.loader import stream_devices
from src.utils import get_logger

LOG = get_logger("02_extract_features")


def main() -> None:
    LOG.info("=== Phase 3: Feature Extraction ===")
    LOG.info("Reading from: %s", CFG.path_raw)
    LOG.info("Writing to:   %s", CFG.path_features)

    # Determine amplitude_stats flag from config (or default True if no audit yet)
    include_amp = not getattr(CFG, "amplitude_normalised", True)
    LOG.info("include_amplitude_stats = %s", include_amp)

    device_count = 0
    total_packets = 0
    total_nan = 0

    for iq, device_id in tqdm(stream_devices(), desc="Devices"):
        X, names = extract_features(iq, include_amplitude_stats=include_amp)

        nan_count = int(np.isnan(X).sum())
        total_nan += nan_count
        if nan_count > 0:
            LOG.warning("Device %d: %d NaN values in features!", device_id, nan_count)

        LOG.info(
            "Device %04d: %d packets, %d features (NaN=%d)",
            device_id, X.shape[0], X.shape[1], nan_count,
        )

        # Infer source file from interim cache name
        source_file = f"device_{device_id:04d}.npz"
        save_features_parquet(device_id, X, names, source_file=source_file)

        device_count += 1
        total_packets += X.shape[0]

    if device_count == 0:
        LOG.error(
            "No devices found. Place HDF5 files in %s and re-run.", CFG.path_raw
        )
        sys.exit(1)

    LOG.info(
        "Feature extraction complete: %d devices, %d total packets, %d total NaN.",
        device_count, total_packets, total_nan,
    )

    # Determinism check
    LOG.info("Running determinism test …")
    determinism_test()
    LOG.info("Determinism test PASSED.")


if __name__ == "__main__":
    main()
