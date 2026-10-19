# SPCX gamma exposure report

As of 2026-10-19T13:44:22+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 148.70 | The underlying price used for every calculation in this run. |
| Net GEX | -$14.7M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 150.00, 155.00, 149.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 140.00, 150.00, 145.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 150.00: 2026-10-19 42%, 2026-11-20 20%, 2026-12-18 16%; 155.00: 2026-10-23 29%, 2026-11-20 20%, 2026-10-21 17%; 149.00: 2026-10-19 77%, 2026-10-23 13%, 2026-10-21 7% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 140.00: 2026-11-20 24%, 2026-12-18 24%, 2026-10-23 24%; 150.00: 2026-11-20 31%, 2026-12-18 25%, 2026-10-19 20%; 145.00: 2026-10-23 23%, 2026-11-20 20%, 2026-12-18 15% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 150.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 149.02 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $4.64B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $19.3M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$131.5M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±3.62 (2.4%) -> 145.08 to 152.32, exp 2026-10-19 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Put/call OI ratio | 1.07 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 1.10 vol pts (put 60.0%, call 58.9%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 19.2% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 27.4% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 14.1% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 39.4% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$14.9M net, 13.6% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-19T13:42:08+00:00)

- Call wall: 150.00 -> 150.00 (+0.00)
- Put wall: 148.00 -> 140.00 (-8.00)
- Zero gamma: 149.39 -> 149.02 (-0.37)
- Abs gamma strike: 150.00 -> 150.00 (+0.00)
- Net GEX: $5.3M -> -$14.7M (-$20.0M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
