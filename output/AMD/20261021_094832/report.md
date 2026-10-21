# AMD gamma exposure report

As of 2026-10-21T13:48:32+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 543.50 | The underlying price used for every calculation in this run. |
| Net GEX | -$43.2M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 550.00, 560.00, 620.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 540.00, 545.00, 550.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 550.00: 2026-10-21 53%, 2026-10-23 31%, 2026-11-20 8%; 560.00: 2026-10-23 60%, 2026-10-21 21%, 2026-10-30 7%; 620.00: 2026-11-20 51%, 2026-10-30 33%, 2026-11-06 6% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 540.00: 2026-10-21 51%, 2026-10-23 26%, 2026-10-30 9%; 545.00: 2026-10-21 68%, 2026-10-23 20%, 2026-10-30 7%; 550.00: 2026-10-23 39%, 2026-11-20 29%, 2026-10-30 20% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 550.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 545.98 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $6.99B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $37.7M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$388.1M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±14.27 (2.6%) -> 529.23 to 557.77, exp 2026-10-21 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 416,704 calls / 416,720 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 620.00 (27,084); puts 440.00 (21,430) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 550 calls, 12,608 OI: 2026-10-23 34% (4,259), 2026-11-20 28% (3,549), 2026-10-21 23% (2,899); put wall 540 puts, 9,516 OI: 2026-11-20 27% (2,572), 2026-10-23 24% (2,237), 2026-10-30 17% (1,623); max call OI 620 calls, 27,084 OI: 2026-11-20 42% (11,450), 2026-10-30 27% (7,325), 2026-10-23 18% (4,920); max put OI 440 puts, 21,430 OI: 2026-11-20 90% (19,372), 2026-10-23 3% (615), 2026-11-06 2% (525) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 550.00: 12,608 calls; put wall 540.00: 9,516 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 1.00 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | -8.93 vol pts (put 55.6%, call 64.5%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 25.1% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 31.9% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 16.8% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 26.2% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$2.0M net, 1.0% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-21T01:10:11+00:00)

- Call wall: 550.00 -> 550.00 (+0.00)
- Put wall: 550.00 -> 540.00 (-10.00)
- Zero gamma: 548.69 -> 545.98 (-2.71)
- Abs gamma strike: 550.00 -> 550.00 (+0.00)
- Net GEX: -$90.9M -> -$43.2M (+$47.7M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
