# IWM gamma exposure report

As of 2026-10-19T16:05:44+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 271.79 | The underlying price used for every calculation in this run. |
| Net GEX | -$2.28B | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 272.00, 275.00, 278.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 272.00, 270.00, 271.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 272.00: 2026-10-19 75%, 2026-10-20 11%, 2026-10-23 6%; 275.00: 2026-10-23 24%, 2026-10-21 20%, 2026-10-22 14%; 278.00: 2026-10-30 70%, 2026-10-23 13%, 2026-10-26 8% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 272.00: 2026-10-19 86%, 2026-10-30 8%, 2026-10-23 3%; 270.00: 2026-10-30 50%, 2026-10-23 18%, 2026-10-20 11%; 271.00: 2026-10-30 44%, 2026-10-23 24%, 2026-10-19 9% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 272.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 273.78 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $7.85B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $162.2M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | $68.3M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±0.94 (0.3%) -> 270.85 to 272.73, exp 2026-10-19 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 568,837 calls / 928,967 puts | Open contracts across all fetched expirations and strikes. |
| OI at main walls | call wall 272.00: 11,176 calls; put wall 272.00: 66,005 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 1.63 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 1.24 vol pts (put 20.0%, call 18.7%, exp 2026-11-13) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 39.0% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 22.7% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 29.9% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 8.3% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | $0 net, 0.0% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-19T15:31:23+00:00)

- Call wall: 272.00 -> 272.00 (+0.00)
- Put wall: 272.00 -> 272.00 (+0.00)
- Zero gamma: 274.41 -> 273.78 (-0.63)
- Abs gamma strike: 272.00 -> 272.00 (+0.00)
- Net GEX: -$1.69B -> -$2.28B (-$597.4M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
