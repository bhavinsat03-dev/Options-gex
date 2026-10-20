from gex import history


def test_save_load_previous_and_diff(tmp_path):
    old = {"ticker": "QQQ", "call_wall": 600.0, "put_wall": 580.0, "zero_gamma": 590.5,
           "abs_gamma_strike": 590.0, "net_gex": 1.0e9, "as_of": "a"}
    older = dict(old, call_wall=1.0)
    history.save(tmp_path, older, "20261014_100000")
    history.save(tmp_path, old, "20261015_100000")
    history.save(tmp_path, dict(old, ticker="SPY"), "20261015_120000")

    prev = history.load_previous(tmp_path, "QQQ", "20261016_100000")
    assert prev["call_wall"] == 600.0  # latest earlier run, other tickers ignored
    assert history.load_previous(tmp_path, "QQQ", "20261014_100000") is None
    assert history.load_previous(tmp_path / "missing", "QQQ", "x") is None

    new = dict(old, call_wall=610.0, put_wall=575.0, zero_gamma=None, net_gex=-5.0e8)
    changes = {c["field"]: c for c in history.diff(prev, new)}
    assert changes["call_wall"]["change"] == 10.0
    assert changes["put_wall"]["change"] == -5.0
    assert changes["net_gex"]["change"] == -1.5e9
    assert "zero_gamma" not in changes  # missing in new run


def test_load_previous_day_skips_same_day(tmp_path):
    history.save(tmp_path, {"ticker": "QQQ", "v": 1}, "20261019_150000")
    history.save(tmp_path, {"ticker": "QQQ", "v": 2}, "20261020_095000")
    assert history.load_previous_day(tmp_path, "QQQ", "20261020_123000")["v"] == 1
    assert history.load_previous(tmp_path, "QQQ", "20261020_123000")["v"] == 2
