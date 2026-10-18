# QQQ gamma exposure report

As of 2026-10-18T00:44:03+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 709.80 | The underlying price used for every calculation in this run. |
| Net GEX | -$6.57B | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 760.00, 750.00, 740.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 700.00, 715.00, 720.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 760.00: 2026-11-20 53%, 2026-11-06 27%, 2026-10-30 14%; 750.00: 2026-11-20 54%, 2026-10-30 17%, 2026-10-23 15%; 740.00: 2026-10-30 52%, 2026-11-20 21%, 2026-10-23 15% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 700.00: 2026-10-30 53%, 2026-11-20 22%, 2026-10-19 10%; 715.00: 2026-10-30 70%, 2026-10-19 7%, 2026-11-20 5%; 720.00: 2026-11-20 30%, 2026-10-30 22%, 2026-10-23 15% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 700.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 738.72 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $70.61B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $683.6M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$450.4M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±9.86 (1.4%) -> 699.94 to 719.66, exp 2026-10-19 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Put/call OI ratio | 1.66 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 6.80 vol pts (put 27.0%, call 20.2%, exp 2026-11-13) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 0.0% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 0.0% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 62.1% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 37.9% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | $0 net, 0.0% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-18T00:36:34+00:00)

- Call wall: 760.00 -> 760.00 (+0.00)
- Put wall: 700.00 -> 700.00 (+0.00)
- Zero gamma: 738.72 -> 738.72 (+0.00)
- Abs gamma strike: 700.00 -> 700.00 (+0.00)
- Net GEX: -$6.57B -> -$6.57B (-$2.9M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
