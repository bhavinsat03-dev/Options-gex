# TSLA gamma exposure report

As of 2026-10-19T13:44:22+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 360.98 | The underlying price used for every calculation in this run. |
| Net GEX | $169.6M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | positive gamma | Dealer hedging tends to offset price moves, a condition historically associated with lower realized volatility. |
| Call walls (top 3) | 365.00, 362.50, 370.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 350.00, 365.00, 370.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 365.00: 2026-10-19 78%, 2026-11-20 7%, 2026-10-30 5%; 362.50: 2026-10-19 98%, 2026-10-30 1%, 2026-10-26 1%; 370.00: 2026-10-19 58%, 2026-11-20 18%, 2026-10-30 9% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 350.00: 2026-10-19 67%, 2026-10-30 18%, 2026-10-28 8%; 365.00: 2026-10-19 69%, 2026-10-23 19%, 2026-10-30 11%; 370.00: 2026-10-19 56%, 2026-10-30 41%, 2026-10-28 3% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 365.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 360.41 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $3.99B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $26.5M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$724.7M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±11.07 (3.1%) -> 349.90 to 372.05, exp 2026-10-19 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Put/call OI ratio | 0.81 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | n/a | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 43.6% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 10.2% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 22.3% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 23.8% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | $40.3M net, 10.4% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-19T13:42:08+00:00)

- Call wall: 365.00 -> 365.00 (+0.00)
- Put wall: 350.00 -> 350.00 (+0.00)
- Zero gamma: 356.67 -> 360.41 (+3.74)
- Abs gamma strike: 350.00 -> 365.00 (+15.00)
- Net GEX: $87.1M -> $169.6M (+$82.5M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
