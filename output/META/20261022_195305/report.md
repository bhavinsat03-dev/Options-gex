# META gamma exposure report

As of 2026-10-22T23:53:05+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 648.85 | The underlying price used for every calculation in this run. |
| Net GEX | -$426.2M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 700.00, 650.00, 750.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 650.00, 660.00, 640.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 700.00: 2026-11-20 65%, 2026-12-18 20%, 2026-11-27 6%; 650.00: 2026-11-20 40%, 2026-12-18 30%, 2026-10-23 15%; 750.00: 2026-11-20 56%, 2026-12-18 33%, 2026-10-30 4% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 650.00: 2026-10-23 76%, 2026-11-20 8%, 2026-12-18 5%; 660.00: 2026-10-23 52%, 2026-11-20 16%, 2026-12-18 14%; 640.00: 2026-10-23 50%, 2026-12-18 19%, 2026-11-20 16% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 650.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 695.78 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $18.40B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $53.2M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | $55.9M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±14.82 (2.3%) -> 634.02 to 663.67, exp 2026-10-23 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 769,356 calls / 519,105 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 700.00 (36,458); puts 650.00 (21,124) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 700 calls, 36,458 OI: 2026-11-20 57% (20,787), 2026-12-18 21% (7,833), 2026-10-23 8% (2,993); put wall 650 puts, 21,124 OI: 2026-10-23 41% (8,676), 2026-11-20 24% (4,976), 2026-12-18 18% (3,869); max call OI 700 calls, 36,458 OI: 2026-11-20 57% (20,787), 2026-12-18 21% (7,833), 2026-10-23 8% (2,993); max put OI 650 puts, 21,124 OI: 2026-10-23 41% (8,676), 2026-11-20 24% (4,976), 2026-12-18 18% (3,869) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 700.00: 36,458 calls; put wall 650.00: 21,124 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 0.67 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | -0.39 vol pts (put 37.9%, call 38.3%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 0.0% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 29.8% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 14.1% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 56.1% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$7.4M net, 19.8% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-22T21:56:03+00:00)

- Call wall: 700.00 -> 700.00 (+0.00)
- Put wall: 650.00 -> 650.00 (+0.00)
- Zero gamma: 697.02 -> 695.78 (-1.24)
- Abs gamma strike: 650.00 -> 650.00 (+0.00)
- Net GEX: -$417.8M -> -$426.2M (-$8.4M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
