"""
src/loader.py
Streaming HDF5 loader for LoRa_RFFI dataset.

Discovers file structure automatically. Streams slices device-by-device
WITHOUT loading full multi-gigabyte HDF5 arrays into memory.
Caches per-device I/Q slices to data/interim/ as npz.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, Generator, List, Optional, Tuple

import h5py
import numpy as np

from src.config import CFG
from src.utils import ensure_dir, get_logger

LOG = get_logger(__name__)

# Baseline primary files (unaugmented) to avoid mixing duplicate / augmented / channel variations:
# 1-30: Train/dataset_training_no_aug.h5
# 31-40: Test/dataset_residential.h5
# 41-45: Test/dataset_rogue.h5
# 46-60: Test/dataset_other_device_type.h5
_PRIMARY_FILES = [
    "dataset_training_no_aug.h5",
    "dataset_residential.h5",
    "dataset_rogue.h5",
    "dataset_other_device_type.h5"
]

def _get_target_h5_files() -> List[Path]:
    """Find the canonical unaugmented baseline files containing all 60 devices."""
    all_h5 = sorted(CFG.path_raw.rglob("*.h5")) + sorted(CFG.path_raw.rglob("*.hdf5"))
    primary = [f for f in all_h5 if f.name in _PRIMARY_FILES]
    if len(primary) != len(_PRIMARY_FILES):
        missing = set(_PRIMARY_FILES) - {f.name for f in primary}
        raise FileNotFoundError(
            f"Missing required primary unaugmented baseline file(s): {missing}. "
            f"Found only {[f.name for f in primary]}. Refusing to fall back to augmented or channel-problem files."
        )
    return primary


def discover_dataset_structure(h5_path: Path) -> Dict[str, Tuple]:
    """Return {key: (shape, dtype)} for every dataset in an HDF5 file."""
    result: Dict[str, Tuple] = {}
    with h5py.File(h5_path, "r") as fh:
        def _visitor(name, obj):
            if isinstance(obj, h5py.Dataset):
                result[name] = (obj.shape, str(obj.dtype))
        fh.visititems(_visitor)
    return result


def _interim_path(device_id: int) -> Path:
    return CFG.path_interim / f"device_{device_id:04d}.npz"


def _save_interim(device_id: int, iq: np.ndarray) -> None:
    ensure_dir(CFG.path_interim)
    np.savez_compressed(_interim_path(device_id), iq=iq)


def _load_interim(device_id: int) -> Optional[np.ndarray]:
    p = _interim_path(device_id)
    if p.exists():
        return np.load(p)["iq"]
    return None


def stream_devices(
    force_reload: bool = False,
) -> Generator[Tuple[np.ndarray, int], None, None]:
    """
    Yield (iq_array: float32 (N,L,2), device_id: int) for each device.
    Uses chunked / indexed slicing from HDF5 to remain strictly low-memory.
    """
    h5_files = _get_target_h5_files()
    if not h5_files:
        raise FileNotFoundError(
            f"No HDF5 files found in {CFG.path_raw}. "
            "Please place the LoRa_RFFI dataset files in data/raw/."
        )

    # First, check if all 60 devices are already cached in interim
    cached_all = True
    for dev_id in range(1, 61):
        if not _interim_path(dev_id).exists():
            cached_all = False
            break

    if cached_all and not force_reload:
        LOG.info("All 60 devices found in interim cache. Streaming from cache...")
        for dev_id in range(1, 61):
            iq = _load_interim(dev_id)
            yield iq, dev_id
        return

    # Scan target HDF5 files device by device
    LOG.info("Streaming and caching devices from HDF5 files...")
    ensure_dir(CFG.path_interim)

    for h5path in h5_files:
        LOG.info("Processing %s ...", h5path.name)
        with h5py.File(h5path, "r") as fh:
            labels = fh["label"][:].ravel().astype(np.int64)
            data_dset = fh["data"]
            unique_devs = np.unique(labels)

            for dev in unique_devs:
                cached = _load_interim(int(dev)) if not force_reload else None
                if cached is not None:
                    continue

                idx = np.where(labels == dev)[0]
                # Slice indices in chunks to minimize memory consumption
                # Each packet has 16384 samples -> (8192 I, 8192 Q)
                raw_chunk = data_dset[idx] # (n_packets, 16384)
                n_pkts, two_l = raw_chunk.shape
                L = two_l // 2
                iq = np.stack([raw_chunk[:, :L], raw_chunk[:, L:]], axis=-1).astype(np.float32)
                _save_interim(int(dev), iq)
                LOG.info("Cached device %d: %d packets.", int(dev), n_pkts)

    # Stream out the sorted devices
    for dev_id in range(1, 61):
        iq = _load_interim(dev_id)
        if iq is not None:
            yield iq, dev_id


def load_all_devices(force_reload: bool = False) -> Dict[int, np.ndarray]:
    """Return {device_id: iq_array} dict."""
    return {dev_id: iq for iq, dev_id in stream_devices(force_reload=force_reload)}


if __name__ == "__main__":
    LOG.info("loader.py test run...")
    count = 0
    for iq, dev_id in stream_devices():
        count += 1
        if count <= 3 or count == 60:
            LOG.info("Device %d: shape=%s, dtype=%s", dev_id, iq.shape, iq.dtype)
    LOG.info("Streaming completed for %d devices.", count)
