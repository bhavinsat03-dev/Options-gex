from datetime import datetime, timezone

import pandas as pd
import pytest

NOW = datetime(2026, 10, 16, 14, 0, tzinfo=timezone.utc)  # Fri 10:00 ET


def make_raw(spot=100.0):
    """Synthetic raw chain: heavy call OI above spot, heavy put OI below."""
    rows = []
    for exp in ("2026-10-23", "2026-11-20"):
        for k in range(80, 121, 5):
            call_oi = 5000 if k == 110 else 1000 if k > spot else 200
            put_oi = 6000 if k == 90 else 1000 if k < spot else 200
            rows.append(("call", exp, float(k), call_oi, 0.20, 1.0, 1.1, 1.05))
            rows.append(("put", exp, float(k), put_oi, 0.25, 1.0, 1.1, 1.05))
    return pd.DataFrame(rows, columns=["type", "expiration", "strike", "open_interest", "iv", "bid", "ask", "last"])


@pytest.fixture
def now():
    return NOW


@pytest.fixture
def raw_chain():
    return make_raw()
