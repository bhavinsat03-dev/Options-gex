# AMD gamma exposure report

As of 2026-10-23T19:01:06+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 516.99 | The underlying price used for every calculation in this run. |
| Net GEX | -$125.4M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 517.50, 515.00, 520.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 517.50, 500.00, 550.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 517.50: 2026-10-23 98%, 2026-10-26 2%; 515.00: 2026-10-23 85%, 2026-10-26 8%, 2026-10-30 3%; 520.00: 2026-10-23 56%, 2026-10-30 13%, 2026-11-20 10% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 517.50: 2026-10-23 99%, 2026-10-26 1%, 2026-10-28 0%; 500.00: 2026-11-20 27%, 2026-10-30 24%, 2026-10-26 15%; 550.00: 2026-11-20 49%, 2026-10-30 21%, 2026-12-18 14% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 517.50 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 518.15 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $9.06B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $24.0M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$51.6M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±3.70 (0.7%) -> 513.29 to 520.69, exp 2026-10-23 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 628,523 calls / 612,122 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 620.00 (29,735); puts 440.00 (24,856) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 517.5 calls, 989 OI: 2026-10-23 80% (788), 2026-10-26 20% (201); put wall 517.5 puts, 1,050 OI: 2026-10-23 81% (847), 2026-10-26 17% (176), 2026-10-28 3% (27); max call OI 620 calls, 29,735 OI: 2026-11-20 39% (11,516), 2026-10-30 25% (7,573), 2026-10-23 17% (5,171); max put OI 440 puts, 24,856 OI: 2026-11-20 79% (19,685), 2026-12-18 11% (2,665), 2026-10-23 3% (864) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 517.50: 989 calls; put wall 517.50: 1,050 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 0.97 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 0.79 vol pts (put 61.0%, call 60.2%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 30.8% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 0.0% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 28.8% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 40.4% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$9.2M net, 10.9% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-23T16:30:16+00:00)

- Call wall: 520.00 -> 517.50 (-2.50)
- Put wall: 520.00 -> 517.50 (-2.50)
- Zero gamma: 518.92 -> 518.15 (-0.77)
- Abs gamma strike: 520.00 -> 517.50 (-2.50)
- Net GEX: $25.3M -> -$125.4M (-$150.7M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
