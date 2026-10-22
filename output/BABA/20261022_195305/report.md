# BABA gamma exposure report

As of 2026-10-22T23:53:05+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 101.82 | The underlying price used for every calculation in this run. |
| Net GEX | -$37.1M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 100.00, 110.00, 120.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 100.00, 105.00, 104.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 100.00: 2026-12-18 85%, 2026-11-20 7%, 2026-10-30 4%; 110.00: 2026-11-20 40%, 2026-12-18 30%, 2026-10-30 22%; 120.00: 2026-11-20 50%, 2026-12-18 40%, 2026-10-30 5% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 100.00: 2026-12-18 50%, 2026-10-23 20%, 2026-11-20 19%; 105.00: 2026-12-18 30%, 2026-11-20 27%, 2026-10-23 25%; 104.00: 2026-10-23 89%, 2026-10-30 9%, 2026-11-13 1% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 100.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 106.61 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $1.57B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $3.5M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | $6.7M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±2.04 (2.0%) -> 99.78 to 103.85, exp 2026-10-23 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 487,627 calls / 273,106 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 120.00 (47,657); puts 100.00 (50,839) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 100 calls, 31,113 OI: 2026-12-18 92% (28,726), 2026-11-20 5% (1,597), 2026-10-30 2% (521); put wall 100 puts, 50,839 OI: 2026-12-18 69% (34,852), 2026-11-20 19% (9,701), 2026-10-23 5% (2,527); max call OI 120 calls, 47,657 OI: 2026-11-20 43% (20,304), 2026-12-18 32% (15,252), 2026-10-30 12% (5,907); max put OI 100 puts, 50,839 OI: 2026-12-18 69% (34,852), 2026-11-20 19% (9,701), 2026-10-23 5% (2,527) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 100.00: 31,113 calls; put wall 100.00: 50,839 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 0.56 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | -2.11 vol pts (put 42.4%, call 44.5%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 0.0% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 24.9% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 17.3% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 57.7% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$10.0M net, 34.0% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-22T21:56:03+00:00)

- Call wall: 110.00 -> 100.00 (-10.00)
- Put wall: 104.00 -> 100.00 (-4.00)
- Zero gamma: 105.78 -> 106.61 (+0.83)
- Abs gamma strike: 104.00 -> 100.00 (-4.00)
- Net GEX: -$26.9M -> -$37.1M (-$10.1M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
