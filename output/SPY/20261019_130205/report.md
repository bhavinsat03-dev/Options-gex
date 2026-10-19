# SPY gamma exposure report

As of 2026-10-19T17:02:05+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 767.49 | The underlying price used for every calculation in this run. |
| Net GEX | -$4.79B | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 768.00, 767.00, 770.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 767.00, 768.00, 760.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 768.00: 2026-10-19 87%, 2026-10-20 4%, 2026-10-23 3%; 767.00: 2026-10-19 84%, 2026-10-20 5%, 2026-10-30 2%; 770.00: 2026-10-23 30%, 2026-10-20 22%, 2026-10-30 16% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 767.00: 2026-10-19 83%, 2026-10-23 6%, 2026-10-20 3%; 768.00: 2026-10-19 75%, 2026-10-21 7%, 2026-10-20 7%; 760.00: 2026-10-30 64%, 2026-10-23 17%, 2026-11-06 5% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 767.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 769.14 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $46.04B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $1.84B | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$2.35B | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±2.21 (0.3%) -> 765.28 to 769.70, exp 2026-10-19 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 1,514,940 calls / 3,235,545 puts | Open contracts across all fetched expirations and strikes. |
| OI at main walls | call wall 768.00: 20,443 calls; put wall 767.00: 26,841 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 2.14 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 2.82 vol pts (put 15.4%, call 12.6%, exp 2026-11-13) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 27.0% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 36.6% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 29.5% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 6.8% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | $0 net, 0.0% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-19T16:33:15+00:00)

- Call wall: 768.00 -> 768.00 (+0.00)
- Put wall: 768.00 -> 767.00 (-1.00)
- Zero gamma: 769.13 -> 769.14 (+0.01)
- Abs gamma strike: 768.00 -> 767.00 (-1.00)
- Net GEX: -$3.41B -> -$4.79B (-$1.38B)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
