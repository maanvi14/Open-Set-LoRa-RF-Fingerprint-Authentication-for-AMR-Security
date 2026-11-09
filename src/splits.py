"""
src/splits.py
Seeded per-episode device/packet splitting for the Familiar-Stranger experiment.

Produces an EpisodeSplit dataclass containing:
  - device assignments (enrolled, proxy, final_unknown)
  - packet index assignments for every subset

All assertions about leakage are embedded here and can be called externally.

Usage:
    python src/splits.py   (runs quick self-test)
"""
from __future__ import annotations

import json
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Dict, List, Optional

import numpy as np

from src.config import CFG
from src.utils import ensure_dir, get_logger, save_json

LOG = get_logger(__name__)


# ---------------------------------------------------------------------------
# EpisodeSplit dataclass
# ---------------------------------------------------------------------------

@dataclass
class EpisodeSplit:
    """
    All device/packet assignments for one episode.

    All index dicts are keyed by device_id (int) → np.ndarray of packet indices.
    """
    episode_idx: int
    seed: int

    # Device assignments
    enrolled_ids: List[int]
    proxy_ids: List[int]
    final_unknown_ids: List[int]

    # Enrolled packet splits (by device)
    enrolled_train_idx: Dict[int, np.ndarray] = field(default_factory=dict)
    enrolled_cal_val_idx: Dict[int, np.ndarray] = field(default_factory=dict)
    enrolled_known_test_idx: Dict[int, np.ndarray] = field(default_factory=dict)

    # Proxy packet splits (by device — same 15 devices, different packet indices)
    proxy_cal_idx: Dict[int, np.ndarray] = field(default_factory=dict)
    proxy_test_idx: Dict[int, np.ndarray] = field(default_factory=dict)

    # Final-unknown (by device — packet indices into their own arrays)
    final_test_idx: Dict[int, np.ndarray] = field(default_factory=dict)

    def to_json_serialisable(self) -> dict:
        """Convert to JSON-serialisable dict (arrays become lists)."""
        d = {
            "episode_idx": self.episode_idx,
            "seed": self.seed,
            "enrolled_ids": self.enrolled_ids,
            "proxy_ids": self.proxy_ids,
            "final_unknown_ids": self.final_unknown_ids,
            "enrolled_train_idx": {str(k): v.tolist() for k, v in self.enrolled_train_idx.items()},
            "enrolled_cal_val_idx": {str(k): v.tolist() for k, v in self.enrolled_cal_val_idx.items()},
            "enrolled_known_test_idx": {str(k): v.tolist() for k, v in self.enrolled_known_test_idx.items()},
            "proxy_cal_idx": {str(k): v.tolist() for k, v in self.proxy_cal_idx.items()},
            "proxy_test_idx": {str(k): v.tolist() for k, v in self.proxy_test_idx.items()},
            "final_test_idx": {str(k): v.tolist() for k, v in self.final_test_idx.items()},
        }
        return d

    def save(self, path: Path) -> None:
        save_json(self.to_json_serialisable(), path)


# ---------------------------------------------------------------------------
# Split creation
# ---------------------------------------------------------------------------

def _split_indices(
    n: int,
    fracs: List[float],
    rng: np.random.Generator,
) -> List[np.ndarray]:
    """
    Split n packet indices into len(fracs) parts by the given fractions.
    Uses a fixed-order split (first frac[0]*n, next frac[1]*n, remainder).
    Does NOT shuffle to keep indices monotonic — caller shuffles if needed.
    """
    assert abs(sum(fracs) - 1.0) < 1e-9, f"Fracs must sum to 1.0, got {sum(fracs)}"
    idx = np.arange(n)
    rng.shuffle(idx)  # shuffle within device, seed-controlled
    cuts = []
    start = 0
    for f in fracs[:-1]:
        end = start + max(1, int(round(f * n)))
        end = min(end, n - len(fracs) + len(cuts) + 1)  # leave at least 1 for remaining
        cuts.append(idx[start:end])
        start = end
    cuts.append(idx[start:])
    return cuts


