# META gamma exposure report

As of 2026-10-18T00:18:26+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 709.33 | The underlying price used for every calculation in this run. |
| Net GEX | $63.5M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | positive gamma | Dealer hedging tends to offset price moves, a condition historically associated with lower realized volatility. |
| Call walls (top 3) | 800.00, 750.00, 700.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 750.00, 700.00, 680.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Absolute gamma strike | 750.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 692.16 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $13.07B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $65.9M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$119.9M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±14.80 (2.1%) -> 694.53 to 724.13, exp 2026-10-19 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Put/call OI ratio | 0.69 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 0.11 vol pts (put 46.9%, call 46.8%, exp 2026-11-13) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 0.0% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 0.0% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 52.1% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 47.9% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | $130.3K net, 0.3% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
