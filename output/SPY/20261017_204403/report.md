# SPY gamma exposure report

As of 2026-10-18T00:44:03+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 763.25 | The underlying price used for every calculation in this run. |
| Net GEX | -$10.03B | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 770.00, 775.00, 780.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 760.00, 745.00, 765.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 770.00: 2026-10-30 27%, 2026-10-23 23%, 2026-11-20 19%; 775.00: 2026-10-30 28%, 2026-10-23 19%, 2026-11-20 18%; 780.00: 2026-10-30 36%, 2026-11-20 25%, 2026-10-23 17% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 760.00: 2026-10-30 56%, 2026-11-20 14%, 2026-10-23 10%; 745.00: 2026-10-30 49%, 2026-10-23 26%, 2026-11-20 16%; 765.00: 2026-10-30 49%, 2026-11-20 15%, 2026-10-19 11% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 760.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 775.78 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $69.60B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $2.20B | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$1.85B | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±6.24 (0.8%) -> 757.01 to 769.49, exp 2026-10-19 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Put/call OI ratio | 3.09 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 4.83 vol pts (put 17.6%, call 12.8%, exp 2026-11-13) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 0.0% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 0.0% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 69.1% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 30.9% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | $0 net, 0.0% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-18T00:36:34+00:00)

- Call wall: 770.00 -> 770.00 (+0.00)
- Put wall: 760.00 -> 760.00 (+0.00)
- Zero gamma: 775.79 -> 775.78 (-0.01)
- Abs gamma strike: 760.00 -> 760.00 (+0.00)
- Net GEX: -$10.03B -> -$10.03B (-$3.6M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
