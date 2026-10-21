# SPY gamma exposure report

As of 2026-10-21T09:59:32+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 769.05 | The underlying price used for every calculation in this run. |
| Net GEX | $17.5K | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | positive gamma | Dealer hedging tends to offset price moves, a condition historically associated with lower realized volatility. |
| Call walls (top 3) | 645.00, 677.00, 672.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | n/a | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 645.00: 2026-11-30 100%; 677.00: 2026-11-30 100%; 672.00: 2026-11-30 100% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | n/a | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 645.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | n/a | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $1.2M | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | -$5.8K | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | $3.3K | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | n/a | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 33 calls / 0 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 645.00 (16); puts n/a | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 645 calls, 16 OI: 2026-11-30 100% (16); put wall n/a; max call OI 645 calls, 16 OI: 2026-11-30 100% (16); max put OI n/a | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 645.00: 16 calls; put wall n/a: 0 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 0.00 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | n/a | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 0.0% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 0.0% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 0.0% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 100.0% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | $17.5K net, 100.0% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-21T01:10:11+00:00)

- Call wall: 780.00 -> 645.00 (-135.00)
- Abs gamma strike: 760.00 -> 645.00 (-115.00)
- Net GEX: -$8.29B -> $17.5K (+$8.29B)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
