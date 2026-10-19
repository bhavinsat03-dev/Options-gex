# AMD gamma exposure report

As of 2026-10-19T21:59:34+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 538.05 | The underlying price used for every calculation in this run. |
| Net GEX | -$65.6M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 550.00, 620.00, 600.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 550.00, 500.00, 530.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 550.00: 2026-10-23 45%, 2026-11-20 19%, 2026-10-21 12%; 620.00: 2026-11-20 51%, 2026-10-30 26%, 2026-12-18 8%; 600.00: 2026-11-20 32%, 2026-12-18 25%, 2026-10-30 16% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 550.00: 2026-10-23 28%, 2026-11-20 28%, 2026-10-30 18%; 500.00: 2026-11-20 28%, 2026-10-23 20%, 2026-12-18 19%; 530.00: 2026-10-23 35%, 2026-11-20 17%, 2026-10-30 14% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 550.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 552.40 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $8.69B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $31.5M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$91.4M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±19.47 (3.6%) -> 518.57 to 557.52, exp 2026-10-21 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 565,327 calls / 582,418 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 620.00 (27,930); puts 440.00 (23,513) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| OI at main walls | call wall 550.00: 10,497 calls; put wall 550.00: 14,363 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 1.03 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 0.45 vol pts (put 57.8%, call 57.4%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 0.0% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 44.1% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 15.5% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 40.4% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$1.1M net, 10.9% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-19T19:21:22+00:00)

- Call wall: 540.00 -> 550.00 (+10.00)
- Put wall: 540.00 -> 550.00 (+10.00)
- Zero gamma: 542.11 -> 552.40 (+10.29)
- Abs gamma strike: 540.00 -> 550.00 (+10.00)
- Net GEX: -$62.8M -> -$65.6M (-$2.7M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
