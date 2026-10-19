# IWM gamma exposure report

As of 2026-10-19T17:11:29+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 271.22 | The underlying price used for every calculation in this run. |
| Net GEX | -$1.18B | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 271.00, 272.00, 278.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 271.00, 270.00, 272.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 271.00: 2026-10-19 76%, 2026-10-21 10%, 2026-10-20 6%; 272.00: 2026-10-19 48%, 2026-10-20 25%, 2026-10-23 11%; 278.00: 2026-10-30 72%, 2026-10-23 12%, 2026-10-26 7% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 271.00: 2026-10-19 48%, 2026-10-30 25%, 2026-10-23 14%; 270.00: 2026-10-30 47%, 2026-10-23 17%, 2026-10-20 13%; 272.00: 2026-10-30 56%, 2026-10-23 20%, 2026-10-22 6% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 271.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 273.80 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $8.06B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $176.7M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$286.0M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±0.96 (0.4%) -> 270.26 to 272.18, exp 2026-10-19 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 568,837 calls / 928,967 puts | Open contracts across all fetched expirations and strikes. |
| OI at main walls | call wall 271.00: 7,109 calls; put wall 271.00: 34,654 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 1.63 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 2.32 vol pts (put 21.0%, call 18.6%, exp 2026-11-13) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 11.5% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 33.7% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 42.8% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 11.9% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | $0 net, 0.0% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-19T17:02:05+00:00)

- Call wall: 272.00 -> 271.00 (-1.00)
- Put wall: 271.00 -> 271.00 (+0.00)
- Zero gamma: 273.87 -> 273.80 (-0.07)
- Abs gamma strike: 271.00 -> 271.00 (+0.00)
- Net GEX: -$1.11B -> -$1.18B (-$72.3M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
