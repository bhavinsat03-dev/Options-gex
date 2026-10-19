# META gamma exposure report

As of 2026-10-19T19:21:22+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 706.21 | The underlying price used for every calculation in this run. |
| Net GEX | $115.9M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | positive gamma | Dealer hedging tends to offset price moves, a condition historically associated with lower realized volatility. |
| Call walls (top 3) | 800.00, 700.00, 750.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 705.00, 750.00, 707.50 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 800.00: 2026-11-20 50%, 2026-12-18 24%, 2026-10-23 10%; 700.00: 2026-11-20 69%, 2026-12-18 20%, 2026-10-23 8%; 750.00: 2026-11-20 41%, 2026-10-23 28%, 2026-12-18 19% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 705.00: 2026-10-19 82%, 2026-10-23 8%, 2026-10-30 5%; 750.00: 2026-10-23 73%, 2026-11-20 12%, 2026-12-18 9%; 707.50: 2026-10-19 98%, 2026-10-23 2%, 2026-10-30 0% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 705.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 702.98 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $19.17B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $92.5M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$118.9M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±3.12 (0.4%) -> 703.09 to 709.34, exp 2026-10-19 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 669,034 calls / 440,544 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 800.00 (51,793); puts 750.00 (19,144) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| OI at main walls | call wall 800.00: 51,793 calls; put wall 705.00: 5,111 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 0.66 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | -0.45 vol pts (put 43.4%, call 43.9%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 10.9% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 23.1% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 10.3% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 55.7% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | $72.2M net, 20.0% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-19T19:14:05+00:00)

- Call wall: 705.00 -> 800.00 (+95.00)
- Put wall: 705.00 -> 705.00 (+0.00)
- Zero gamma: 703.47 -> 702.98 (-0.49)
- Abs gamma strike: 705.00 -> 705.00 (+0.00)
- Net GEX: $92.0M -> $115.9M (+$23.9M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
