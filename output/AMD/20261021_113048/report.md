# AMD gamma exposure report

As of 2026-10-21T15:30:48+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 546.88 | The underlying price used for every calculation in this run. |
| Net GEX | $98.2M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | positive gamma | Dealer hedging tends to offset price moves, a condition historically associated with lower realized volatility. |
| Call walls (top 3) | 550.00, 545.00, 547.50 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 545.00, 550.00, 540.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 550.00: 2026-10-21 68%, 2026-10-23 22%, 2026-11-20 5%; 545.00: 2026-10-21 70%, 2026-10-23 23%, 2026-10-30 3%; 547.50: 2026-10-21 67%, 2026-10-23 32%, 2026-10-26 0% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 545.00: 2026-10-21 72%, 2026-10-23 17%, 2026-10-30 7%; 550.00: 2026-10-23 29%, 2026-10-21 24%, 2026-11-20 23%; 540.00: 2026-10-23 36%, 2026-10-21 30%, 2026-10-30 13% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 550.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 542.57 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $7.79B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $36.2M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$250.0M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±7.42 (1.4%) -> 539.46 to 554.31, exp 2026-10-21 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 416,704 calls / 416,720 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 620.00 (27,084); puts 440.00 (21,430) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 550 calls, 12,608 OI: 2026-10-23 34% (4,259), 2026-11-20 28% (3,549), 2026-10-21 23% (2,899); put wall 545 puts, 4,811 OI: 2026-10-23 30% (1,455), 2026-10-30 26% (1,249), 2026-10-21 24% (1,139); max call OI 620 calls, 27,084 OI: 2026-11-20 42% (11,450), 2026-10-30 27% (7,325), 2026-10-23 18% (4,920); max put OI 440 puts, 21,430 OI: 2026-11-20 90% (19,372), 2026-10-23 3% (615), 2026-11-06 2% (525) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 550.00: 12,608 calls; put wall 545.00: 4,811 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 1.00 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | -0.82 vol pts (put 59.2%, call 60.0%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 26.9% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 32.7% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 16.3% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 24.1% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$1.3M net, 0.9% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-21T13:48:32+00:00)

- Call wall: 550.00 -> 550.00 (+0.00)
- Put wall: 540.00 -> 545.00 (+5.00)
- Zero gamma: 545.98 -> 542.57 (-3.41)
- Abs gamma strike: 550.00 -> 550.00 (+0.00)
- Net GEX: -$43.2M -> $98.2M (+$141.4M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
