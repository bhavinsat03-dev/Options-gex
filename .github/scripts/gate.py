"""Decide whether a scheduled run should go ahead.

GitHub cron is UTC-only and can start runs late or drop them. Each slot
(New York time) is listed twice in the workflow, once per DST offset, so
there are two chances per slot. A firing runs the most recent slot that
started within WINDOW and has not been done today; done slots are read
from output/latest/slots.txt on the data branch.

A manual run may claim a slot explicitly ("YYYY-MM-DD HH:MM"); it then
runs only if that slot isn't done yet, and is recorded and posted like a
scheduled run. This lets an external on-time trigger beat GitHub's delays.

Usage: gate.py <event_name> <done_slots_file> [claimed_slot]; prints run=..., slot=...
"""

import sys
from datetime import datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

SLOTS = ["09:50", "12:30", "15:00"]
WINDOW = timedelta(minutes=120)


def decide(event: str, done: set[str], now: datetime, claimed: str = "") -> tuple[bool, str]:
    if claimed:
        return claimed not in done, claimed
    if event != "schedule":
        return True, "manual"
    if now.weekday() >= 5:
        return False, ""
    started = []
    for hhmm in SLOTS:
        h, m = map(int, hhmm.split(":"))
        start = now.replace(hour=h, minute=m, second=0, microsecond=0)
        if start <= now <= start + WINDOW:
            started.append(start)
    if not started:
        return False, ""
    key = max(started).strftime("%Y-%m-%d %H:%M")
    return key not in done, key


if __name__ == "__main__":
    event, done_file = sys.argv[1], Path(sys.argv[2])
    done = set(done_file.read_text().split("\n")) if done_file.exists() else set()
    claimed = sys.argv[3].strip() if len(sys.argv) > 3 else ""
    run, slot = decide(event, done, datetime.now(ZoneInfo("America/New_York")), claimed)
    print(f"run={'true' if run else 'false'}")
    print(f"slot={slot}")
