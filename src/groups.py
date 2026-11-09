"""
src/groups.py
Hardware-model grouping analysis.

Loads group information from reports/dataset_audit.md if available.
If group info is available: computes FAR for strangers sharing a hardware group
with enrolled devices vs not.

All inferences are labelled "inferred" if not from official documentation.
"""
from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import numpy as np
import pandas as pd

from src.config import CFG
from src.utils import ensure_dir, get_logger

LOG = get_logger(__name__)


# ---------------------------------------------------------------------------
# Parse group info from audit report
# ---------------------------------------------------------------------------

def load_group_info(
    audit_path: Optional[Path] = None,
) -> Tuple[Dict[int, str], bool]:
    """
    Load device-to-group mapping from dataset_audit.md if available.

    Returns (group_map, is_official) where:
      - group_map: {device_id: group_label}
      - is_official: True if from official documentation, False if inferred
    """
    if audit_path is None:
        audit_path = CFG.path_reports / "dataset_audit.md"

    if not audit_path.exists():
        LOG.info("No audit report found at %s. Returning empty group map.", audit_path)
        return {}, False

    text = audit_path.read_text(encoding="utf-8")

    # Try to find a "Hardware / Group Information" table in the markdown
    # Pattern: | device_id | group_label |
    group_map: Dict[int, str] = {}
    table_found = False

    lines = text.split("\n")
    in_table = False
    for i, line in enumerate(lines):
        # Detect hardware section
        if "Hardware" in line and "Group" in line and line.startswith("#"):
            in_table = True
            continue
        if in_table and line.startswith("|") and "device" in line.lower():
            # Header row — start reading data rows
            continue
        if in_table and line.startswith("|") and "---" in line:
            continue
        if in_table and line.startswith("|"):
            parts = [p.strip() for p in line.strip("|").split("|")]
            if len(parts) >= 2:
                try:
                    dev_id = int(parts[0])
                    grp = parts[1]
                    group_map[dev_id] = grp
                    table_found = True
                except ValueError:
                    pass
        elif in_table and not line.startswith("|") and line.strip():
            in_table = False

    if not table_found:
        LOG.info("No hardware group table found in audit report. Returning empty group map.")
        return {}, False

    # Check if labelled as official or inferred
    is_official = "inferred" not in text.lower()
    LOG.info(
        "Loaded %d device-to-group mappings (official=%s).",
        len(group_map), is_official,
    )
    return group_map, is_official


# ---------------------------------------------------------------------------
# Group-based FAR analysis
# ---------------------------------------------------------------------------

def run_group_analysis(
    n_episodes: Optional[int] = None,
    group_map: Optional[Dict[int, str]] = None,
) -> pd.DataFrame:
    """
    Compare FAR for strangers sharing a hardware group with enrolled
    vs strangers not sharing a group.

    Returns DataFrame (possibly empty if no group info available).
    """
    if group_map is None:
        group_map, is_official = load_group_info()
    else:
        is_official = False  # caller-provided; treat as inferred

    if not group_map:
        LOG.info("No group information available. Skipping group analysis.")
        return pd.DataFrame(columns=[
            "episode", "device_id", "group",
            "shares_group_with_enrolled", "FAR_B",
            "analysis_type",
        ])

    if n_episodes is None:
        n_episodes = CFG.n_episodes

    ep_dir = CFG.path_results / "episodes"
    all_rows = []

    for ep_idx in range(n_episodes):
        p = ep_dir / f"episode_{ep_idx:03d}.json"
        if not p.exists():
            continue
        with open(p) as fh:
            res = json.load(fh)

        enrolled_ids  = [int(x) for x in res.get("enrolled_ids", [])]
        pdev_far_b    = {int(k): float(v) for k, v in res.get("per_device_FAR_B", {}).items()}

        enrolled_groups = {group_map.get(eid) for eid in enrolled_ids if eid in group_map}

        for dev_id, far_b in pdev_far_b.items():
            grp = group_map.get(dev_id, "unknown")
            shares = grp in enrolled_groups and grp != "unknown"
            all_rows.append({
                "episode": ep_idx,
                "device_id": dev_id,
                "group": grp,
                "shares_group_with_enrolled": bool(shares),
                "FAR_B": far_b,
                "analysis_type": "official" if is_official else "inferred",
            })

    df = pd.DataFrame(all_rows)
    if len(df) > 0:
        # Summary statistics
        summary = df.groupby("shares_group_with_enrolled")["FAR_B"].agg(["mean", "std", "count"])
        LOG.info("Group FAR analysis:\n%s", summary)

    ensure_dir(CFG.path_tables)
    out_path = CFG.path_tables / "group_analysis.csv"
    df.to_csv(out_path, index=False)
    LOG.info("Group analysis saved → %s", out_path)
    return df


if __name__ == "__main__":
    LOG.info("groups.py self-test …")
    gm, official = load_group_info()
    LOG.info("Group map size: %d, official: %s", len(gm), official)
    try:
        df = run_group_analysis(n_episodes=1)
        print(df)
    except Exception as e:
        LOG.warning("Group analysis (expected during dev): %s", e)
    LOG.info("groups.py self-test complete.")
