# META gamma exposure report

As of 2026-10-19T13:38:14+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 701.56 | The underlying price used for every calculation in this run. |
| Net GEX | $10.3M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | positive gamma | Dealer hedging tends to offset price moves, a condition historically associated with lower realized volatility. |
| Call walls (top 3) | 800.00, 700.00, 750.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 700.00, 750.00, 680.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 800.00: 2026-11-20 48%, 2026-12-18 22%, 2026-10-23 13%; 700.00: 2026-11-20 64%, 2026-12-18 18%, 2026-10-19 9%; 750.00: 2026-11-20 38%, 2026-10-23 28%, 2026-12-18 18% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 700.00: 2026-10-19 48%, 2026-12-18 16%, 2026-10-23 15%; 750.00: 2026-10-23 72%, 2026-11-20 12%, 2026-12-18 10%; 680.00: 2026-10-30 42%, 2026-10-23 26%, 2026-10-19 10% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 700.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 700.48 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $20.05B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $77.7M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$746.5M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±16.55 (2.4%) -> 685.00 to 718.11, exp 2026-10-19 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Put/call OI ratio | 0.66 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | -6.58 vol pts (put 48.2%, call 54.8%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 17.1% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 22.8% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 9.8% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 50.3% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | $47.4M net, 17.8% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-18T00:44:03+00:00)

- Call wall: 800.00 -> 800.00 (+0.00)
- Put wall: 750.00 -> 700.00 (-50.00)
- Zero gamma: 692.30 -> 700.48 (+8.18)
- Abs gamma strike: 750.00 -> 700.00 (-50.00)
- Net GEX: $63.1M -> $10.3M (-$52.8M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
