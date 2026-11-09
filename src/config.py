"""
src/config.py
Loads config.yaml and exposes a typed Config dataclass.
All other modules import from here — never read config.yaml directly.
"""
from __future__ import annotations

import os
import random
from dataclasses import dataclass, field
from pathlib import Path
from typing import List

import yaml

# ---------------------------------------------------------------------------
# Locate config.yaml: walk up from this file until found
# ---------------------------------------------------------------------------
def _find_config() -> Path:
    here = Path(__file__).resolve().parent
    for directory in [here, here.parent] + list(here.parents):
        candidate = directory / "config.yaml"
        if candidate.exists():
            return candidate
    raise FileNotFoundError("config.yaml not found anywhere above src/")


_CFG_PATH = _find_config()

with open(_CFG_PATH, "r") as _fh:
    _RAW: dict = yaml.safe_load(_fh)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def _project_root() -> Path:
    return _CFG_PATH.parent


def _resolve(rel: str) -> Path:
    return (_project_root() / rel).resolve()


# ---------------------------------------------------------------------------
# Config dataclass
# ---------------------------------------------------------------------------
@dataclass
class Config:
    # Reproducibility
    global_seed: int = 42
    n_episodes: int = 20

    # Device group sizes
    n_enrolled: int = 30
    n_proxy: int = 15
    n_final_unknown: int = 15

    # Packet splits
    train_frac: float = 0.70
    cal_val_frac: float = 0.15
    known_test_frac: float = 0.15
    proxy_cal_frac: float = 0.50
    proxy_test_frac: float = 0.50

    # Minimum packets
    min_packets: int = 150

    # Random Forest
    rf_n_estimators: int = 300
    rf_class_weight: str = "balanced"
    rf_n_jobs: int = -1

    # Threshold
    youden_primary: bool = True
    alternative_tau_known_acceptance: float = 0.95

    # LOPO / robust threshold
    lopo_alpha: float = 0.05
    lopo_percentile: int = 90

    # Sweep
    sweep_ks: List[int] = field(default_factory=lambda: [0, 1, 3, 5, 10, 15])

    # Amplitude normalisation (Shen et al. LoRa signals have mean ~0.217, not normalized to 1.0)
    amplitude_normalised: bool = False

    # FFT features
    fft_n_bins: int = 256
    fft_top_m_bins: int = 10
    fft_subbands: int = 4

    # Paths (resolved to absolute)
    path_raw: Path = field(default_factory=lambda: _resolve("data/raw"))
    path_interim: Path = field(default_factory=lambda: _resolve("data/interim"))
    path_features: Path = field(default_factory=lambda: _resolve("data/features"))
    path_results: Path = field(default_factory=lambda: _resolve("results"))
    path_reports: Path = field(default_factory=lambda: _resolve("reports"))
    path_paper: Path = field(default_factory=lambda: _resolve("paper"))
    path_figures: Path = field(default_factory=lambda: _resolve("results/figures"))
    path_tables: Path = field(default_factory=lambda: _resolve("results/tables"))

    def episode_seed(self, ep_idx: int) -> int:
        """Deterministic per-episode seed derived from global_seed."""
        rng = random.Random(self.global_seed)
        # Generate enough seeds up to ep_idx
        n_needed = max(ep_idx + 1, self.n_episodes + 1)
        seeds = [rng.randint(0, 2**31 - 1) for _ in range(n_needed)]
        return seeds[ep_idx]


def _build_config() -> Config:
    r = _RAW
    paths = r.get("paths", {})
    return Config(
        global_seed=r.get("global_seed", 42),
        n_episodes=r.get("n_episodes", 20),
        n_enrolled=r.get("n_enrolled", 30),
        n_proxy=r.get("n_proxy", 15),
        n_final_unknown=r.get("n_final_unknown", 15),
        train_frac=r.get("train_frac", 0.70),
        cal_val_frac=r.get("cal_val_frac", 0.15),
        known_test_frac=r.get("known_test_frac", 0.15),
        proxy_cal_frac=r.get("proxy_cal_frac", 0.50),
        proxy_test_frac=r.get("proxy_test_frac", 0.50),
        min_packets=r.get("min_packets", 150),
        rf_n_estimators=r.get("rf_n_estimators", 300),
        rf_class_weight=r.get("rf_class_weight", "balanced"),
        rf_n_jobs=r.get("rf_n_jobs", -1),
        youden_primary=r.get("youden_primary", True),
        alternative_tau_known_acceptance=r.get("alternative_tau_known_acceptance", 0.95),
        lopo_alpha=r.get("lopo_alpha", 0.05),
        lopo_percentile=r.get("lopo_percentile", 90),
        sweep_ks=r.get("sweep_ks", [0, 1, 3, 5, 10, 15]),
        amplitude_normalised=r.get("amplitude_normalised", False),
        fft_n_bins=r.get("fft_n_bins", 256),
        fft_top_m_bins=r.get("fft_top_m_bins", 10),
        fft_subbands=r.get("fft_subbands", 4),
        path_raw=_resolve(paths.get("raw", "data/raw")),
        path_interim=_resolve(paths.get("interim", "data/interim")),
        path_features=_resolve(paths.get("features", "data/features")),
        path_results=_resolve(paths.get("results", "results")),
        path_reports=_resolve(paths.get("reports", "reports")),
        path_paper=_resolve(paths.get("paper", "paper")),
        path_figures=_resolve(paths.get("figures", "results/figures")),
        path_tables=_resolve(paths.get("tables", "results/tables")),
    )


# Module-level singleton
CFG: Config = _build_config()


if __name__ == "__main__":
    print("Config loaded successfully.")
    print(f"  global_seed      : {CFG.global_seed}")
    print(f"  n_episodes       : {CFG.n_episodes}")
    print(f"  n_enrolled       : {CFG.n_enrolled}")
    print(f"  n_proxy          : {CFG.n_proxy}")
    print(f"  n_final_unknown  : {CFG.n_final_unknown}")
    print(f"  sweep_ks         : {CFG.sweep_ks}")
    print(f"  path_raw         : {CFG.path_raw}")

