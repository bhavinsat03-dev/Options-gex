"""Run history: one JSON summary per ticker per run under <output>/history/."""

from __future__ import annotations

import json
from pathlib import Path

import pandas as pd

OI_COLUMNS = ["expiration", "strike", "type", "open_interest", "volume"]

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


def load_previous_day(history_dir: Path, ticker: str, stamp: str) -> dict | None:
    """Most recent summary for ``ticker`` from a day before ``stamp``'s day.

    Open interest updates once per day, so day-over-day is the meaningful
    comparison for it. Stamps are YYYYMMDD_HHMMSS in New York time.
    """
    return load_previous(history_dir, ticker, stamp[:8] + "_000000")


def oi_path(history_dir: Path, ticker: str, stamp: str) -> Path:
    return Path(history_dir) / f"{ticker}_{stamp}_oi.csv.gz"


def save_oi(history_dir: Path, ticker: str, stamp: str, contracts: pd.DataFrame) -> Path:
    """Compact per-contract OI snapshot, so later runs can report OI changes."""
    path = oi_path(history_dir, ticker, stamp)
    path.parent.mkdir(parents=True, exist_ok=True)
    cols = [c for c in OI_COLUMNS if c in contracts]
    contracts[cols].to_csv(path, index=False, compression="gzip")
    return path


def load_previous_day_oi(history_dir: Path, ticker: str, stamp: str) -> pd.DataFrame | None:
    """The OI snapshot matching ``load_previous_day``'s run, or None."""
    history_dir = Path(history_dir)
    if not history_dir.is_dir():
        return None
    prefix, cutoff = f"{ticker}_", stamp[:8] + "_000000"
    stamps = sorted(
        p.name[len(prefix):-len("_oi.csv.gz")]
        for p in history_dir.glob(f"{ticker}_*_oi.csv.gz")
        if p.name[len(prefix):-len("_oi.csv.gz")] < cutoff
    )
    if not stamps:
        return None
    return pd.read_csv(oi_path(history_dir, ticker, stamps[-1]), dtype={"expiration": str})


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
