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


def fake_earnings(ticker, settings, today):
    return "2026-10-29" if ticker == "QQQ" else None


def run(tmp_path, now, *args):
    cfg = tmp_path / "config.toml"
    if not cfg.exists():
        cfg.write_text('tickers = ["IGNORED"]\npause_between_tickers = 0\n')
    return cli.main([*args, "-c", str(cfg), "-o", str(tmp_path / "out")],
                    fetch=fake_fetch, fetch_spot=fake_spot, fetch_earnings=fake_earnings, now=now)


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
             fetch=fetch_shifted, fetch_earnings=fake_earnings, now=later)
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
    assert "| QQQ | 100.00 |" in brief and "110 (10,000; +" in brief
    assert "Failed: BAD" in brief


def test_brief_lists_next_walls(tmp_path, now):
    run(tmp_path, now, "QQQ", "--no-plots")
    brief = (tmp_path / "out" / "latest" / "brief.md").read_text()
    assert "| Net GEX | Call GEX | Put GEX |" in brief and "Abs gamma" not in brief
    assert "| Next call walls | Next put walls |" in brief and "Max call OI" not in brief
    summary = json.loads((tmp_path / "out" / "QQQ" / STAMP / "summary.json").read_text())
    assert " / ".join(f"{k:g}" for k in summary["call_walls"][1:]) in brief


def test_brief_key_expiries_and_oi_change(tmp_path, now):
    run(tmp_path, now, "QQQ", "--no-plots")
    brief = (tmp_path / "out" / "latest" / "brief.md").read_text()
    assert "### 3) Key expiries and wall OI change" in brief and "no prior day" in brief

    more = make_raw()
    more.loc[(more["type"] == "call") & (more["strike"] == 110), "open_interest"] += 500

    def fetch_more(ticker, settings, when):
        return 100.0, more

    cli.main(["QQQ", "-c", str(tmp_path / "config.toml"), "-o", str(tmp_path / "out"), "--no-plots"],
             fetch=fetch_more, fetch_earnings=fake_earnings, now=now + timedelta(days=1))
    brief = (tmp_path / "out" / "latest" / "brief.md").read_text()
    assert "call wall **110**" in brief and "OI 11,000, +1,000 vs Oct 16" in brief


def test_oi_change_labels_previous_day_in_new_york_time(tmp_path):
    from gex import report
    from datetime import datetime, timezone
    # 21:26 ET on Oct 19 is 01:26 UTC on Oct 20; label must say Oct 19.
    prev = {"as_of": datetime(2026, 10, 20, 1, 26, tzinfo=timezone.utc).isoformat(),
            "oi_at": {"call": {"110": 9000}, "put": {}}}
    s = {"oi_expiries": {"call_wall": {"strike": 110.0, "type": "call", "oi": 10000,
                                       "expiries": [{"expiration": "2026-11-20", "oi": 10000, "pct": 100.0}]}}}
    assert "+1,000 vs Oct 19" in report.key_expiry_line(s, prev)


def test_weekly_brief_without_history(tmp_path, now):
    run(tmp_path, now, "QQQ", "--no-plots", "--no-history", "--max-dte", "7", "--title", "Weekly")
    brief = (tmp_path / "out" / "latest" / "brief.md").read_text()
    assert brief.startswith("## Weekly: ")
    assert "### 3) Key expiries\n" in brief and "vs " not in brief and "no prior day" not in brief


def test_brief_omits_positioning_by_default(tmp_path, now):
    run(tmp_path, now, "QQQ", "--no-plots")
    brief = (tmp_path / "out" / "latest" / "brief.md").read_text()
    assert "Positioning changes" not in brief and "σ = one expected move" in brief
    summary = json.loads((tmp_path / "out" / "QQQ" / STAMP / "summary.json").read_text())
    assert "volume_vs_oi" in summary and "oi_changes" in summary


