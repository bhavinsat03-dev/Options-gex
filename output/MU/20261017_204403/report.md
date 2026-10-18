# MU gamma exposure report

As of 2026-10-18T00:44:03+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 878.84 | The underlying price used for every calculation in this run. |
| Net GEX | -$220.9M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 900.00, 1,000.00, 910.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 900.00, 850.00, 950.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 900.00: 2026-11-20 29%, 2026-10-19 22%, 2026-10-23 18%; 1,000.00: 2026-11-20 38%, 2026-10-23 29%, 2026-10-30 17%; 910.00: 2026-11-20 69%, 2026-10-19 13%, 2026-10-23 5% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 900.00: 2026-10-23 37%, 2026-11-20 26%, 2026-10-30 11%; 850.00: 2026-11-20 48%, 2026-10-23 19%, 2026-10-30 11%; 950.00: 2026-11-20 30%, 2026-10-30 27%, 2026-10-23 25% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 900.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 936.72 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $12.90B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $28.9M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$95.3M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±29.65 (3.4%) -> 849.19 to 908.49, exp 2026-10-19 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Put/call OI ratio | 0.95 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 2.93 vol pts (put 54.9%, call 51.9%, exp 2026-11-13) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 0.0% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 0.0% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 59.4% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 40.6% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$11.3M net, 2.5% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-18T00:36:34+00:00)

- Call wall: 900.00 -> 900.00 (+0.00)
- Put wall: 900.00 -> 900.00 (+0.00)
- Zero gamma: 936.74 -> 936.72 (-0.02)
- Abs gamma strike: 900.00 -> 900.00 (+0.00)
- Net GEX: -$220.7M -> -$220.9M (-$135.8K)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
