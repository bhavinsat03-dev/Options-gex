# SPY gamma exposure report

As of 2026-10-19T17:11:29+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 767.30 | The underlying price used for every calculation in this run. |
| Net GEX | -$5.36B | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 768.00, 767.00, 770.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 767.00, 760.00, 768.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 768.00: 2026-10-19 86%, 2026-10-20 5%, 2026-10-23 4%; 767.00: 2026-10-19 85%, 2026-10-20 5%, 2026-10-30 2%; 770.00: 2026-10-23 32%, 2026-10-20 23%, 2026-10-30 17% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 767.00: 2026-10-19 87%, 2026-10-23 5%, 2026-10-20 2%; 760.00: 2026-10-30 64%, 2026-10-23 17%, 2026-11-06 4%; 768.00: 2026-10-19 70%, 2026-10-21 9%, 2026-10-20 8% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 767.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 769.11 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $46.28B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $1.83B | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$2.54B | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±2.03 (0.3%) -> 765.27 to 769.33, exp 2026-10-19 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 1,514,940 calls / 3,235,545 puts | Open contracts across all fetched expirations and strikes. |
| OI at main walls | call wall 768.00: 20,443 calls; put wall 767.00: 26,841 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 2.14 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 2.95 vol pts (put 15.5%, call 12.5%, exp 2026-11-13) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 27.6% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 36.3% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 29.3% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 6.8% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | $0 net, 0.0% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-19T17:02:05+00:00)

- Call wall: 768.00 -> 768.00 (+0.00)
- Put wall: 767.00 -> 767.00 (+0.00)
- Zero gamma: 769.14 -> 769.11 (-0.03)
- Abs gamma strike: 767.00 -> 767.00 (+0.00)
- Net GEX: -$4.79B -> -$5.36B (-$567.7M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
