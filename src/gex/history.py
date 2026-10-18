"""Run history: one JSON summary per ticker per run under <output>/history/."""

from __future__ import annotations

import json
from pathlib import Path

TRACKED = [
    ("call_wall", "Call wall"),
    ("put_wall", "Put wall"),
    ("zero_gamma", "Zero gamma"),
    ("abs_gamma_strike", "Abs gamma strike"),
    ("net_gex", "Net GEX"),
]


def history_path(history_dir: Path, ticker: str, stamp: str) -> Path:
    return Path(history_dir) / f"{ticker}_{stamp}.json"


def load_previous(history_dir: Path, ticker: str, stamp: str) -> dict | None:
    """Most recent saved summary for ``ticker`` from before ``stamp``."""
    history_dir = Path(history_dir)
    if not history_dir.is_dir():
        return None
    prefix = f"{ticker}_"
    stamps = sorted(
        p.stem[len(prefix):]
        for p in history_dir.glob(f"{ticker}_*.json")
        if p.stem[len(prefix):] < stamp
    )
    if not stamps:
        return None
    return json.loads(history_path(history_dir, ticker, stamps[-1]).read_text())


def save(history_dir: Path, summary: dict, stamp: str) -> Path:
    path = history_path(history_dir, summary["ticker"], stamp)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(summary, indent=2))
    return path


def diff(previous: dict, current: dict) -> list[dict]:
    """Changes in the tracked fields; fields missing in either run are skipped."""
    changes = []
    for key, label in TRACKED:
        old, new = previous.get(key), current.get(key)
        if old is None or new is None:
            continue
        changes.append({"field": key, "label": label, "old": old, "new": new, "change": new - old})
    return changes
