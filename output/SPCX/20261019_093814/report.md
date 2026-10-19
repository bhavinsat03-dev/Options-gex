# SPCX gamma exposure report

As of 2026-10-19T13:38:14+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 149.03 | The underlying price used for every calculation in this run. |
| Net GEX | $2.7M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | positive gamma | Dealer hedging tends to offset price moves, a condition historically associated with lower realized volatility. |
| Call walls (top 3) | 155.00, 150.00, 152.50 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 148.00, 145.00, 146.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 155.00: 2026-12-18 96%, 2026-11-20 2%, 2026-10-30 2%; 150.00: 2026-10-26 42%, 2026-10-28 38%, 2026-10-23 20%; 152.50: 2026-10-23 80%, 2026-11-06 18%, 2026-10-30 2% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 148.00: 2026-10-28 70%, 2026-10-30 29%, 2026-10-23 0%; 145.00: 2026-11-20 89%, 2026-11-13 4%, 2026-10-23 4%; 146.00: 2026-10-23 82%, 2026-11-06 14%, 2026-10-30 3% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 155.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 148.93 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $1.8M | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $4.4M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$531.8K | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | n/a | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Put/call OI ratio | 1.07 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | n/a | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 0.0% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 11.7% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 37.0% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 51.3% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | $2.2M net, 38.7% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-18T00:44:03+00:00)

- Call wall: 150.00 -> 155.00 (+5.00)
- Put wall: 148.00 -> 148.00 (+0.00)
- Zero gamma: 153.60 -> 148.93 (-4.67)
- Abs gamma strike: 150.00 -> 155.00 (+5.00)
- Net GEX: -$46.0M -> $2.7M (+$48.7M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
