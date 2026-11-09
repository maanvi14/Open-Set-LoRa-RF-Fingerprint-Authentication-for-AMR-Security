"""
src/utils.py
Shared utilities: logging setup, path helpers, safe JSON/YAML I/O.
"""
from __future__ import annotations

import json
import logging
import sys
from pathlib import Path
from typing import Any

import yaml


def get_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s"))
        logger.addHandler(handler)
    logger.setLevel(level)
    return logger


def ensure_dir(path: Path) -> Path:
    path.mkdir(parents=True, exist_ok=True)
    return path


def save_json(obj: Any, path: Path) -> None:
    ensure_dir(path.parent)
    with open(path, "w") as fh:
        json.dump(obj, fh, indent=2, default=str)


def load_json(path: Path) -> Any:
    with open(path, "r") as fh:
        return json.load(fh)


def save_yaml(obj: Any, path: Path) -> None:
    ensure_dir(path.parent)
    with open(path, "w") as fh:
        yaml.safe_dump(obj, fh)

