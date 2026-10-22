# SPY gamma exposure report

As of 2026-10-22T16:30:29+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 765.01 | The underlying price used for every calculation in this run. |
| Net GEX | -$15.03B | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 765.00, 770.00, 780.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 765.00, 760.00, 766.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 765.00: 2026-10-22 71%, 2026-10-23 14%, 2026-11-20 5%; 770.00: 2026-10-23 40%, 2026-10-30 24%, 2026-11-20 15%; 780.00: 2026-10-30 42%, 2026-11-20 22%, 2026-11-13 9% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 765.00: 2026-10-22 42%, 2026-10-23 23%, 2026-10-30 22%; 760.00: 2026-10-30 48%, 2026-10-23 22%, 2026-11-20 13%; 766.00: 2026-10-22 44%, 2026-10-26 39%, 2026-10-23 8% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 765.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 773.03 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $82.26B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $2.62B | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$2.05B | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±2.85 (0.4%) -> 762.16 to 767.86, exp 2026-10-22 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 2,152,484 calls / 5,927,332 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 800.00 (162,165); puts 750.00 (204,827) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 765 calls, 21,844 OI: 2026-11-20 33% (7,225), 2026-10-22 18% (3,928), 2026-10-30 16% (3,390); put wall 765 puts, 103,827 OI: 2026-10-30 43% (44,435), 2026-11-20 22% (22,947), 2026-10-23 15% (15,378); max call OI 800 calls, 162,165 OI: 2026-11-20 50% (81,279), 2026-10-30 30% (49,118), 2026-10-23 6% (9,453); max put OI 750 puts, 204,827 OI: 2026-11-20 40% (81,348), 2026-10-30 33% (67,250), 2026-11-06 9% (18,272) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 765.00: 21,844 calls; put wall 765.00: 103,827 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 2.75 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 2.92 vol pts (put 16.2%, call 13.3%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 12.7% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 19.6% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 36.3% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 31.3% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$312.5M net, 4.5% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-22T13:50:59+00:00)

- Call wall: 770.00 -> 765.00 (-5.00)
- Put wall: 765.00 -> 765.00 (+0.00)
- Zero gamma: 772.31 -> 773.03 (+0.72)
- Abs gamma strike: 765.00 -> 765.00 (+0.00)
- Net GEX: -$14.97B -> -$15.03B (-$60.6M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
