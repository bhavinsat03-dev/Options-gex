# BABA gamma exposure report

As of 2026-10-18T00:44:03+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 109.11 | The underlying price used for every calculation in this run. |
| Net GEX | $11.4M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | positive gamma | Dealer hedging tends to offset price moves, a condition historically associated with lower realized volatility. |
| Call walls (top 3) | 120.00, 115.00, 110.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 110.00, 105.00, 100.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 120.00: 2026-11-20 73%, 2026-10-30 16%, 2026-10-23 6%; 115.00: 2026-10-23 61%, 2026-11-20 21%, 2026-10-30 13%; 110.00: 2026-11-20 67%, 2026-10-23 14%, 2026-10-30 14% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 110.00: 2026-11-20 67%, 2026-10-30 15%, 2026-10-23 11%; 105.00: 2026-11-20 50%, 2026-10-23 32%, 2026-10-30 11%; 100.00: 2026-11-20 70%, 2026-10-23 12%, 2026-10-30 8% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 110.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 105.65 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $624.6M | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $6.6M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$9.6M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±4.34 (4.0%) -> 104.77 to 113.46, exp 2026-10-23 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Put/call OI ratio | 0.39 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | -0.37 vol pts (put 40.1%, call 40.4%, exp 2026-11-13) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 0.0% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 0.0% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 48.2% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 51.8% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$77.6K net, 0.6% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-18T00:36:34+00:00)

- Call wall: 120.00 -> 120.00 (+0.00)
- Put wall: 110.00 -> 110.00 (+0.00)
- Zero gamma: 105.65 -> 105.65 (+0.00)
- Abs gamma strike: 110.00 -> 110.00 (+0.00)
- Net GEX: $11.4M -> $11.4M (-$980)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
