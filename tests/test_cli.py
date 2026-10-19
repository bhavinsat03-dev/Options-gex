import json
from datetime import timedelta

import pandas as pd

from gex import cli
from gex.data import DataError

from conftest import make_raw

STAMP = "20261016_100000"


def fake_fetch(ticker, settings, now):
    if ticker in ("BAD", "NDX"):
        raise DataError(f"no listed options for {ticker}")
    return 100.0, make_raw()


def fake_spot(ticker, settings):
    if ticker == "NDX":
        return 4100.0
    raise DataError("no price")


def run(tmp_path, now, *args):
    cfg = tmp_path / "config.toml"
    if not cfg.exists():
        cfg.write_text('tickers = ["IGNORED"]\npause_between_tickers = 0\n')
    return cli.main([*args, "-c", str(cfg), "-o", str(tmp_path / "out")],
                    fetch=fake_fetch, fetch_spot=fake_spot, now=now)


def test_end_to_end(tmp_path, now, capsys):
    assert run(tmp_path, now, "QQQ", "bad") == 0

    run_dir = tmp_path / "out" / "QQQ" / STAMP
    for name in ("gex_by_strike.csv", "contracts.csv", "gamma_profile.csv", "summary.json",
                 "report.md", "gex.png", "gamma_profile.png"):
        assert (run_dir / name).exists(), name
    summary = json.loads((run_dir / "summary.json").read_text())
    assert summary["call_wall"] == 110.0 and summary["put_wall"] == 90.0
    assert len(summary["call_walls"]) == 3
    assert summary["regime"] in ("positive gamma", "negative gamma")
    assert summary["expected_move"]["strike"] == 100.0

    by_strike = pd.read_csv(run_dir / "gex_by_strike.csv")
    for col in ("dex", "vanna_exp", "charm_exp", "abs_gex"):
        assert col in by_strike

    report = (run_dir / "report.md").read_text()
    for metric in ("Net GEX", "Absolute gamma strike", "Zero-gamma flip", "Net vanna",
                   "Net charm", "Expected move", "25-delta skew", "Put/call OI ratio"):
        assert metric in report

    table = pd.read_csv(tmp_path / "out" / f"summary_{STAMP}.csv")
    assert list(table["ticker"]) == ["QQQ", "BAD"]
    assert table.loc[0, "status"] == "ok"
    assert table.loc[1, "status"].startswith("error")
    assert not (tmp_path / "out" / "BAD").exists()
    assert (tmp_path / "out" / "history" / f"QQQ_{STAMP}.json").exists()

    out = capsys.readouterr().out
    assert "QQQ" in out and "BAD" in out


def test_ndx_derived_from_qqq(tmp_path, now, capsys):
    assert run(tmp_path, now, "NDX") == 0
    summary = json.loads((tmp_path / "out" / "NDX" / STAMP / "summary.json").read_text())
    assert summary["derived"] is True and summary["derived_from"] == "QQQ"
    assert summary["call_wall"] == 110.0 * 41 and summary["put_wall"] == 90.0 * 41
    assert summary["net_gex"] is None
    assert "Derived levels" in (tmp_path / "out" / "NDX" / STAMP / "report.md").read_text()

    table = pd.read_csv(tmp_path / "out" / f"summary_{STAMP}.csv")
    assert list(table["ticker"]) == ["NDX"]
    assert table.loc[0, "status"] == "derived from QQQ"
    assert table.loc[0, "source"] == "derived from QQQ"
    assert "NDX*" in capsys.readouterr().out


def test_history_changes_printed(tmp_path, now, capsys):
    run(tmp_path, now, "QQQ")
    capsys.readouterr()
    # Second run a day later with walls shifted up by 5.
    shifted = make_raw()
    shifted["strike"] += 5

    def fetch_shifted(ticker, settings, when):
        return 105.0, shifted

    later = now + timedelta(days=1)
    cli.main(["QQQ", "-c", str(tmp_path / "config.toml"), "-o", str(tmp_path / "out"), "--no-plots"],
             fetch=fetch_shifted, now=later)
    out = capsys.readouterr().out
    assert "QQQ changes since" in out
    assert "Call wall: 110.00 -> 115.00 (+5.00)" in out
    report = (tmp_path / "out" / "QQQ" / "20261017_100000" / "report.md").read_text()
    assert "Changes since previous run" in report
    assert len(list((tmp_path / "out" / "history").glob("QQQ_*.json"))) == 2


def test_all_fail_returns_nonzero(tmp_path, now):
    assert run(tmp_path, now, "BAD", "--no-plots") == 1


def test_tradingview_outputs(tmp_path, now):
    run(tmp_path, now, "QQQ", "NDX", "--no-plots")
    line = (tmp_path / "out" / "latest" / "QQQ_tradingview.txt").read_text().strip()
    assert line.startswith("SYM=QQQ;ASOF=2026-10-16 10:00 ET;CW=110,")
    assert ";PW=90," in line and ";ZG=99.9;" in line and ";OC=110;OP=90;" in line and line.endswith(";SRC=chain")
    pine = (tmp_path / "out" / "QQQ" / STAMP / "tradingview.pine").read_text()
    assert pine.startswith("//@version=6") and f'input.string("{line}"' in pine
    ndx = (tmp_path / "out" / "latest" / "NDX_tradingview.txt").read_text()
    assert "SYM=NDX;" in ndx and "CW=4510," in ndx and ndx.strip().endswith("SRC=QQQ")


def test_brief_has_two_tables(tmp_path, now):
    run(tmp_path, now, "QQQ", "bad", "--no-plots")
    brief = (tmp_path / "out" / "latest" / "brief.md").read_text()
    assert "### 1) Levels" in brief and "### 2) Dealer positioning and volatility" in brief
    assert "| QQQ | 100.00 |" in brief and "110 (10,000)" in brief
    assert "Failed: BAD" in brief
