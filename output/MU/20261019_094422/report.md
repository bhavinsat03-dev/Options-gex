# MU gamma exposure report

As of 2026-10-19T13:44:22+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 912.44 | The underlying price used for every calculation in this run. |
| Net GEX | $65.1M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | positive gamma | Dealer hedging tends to offset price moves, a condition historically associated with lower realized volatility. |
| Call walls (top 3) | 1,000.00, 900.00, 910.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 900.00, 880.00, 840.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 1,000.00: 2026-11-20 52%, 2026-12-18 48%, 2026-10-30 0%; 900.00: 2026-11-20 64%, 2026-12-18 36%; 910.00: 2026-11-20 100% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 900.00: 2026-12-18 99%, 2026-10-23 1%, 2026-11-13 0%; 880.00: 2026-12-18 99%, 2026-11-20 1%, 2026-11-27 0%; 840.00: 2026-12-18 100%, 2026-10-30 0%, 2026-11-20 0% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 900.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 911.12 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $2.14B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $7.8M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$9.4M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±107.64 (11.8%) -> 804.80 to 1,020.08, exp 2026-10-19 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Put/call OI ratio | 1.13 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | n/a | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 0.1% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 2.6% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 0.8% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 96.5% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | $14.8M net, 42.4% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-19T13:42:08+00:00)

- Call wall: 900.00 -> 1,000.00 (+100.00)
- Put wall: 900.00 -> 900.00 (+0.00)
- Zero gamma: 910.70 -> 911.12 (+0.42)
- Abs gamma strike: 900.00 -> 900.00 (+0.00)
- Net GEX: $125.9M -> $65.1M (-$60.8M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
