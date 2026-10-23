# AMD gamma exposure report

As of 2026-10-23T13:51:27+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 513.48 | The underlying price used for every calculation in this run. |
| Net GEX | -$150.7M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 520.00, 510.00, 600.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 510.00, 500.00, 520.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 520.00: 2026-10-23 82%, 2026-10-30 5%, 2026-11-20 5%; 510.00: 2026-10-23 68%, 2026-12-18 9%, 2026-11-20 6%; 600.00: 2026-11-20 36%, 2026-12-18 32%, 2026-10-30 12% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 510.00: 2026-10-23 65%, 2026-10-26 10%, 2026-10-30 7%; 500.00: 2026-10-23 32%, 2026-11-20 19%, 2026-10-30 15%; 520.00: 2026-10-23 60%, 2026-10-30 13%, 2026-11-20 10% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 520.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 531.03 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $8.99B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $22.3M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$214.1M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±11.90 (2.3%) -> 501.57 to 525.37, exp 2026-10-23 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 628,523 calls / 612,122 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 600.00 (27,264); puts 440.00 (24,856) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 520 calls, 11,628 OI: 2026-10-23 43% (4,960), 2026-11-20 19% (2,253), 2026-12-18 15% (1,732); put wall 510 puts, 9,964 OI: 2026-10-23 21% (2,062), 2026-11-20 17% (1,728), 2026-11-13 17% (1,676); max call OI 600 calls, 27,264 OI: 2026-11-20 23% (6,346), 2026-12-18 23% (6,181), 2026-10-23 20% (5,442); max put OI 440 puts, 24,856 OI: 2026-11-20 79% (19,685), 2026-12-18 11% (2,665), 2026-10-23 3% (864) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 520.00: 11,628 calls; put wall 510.00: 9,964 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 0.97 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 3.24 vol pts (put 63.4%, call 60.2%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 40.4% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 0.0% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 24.9% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 34.7% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$9.0M net, 9.6% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-22T23:53:05+00:00)

- Call wall: 520.00 -> 520.00 (+0.00)
- Put wall: 500.00 -> 510.00 (+10.00)
- Zero gamma: 547.11 -> 531.03 (-16.08)
- Abs gamma strike: 500.00 -> 520.00 (+20.00)
- Net GEX: -$284.5M -> -$150.7M (+$133.8M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