def test_brief_positioning_section(tmp_path, now):
    run(tmp_path, now, "QQQ", "--no-plots", "--positioning")
    brief = (tmp_path / "out" / "latest" / "brief.md").read_text()
    assert "### 4) Positioning changes" in brief and "OI change: no prior day" in brief
    assert (tmp_path / "out" / "history" / f"QQQ_{STAMP}_oi.csv.gz").exists()

    more = make_raw()
    more["volume"] = 0
    sel = (more["type"] == "put") & (more["strike"] == 95) & (more["expiration"] == "2026-10-23")
    more.loc[sel, "open_interest"] += 4000           # new positioning in the 95 puts
    more.loc[sel, "volume"] = 3000                   # ...and they are still trading hard today
    more.loc[(more["type"] == "call") & (more["strike"] == 110), "open_interest"] -= 300

    def fetch_more(ticker, settings, when):
        return 100.0, more

    cli.main(["QQQ", "-c", str(tmp_path / "config.toml"), "-o", str(tmp_path / "out"), "--no-plots",
              "--positioning"],
             fetch=fetch_more, fetch_earnings=fake_earnings, now=now + timedelta(days=1))
    brief = (tmp_path / "out" / "latest" / "brief.md").read_text()
    assert "OI adds vs Oct 16: 95P Oct 23 +4,000 (OI 5,000)" in brief
    assert "OI drops vs Oct 16: 110C Oct 23 -300" in brief or "OI drops vs Oct 16: 110C Nov 20 -300" in brief
    assert "High volume vs OI today: 95P Oct 23 vol 3,000 (0.6× OI 5,000)" in brief
    summary = json.loads((tmp_path / "out" / "QQQ" / "20261017_100000" / "summary.json").read_text())
    assert summary["oi_changes"]["adds"][0]["change"] == 4000


def test_brief_sigma_and_no_earnings_column(tmp_path, now):
    run(tmp_path, now, "QQQ", "NDX", "--no-plots")
    brief = (tmp_path / "out" / "latest" / "brief.md").read_text()
    assert "Earnings" not in brief and "Oct 29" not in brief
    qqq = next(line for line in brief.splitlines() if line.startswith("| QQQ |"))
    assert "σ)" in qqq                                # vs-flip and wall distances in expected-move units
    ndx = next(line for line in brief.splitlines() if line.startswith("| NDX"))
    assert "4510 (+" in ndx                            # σ still shown without OI for derived levels
    summary = json.loads((tmp_path / "out" / "QQQ" / STAMP / "summary.json").read_text())
    assert summary["earnings_date"] == "2026-10-29"   # still recorded, just not shown in the post


def test_earnings_outside_window_not_flagged(tmp_path, now):
    cfg = tmp_path / "config.toml"
    cfg.write_text('tickers = ["QQQ"]\npause_between_tickers = 0\n')
    cli.main(["QQQ", "-c", str(cfg), "-o", str(tmp_path / "out"), "--no-plots"],
             fetch=fake_fetch, fetch_earnings=lambda t, s, d: "2027-03-01", now=now)
    summary = json.loads((tmp_path / "out" / "QQQ" / STAMP / "summary.json").read_text())
    assert summary["earnings_date"] is None


def test_brief_colour_cues(tmp_path, now):
    run(tmp_path, now, "QQQ", "NDX", "--no-plots")
    brief = (tmp_path / "out" / "latest" / "brief.md").read_text()
    qqq = next(line for line in brief.splitlines() if line.startswith("| QQQ |"))
    assert ("🟢" in qqq) != ("🔴" in qqq)              # exactly one regime colour
    assert "🟩 +$" in qqq and "🟥 −$" in qqq           # call and put GEX squares
    assert "🟢/🔴 positive/negative gamma" in brief    # legend
    ndx = next(line for line in brief.splitlines() if line.startswith("| NDX"))
    assert "| - | - | - |" in ndx                      # derived ticker: no dollar figures, no stray emoji


def test_heatmap_written_with_plots(tmp_path, now):
    run(tmp_path, now, "QQQ")
    assert (tmp_path / "out" / "latest" / "heatmap.png").stat().st_size > 10_000


def test_heatmap_skipped_without_plots(tmp_path, now):
    run(tmp_path, now, "QQQ", "--no-plots")
    assert not (tmp_path / "out" / "latest" / "heatmap.png").exists()


def test_thin_chain_reported_as_unavailable(tmp_path, now):
    """Pre-market Yahoo chains keep a few stray contracts; they must not become levels."""
    thin = make_raw()
    thin["open_interest"] = 0
    thin.loc[(thin["type"] == "call") & (thin["strike"] == 80) & (thin["expiration"] == "2026-11-20"), "open_interest"] = 16

    def fetch_thin(ticker, settings, when):
        return 100.0, thin

    cfg = tmp_path / "config.toml"
    cfg.write_text('tickers = ["QQQ"]\npause_between_tickers = 0\n')
    code = cli.main(["QQQ", "-c", str(cfg), "-o", str(tmp_path / "out"), "--no-plots"],
                    fetch=fetch_thin, fetch_earnings=fake_earnings, now=now)
    assert code == 1                                         # every ticker failed: the run fails, nothing posts
    brief = (tmp_path / "out" / "latest" / "brief.md").read_text()
    assert "QQQ (error: data not available yet (16 contracts" in brief
    assert "| QQQ |" not in brief                            # no junk row in the tables
    assert not (tmp_path / "out" / "latest" / "QQQ_tradingview.txt").exists()
    assert not (tmp_path / "out" / "history").exists() or not list((tmp_path / "out" / "history").glob("QQQ_*"))