def create_episode_split(
    all_device_ids: List[int],
    packet_counts: Dict[int, int],
    episode_idx: int,
    seed: Optional[int] = None,
) -> EpisodeSplit:
    """
    Create a full EpisodeSplit for one episode.

    Parameters
    ----------
    all_device_ids : List[int]
        All 60 device IDs in the dataset.
    packet_counts : Dict[int, int]
        {device_id: n_packets} for all devices.
    episode_idx : int
        Episode index (0-based).
    seed : int, optional
        Seed for this episode (derived from CFG.episode_seed if None).
    """
    if seed is None:
        seed = CFG.episode_seed(episode_idx)

    rng = np.random.default_rng(seed)

    total = len(all_device_ids)
    n_en  = CFG.n_enrolled
    n_px  = CFG.n_proxy
    n_fu  = CFG.n_final_unknown

    if total < n_en + n_px + n_fu:
        raise ValueError(
            f"Not enough devices: need {n_en+n_px+n_fu}, have {total}"
        )

    # Shuffle devices
    dev_arr = np.array(sorted(all_device_ids))
    rng.shuffle(dev_arr)

    enrolled_ids   = sorted(dev_arr[:n_en].tolist())
    proxy_ids      = sorted(dev_arr[n_en:n_en + n_px].tolist())
    final_unk_ids  = sorted(dev_arr[n_en + n_px:n_en + n_px + n_fu].tolist())

    split = EpisodeSplit(
        episode_idx=episode_idx,
        seed=seed,
        enrolled_ids=enrolled_ids,
        proxy_ids=proxy_ids,
        final_unknown_ids=final_unk_ids,
    )

    # --- Enrolled packet splits ---
    fracs_en = [CFG.train_frac, CFG.cal_val_frac, CFG.known_test_frac]
    # Normalise in case they don't sum to exactly 1 due to float issues
    total_frac = sum(fracs_en)
    fracs_en = [f / total_frac for f in fracs_en]

    for dev_id in enrolled_ids:
        n = packet_counts[dev_id]
        dev_rng = np.random.default_rng(seed ^ (dev_id * 7919 + 1))
        parts = _split_indices(n, fracs_en, dev_rng)
        split.enrolled_train_idx[dev_id]      = np.sort(parts[0])
        split.enrolled_cal_val_idx[dev_id]    = np.sort(parts[1])
        split.enrolled_known_test_idx[dev_id] = np.sort(parts[2])

    # --- Proxy packet splits ---
    fracs_px = [CFG.proxy_cal_frac, CFG.proxy_test_frac]
    total_px = sum(fracs_px)
    fracs_px = [f / total_px for f in fracs_px]

    for dev_id in proxy_ids:
        n = packet_counts[dev_id]
        dev_rng = np.random.default_rng(seed ^ (dev_id * 6271 + 2))
        parts = _split_indices(n, fracs_px, dev_rng)
        split.proxy_cal_idx[dev_id]  = np.sort(parts[0])
        split.proxy_test_idx[dev_id] = np.sort(parts[1])

    # --- Final-unknown: all packets go to final_test ---
    for dev_id in final_unk_ids:
        n = packet_counts[dev_id]
        split.final_test_idx[dev_id] = np.arange(n)

    return split


# ---------------------------------------------------------------------------
# Leakage assertions
# ---------------------------------------------------------------------------

