# TSLA gamma exposure report

As of 2026-10-19T13:56:52+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 362.55 | The underlying price used for every calculation in this run. |
| Net GEX | $161.6M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | positive gamma | Dealer hedging tends to offset price moves, a condition historically associated with lower realized volatility. |
| Call walls (top 3) | 362.50, 365.00, 400.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 360.00, 350.00, 365.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 362.50: 2026-10-19 90%, 2026-10-23 9%, 2026-10-30 1%; 365.00: 2026-10-19 74%, 2026-10-23 13%, 2026-11-20 5%; 400.00: 2026-11-20 30%, 2026-12-18 21%, 2026-10-23 20% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 360.00: 2026-10-19 62%, 2026-10-23 11%, 2026-12-18 8%; 350.00: 2026-12-18 28%, 2026-11-20 28%, 2026-10-23 16%; 365.00: 2026-10-19 64%, 2026-10-23 12%, 2026-10-30 7% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 365.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 359.80 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $10.72B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $54.1M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$285.2M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±5.74 (1.6%) -> 356.81 to 368.28, exp 2026-10-19 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Put/call OI ratio | 0.81 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 4.41 vol pts (put 48.8%, call 44.4%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 26.9% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 21.9% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 12.1% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 39.1% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$6.8M net, 15.5% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-19T13:44:22+00:00)

- Call wall: 365.00 -> 362.50 (-2.50)
- Put wall: 350.00 -> 360.00 (+10.00)
- Zero gamma: 360.41 -> 359.80 (-0.61)
- Abs gamma strike: 365.00 -> 365.00 (+0.00)
- Net GEX: $169.6M -> $161.6M (-$7.9M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
