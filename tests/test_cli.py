import json

import pandas as pd

from gex import cli
from gex.data import DataError

from conftest import make_raw


def fake_fetch(ticker, settings, now):
    if ticker == "BAD":
        raise DataError("no listed options for BAD")
    return 100.0, make_raw()


def test_end_to_end(tmp_path, now, capsys):
    cfg = tmp_path / "config.toml"
    cfg.write_text('tickers = ["IGNORED"]\npause_between_tickers = 0\n')
    rc = cli.main(["QQQ", "bad", "-c", str(cfg), "-o", str(tmp_path / "out")], fetch=fake_fetch, now=now)
    assert rc == 0

    run_dir = tmp_path / "out" / "QQQ" / "20261016_100000"
    for name in ("gex_by_strike.csv", "contracts.csv", "gex_profile.csv", "summary.json", "gex.png"):
        assert (run_dir / name).exists(), name
    summary = json.loads((run_dir / "summary.json").read_text())
    assert summary["call_wall"] == 110.0 and summary["put_wall"] == 90.0

    table = pd.read_csv(tmp_path / "out" / "summary_20261016_100000.csv")
    assert list(table["ticker"]) == ["QQQ", "BAD"]
    assert table.loc[0, "status"] == "ok"
    assert table.loc[1, "status"].startswith("error")
    assert not (tmp_path / "out" / "BAD").exists()

    out = capsys.readouterr().out
    assert "QQQ" in out and "BAD" in out


def test_all_fail_returns_nonzero(tmp_path, now):
    rc = cli.main(["BAD", "-c", str(tmp_path / "missing.toml"), "-o", str(tmp_path), "--no-plots"],
                  fetch=fake_fetch, now=now)
    assert rc == 1
