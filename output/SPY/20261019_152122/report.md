# SPY gamma exposure report

As of 2026-10-19T19:21:22+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 768.01 | The underlying price used for every calculation in this run. |
| Net GEX | $743.5M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | positive gamma | Dealer hedging tends to offset price moves, a condition historically associated with lower realized volatility. |
| Call walls (top 3) | 768.00, 770.00, 780.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 768.00, 760.00, 769.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 768.00: 2026-10-19 97%, 2026-10-20 1%, 2026-10-23 1%; 770.00: 2026-10-23 32%, 2026-10-20 28%, 2026-10-30 16%; 780.00: 2026-10-23 39%, 2026-10-30 38%, 2026-10-22 7% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 768.00: 2026-10-19 90%, 2026-10-21 3%, 2026-10-20 3%; 760.00: 2026-10-30 65%, 2026-10-23 17%, 2026-11-06 5%; 769.00: 2026-10-23 74%, 2026-10-20 7%, 2026-10-30 6% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 768.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 767.94 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $45.81B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $1.78B | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$1.91B | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±0.99 (0.1%) -> 767.02 to 769.00, exp 2026-10-19 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 1,514,941 calls / 3,235,545 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 790.00 (81,595); puts 750.00 (173,745) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| OI at main walls | call wall 768.00: 20,443 calls; put wall 768.00: 16,697 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 2.14 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 3.20 vol pts (put 15.4%, call 12.2%, exp 2026-11-13) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 36.1% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 32.7% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 25.3% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 5.9% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | $0 net, 0.0% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-19T19:14:05+00:00)

- Call wall: 768.00 -> 768.00 (+0.00)
- Put wall: 768.00 -> 768.00 (+0.00)
- Zero gamma: 769.53 -> 767.94 (-1.59)
- Abs gamma strike: 768.00 -> 768.00 (+0.00)
- Net GEX: -$3.44B -> $743.5M (+$4.18B)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
