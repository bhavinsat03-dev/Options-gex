# QQQ gamma exposure report

As of 2026-10-19T13:42:08+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 719.30 | The underlying price used for every calculation in this run. |
| Net GEX | -$968.6M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 720.00, 721.00, 722.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 720.00, 710.00, 715.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 720.00: 2026-10-19 71%, 2026-10-20 15%, 2026-10-23 8%; 721.00: 2026-10-19 88%, 2026-10-20 5%, 2026-10-23 4%; 722.00: 2026-10-19 76%, 2026-10-20 10%, 2026-10-23 7% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 720.00: 2026-10-19 52%, 2026-10-23 21%, 2026-11-06 7%; 710.00: 2026-10-23 58%, 2026-11-06 19%, 2026-10-21 7%; 715.00: 2026-10-19 72%, 2026-11-06 10%, 2026-10-22 6% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 720.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 721.19 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $27.13B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $401.5M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$1.18B | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±4.76 (0.7%) -> 714.54 to 724.06, exp 2026-10-19 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Put/call OI ratio | 1.69 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 4.82 vol pts (put 24.7%, call 19.9%, exp 2026-11-13) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 32.3% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 48.2% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 5.0% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 14.5% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | $0 net, 0.0% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-19T13:38:14+00:00)

- Call wall: 720.00 -> 720.00 (+0.00)
- Put wall: 720.00 -> 720.00 (+0.00)
- Zero gamma: 725.64 -> 721.19 (-4.45)
- Abs gamma strike: 720.00 -> 720.00 (+0.00)
- Net GEX: -$3.76B -> -$968.6M (+$2.79B)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