def assert_no_leakage(split: EpisodeSplit) -> None:
    """
    Run all leakage assertions on an EpisodeSplit. Raises AssertionError on violation.
    """
    en_set = set(split.enrolled_ids)
    px_set = set(split.proxy_ids)
    fu_set = set(split.final_unknown_ids)

    # 1. Device group disjointness
    assert len(en_set & px_set) == 0, \
        f"Enrolled ∩ Proxy = {en_set & px_set}"
    assert len(en_set & fu_set) == 0, \
        f"Enrolled ∩ FinalUnknown = {en_set & fu_set}"
    assert len(px_set & fu_set) == 0, \
        f"Proxy ∩ FinalUnknown = {px_set & fu_set}"

    # 2. FINAL_UNKNOWN devices have no packets in any other split
    for dev_id in split.final_unknown_ids:
        assert dev_id not in split.enrolled_train_idx, \
            f"Final-unknown device {dev_id} found in enrolled_train"
        assert dev_id not in split.enrolled_cal_val_idx, \
            f"Final-unknown device {dev_id} found in enrolled_cal_val"
        assert dev_id not in split.enrolled_known_test_idx, \
            f"Final-unknown device {dev_id} found in enrolled_known_test"
        assert dev_id not in split.proxy_cal_idx, \
            f"Final-unknown device {dev_id} found in proxy_cal"
        assert dev_id not in split.proxy_test_idx, \
            f"Final-unknown device {dev_id} found in proxy_test"

    # 3. Enrolled packet splits are disjoint for each device
    for dev_id in split.enrolled_ids:
        tr = set(split.enrolled_train_idx[dev_id].tolist())
        cv = set(split.enrolled_cal_val_idx[dev_id].tolist())
        kt = set(split.enrolled_known_test_idx[dev_id].tolist())
        assert len(tr & cv) == 0, f"Device {dev_id}: train ∩ cal_val not empty"
        assert len(tr & kt) == 0, f"Device {dev_id}: train ∩ known_test not empty"
        assert len(cv & kt) == 0, f"Device {dev_id}: cal_val ∩ known_test not empty"

    # 4. Proxy packet splits are disjoint per device
    for dev_id in split.proxy_ids:
        pc = set(split.proxy_cal_idx[dev_id].tolist())
        pt = set(split.proxy_test_idx[dev_id].tolist())
        assert len(pc & pt) == 0, \
            f"Proxy device {dev_id}: PROXY_CAL ∩ PROXY_TEST not empty"

    LOG.debug("All leakage assertions passed for episode %d.", split.episode_idx)


def assert_known_test_identical(split_a: EpisodeSplit, split_b: EpisodeSplit) -> None:
    """
    Assert that known_test packet indices are identical across two splits
    (Condition A and B must share the same FRR base).
    """
    for dev_id in split_a.enrolled_ids:
        idx_a = split_a.enrolled_known_test_idx[dev_id]
        idx_b = split_b.enrolled_known_test_idx.get(dev_id)
        assert idx_b is not None, f"Device {dev_id} missing from split_b known_test"
        assert np.array_equal(idx_a, idx_b), \
            f"known_test indices differ for device {dev_id}"


# ---------------------------------------------------------------------------
# Save/load split JSON
# ---------------------------------------------------------------------------

def save_split(split: EpisodeSplit, out_dir: Optional[Path] = None) -> Path:
    if out_dir is None:
        out_dir = CFG.path_results / "episodes"
    ensure_dir(out_dir)
    p = out_dir / f"split_{split.episode_idx:03d}.json"
    split.save(p)
    return p


def load_split_json(path: Path) -> dict:
    with open(path, "r") as fh:
        return json.load(fh)


if __name__ == "__main__":
    LOG.info("splits.py self-test …")
    rng = np.random.default_rng(42)
    # Fake 60 devices with ~300 packets each
    dev_ids = list(range(60))
    pkt_counts = {d: int(rng.integers(200, 400)) for d in dev_ids}

    split = create_episode_split(dev_ids, pkt_counts, episode_idx=0)
    assert_no_leakage(split)
    LOG.info(
        "Episode 0: enrolled=%d, proxy=%d, final_unknown=%d",
        len(split.enrolled_ids), len(split.proxy_ids), len(split.final_unknown_ids),
    )
    LOG.info("splits.py self-test PASSED.")
