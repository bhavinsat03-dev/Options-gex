# SPCX gamma exposure report

As of 2026-10-19T19:21:22+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 147.07 | The underlying price used for every calculation in this run. |
| Net GEX | -$60.5M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 147.00, 150.00, 155.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 147.00, 140.00, 150.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 147.00: 2026-10-19 93%, 2026-10-23 3%, 2026-11-13 1%; 150.00: 2026-11-20 34%, 2026-12-18 26%, 2026-10-23 14%; 155.00: 2026-10-23 27%, 2026-12-18 20%, 2026-11-20 19% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 147.00: 2026-10-19 95%, 2026-10-21 2%, 2026-10-23 2%; 140.00: 2026-10-23 25%, 2026-11-20 24%, 2026-12-18 23%; 150.00: 2026-11-20 29%, 2026-12-18 24%, 2026-10-30 19% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 147.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 148.58 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $5.46B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $16.7M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$13.8M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±0.91 (0.6%) -> 146.16 to 147.99, exp 2026-10-19 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 931,825 calls / 995,503 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 150.00 (55,090); puts 140.00 (77,471) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| OI at main walls | call wall 147.00: 8,377 calls; put wall 147.00: 6,551 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 1.07 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | -0.68 vol pts (put 57.3%, call 58.0%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 27.3% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 23.9% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 12.2% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 36.6% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$15.5M net, 13.1% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-19T19:14:05+00:00)

- Call wall: 147.00 -> 147.00 (+0.00)
- Put wall: 147.00 -> 147.00 (+0.00)
- Zero gamma: 148.56 -> 148.58 (+0.02)
- Abs gamma strike: 147.00 -> 147.00 (+0.00)
- Net GEX: -$116.8M -> -$60.5M (+$56.3M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
