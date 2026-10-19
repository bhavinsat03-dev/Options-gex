# QQQ gamma exposure report

As of 2026-10-19T13:38:14+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 718.69 | The underlying price used for every calculation in this run. |
| Net GEX | -$3.76B | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 720.00, 715.00, 717.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 720.00, 715.00, 710.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 720.00: 2026-10-19 64%, 2026-10-20 15%, 2026-10-23 9%; 715.00: 2026-10-19 77%, 2026-10-23 10%, 2026-10-20 5%; 717.00: 2026-10-19 81%, 2026-10-20 8%, 2026-10-23 6% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 720.00: 2026-10-19 43%, 2026-10-30 19%, 2026-10-23 17%; 715.00: 2026-10-19 47%, 2026-10-30 26%, 2026-10-23 11%; 710.00: 2026-10-23 42%, 2026-10-30 18%, 2026-11-06 14% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 720.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 725.64 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $47.90B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $785.6M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$1.37B | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±4.77 (0.7%) -> 713.93 to 723.46, exp 2026-10-19 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Put/call OI ratio | 1.69 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 5.02 vol pts (put 24.8%, call 19.8%, exp 2026-11-13) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 26.4% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 36.6% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 26.6% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 10.4% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | $0 net, 0.0% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-18T00:44:03+00:00)

- Call wall: 760.00 -> 720.00 (-40.00)
- Put wall: 700.00 -> 720.00 (+20.00)
- Zero gamma: 738.72 -> 725.64 (-13.08)
- Abs gamma strike: 700.00 -> 720.00 (+20.00)
- Net GEX: -$6.57B -> -$3.76B (+$2.81B)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
