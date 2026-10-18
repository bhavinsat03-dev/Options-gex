# AMD gamma exposure report

As of 2026-10-18T00:44:03+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 528.75 | The underlying price used for every calculation in this run. |
| Net GEX | -$139.5M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 620.00, 600.00, 520.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 550.00, 530.00, 540.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 620.00: 2026-11-20 53%, 2026-10-30 27%, 2026-10-23 9%; 600.00: 2026-11-20 42%, 2026-10-23 20%, 2026-10-30 18%; 520.00: 2026-10-23 63%, 2026-11-20 22%, 2026-10-19 5% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 550.00: 2026-11-20 31%, 2026-10-23 28%, 2026-10-30 18%; 530.00: 2026-10-23 26%, 2026-10-19 23%, 2026-11-20 23%; 540.00: 2026-10-23 26%, 2026-10-30 21%, 2026-11-20 19% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 550.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 579.56 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $7.28B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $16.6M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$29.8M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±17.27 (3.3%) -> 511.48 to 546.02, exp 2026-10-19 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Put/call OI ratio | 1.02 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 1.29 vol pts (put 62.6%, call 61.4%, exp 2026-11-13) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 0.0% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 0.0% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 63.1% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 36.9% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$1.4M net, 0.7% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-18T00:36:34+00:00)

- Call wall: 620.00 -> 620.00 (+0.00)
- Put wall: 550.00 -> 550.00 (+0.00)
- Zero gamma: 579.57 -> 579.56 (-0.01)
- Abs gamma strike: 550.00 -> 550.00 (+0.00)
- Net GEX: -$139.4M -> -$139.5M (-$57.0K)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
