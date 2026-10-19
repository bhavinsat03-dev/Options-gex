# TSLA gamma exposure report

As of 2026-10-19T13:42:08+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 359.65 | The underlying price used for every calculation in this run. |
| Net GEX | $87.1M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | positive gamma | Dealer hedging tends to offset price moves, a condition historically associated with lower realized volatility. |
| Call walls (top 3) | 365.00, 370.00, 350.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 350.00, 365.00, 340.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 365.00: 2026-10-19 75%, 2026-11-20 9%, 2026-10-30 7%; 370.00: 2026-10-19 50%, 2026-11-20 20%, 2026-12-18 10%; 350.00: 2026-11-20 55%, 2026-12-18 18%, 2026-10-19 17% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 350.00: 2026-10-19 43%, 2026-11-20 25%, 2026-10-23 14%; 365.00: 2026-10-19 62%, 2026-10-23 17%, 2026-10-30 10%; 340.00: 2026-11-20 36%, 2026-10-23 28%, 2026-10-30 21% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 350.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 356.67 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $6.99B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $20.2M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$638.4M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±8.10 (2.3%) -> 351.55 to 367.75, exp 2026-10-19 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Put/call OI ratio | 0.81 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | -2.66 vol pts (put 50.7%, call 53.4%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 36.2% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 10.9% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 18.2% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 34.7% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | $52.2M net, 12.9% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-19T13:38:14+00:00)

- Call wall: 360.00 -> 365.00 (+5.00)
- Put wall: 350.00 -> 350.00 (+0.00)
- Zero gamma: 354.43 -> 356.67 (+2.24)
- Abs gamma strike: 360.00 -> 350.00 (-10.00)
- Net GEX: $61.4M -> $87.1M (+$25.6M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
