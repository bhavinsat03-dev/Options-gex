# BABA gamma exposure report

As of 2026-10-19T13:44:22+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 109.75 | The underlying price used for every calculation in this run. |
| Net GEX | -$251.3K | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 130.00, 125.00, 110.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 100.00, 105.00, 130.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 130.00: 2026-11-20 89%, 2026-10-30 8%, 2026-12-18 3%; 125.00: 2026-11-20 87%, 2026-10-30 10%, 2026-11-06 4%; 110.00: 2026-11-20 100% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 100.00: 2026-12-18 96%, 2026-10-30 4%, 2026-10-23 0%; 105.00: 2026-12-18 80%, 2026-10-30 15%, 2026-11-06 5%; 130.00: 2026-12-18 85%, 2026-11-20 15%, 2026-10-30 0% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 100.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 109.78 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $523.7M | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $3.4M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$3.0M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | n/a | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Put/call OI ratio | 0.56 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | -5.26 vol pts (put 56.8%, call 62.0%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 0.0% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 2.7% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 14.8% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 82.5% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$6.9M net, 40.4% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-19T13:42:08+00:00)

- Call wall: 120.00 -> 130.00 (+10.00)
- Put wall: 100.00 -> 100.00 (+0.00)
- Zero gamma: 109.40 -> 109.78 (+0.38)
- Abs gamma strike: 100.00 -> 100.00 (+0.00)
- Net GEX: $1.8M -> -$251.3K (-$2.1M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
