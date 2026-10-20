# QQQ gamma exposure report

As of 2026-10-20T19:30:24+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 716.94 | The underlying price used for every calculation in this run. |
| Net GEX | -$9.59B | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 720.00, 717.00, 716.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 717.00, 720.00, 710.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 720.00: 2026-11-20 30%, 2026-10-21 30%, 2026-10-23 16%; 717.00: 2026-10-20 84%, 2026-10-23 7%, 2026-10-21 3%; 716.00: 2026-10-20 86%, 2026-10-21 5%, 2026-10-23 4% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 717.00: 2026-10-20 94%, 2026-11-06 2%, 2026-10-21 2%; 720.00: 2026-10-23 28%, 2026-11-20 25%, 2026-10-30 19%; 710.00: 2026-10-23 49%, 2026-10-30 15%, 2026-11-06 12% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 717.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 724.20 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $68.29B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $1.27B | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$952.3M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±2.11 (0.3%) -> 714.83 to 719.05, exp 2026-10-20 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 1,743,135 calls / 2,832,195 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 760.00 (91,745); puts 700.00 (220,085) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 720 calls, 54,446 OI: 2026-11-20 51% (27,621), 2026-10-30 11% (5,906), 2026-10-20 9% (4,678); put wall 717 puts, 25,382 OI: 2026-11-06 41% (10,301), 2026-10-20 19% (4,807), 2026-10-30 10% (2,527); max call OI 760 calls, 91,745 OI: 2026-11-20 35% (32,188), 2026-11-06 27% (25,189), 2026-10-30 18% (16,872); max put OI 700 puts, 220,085 OI: 2026-10-30 41% (89,790), 2026-11-20 27% (60,395), 2026-10-23 8% (17,729) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 720.00: 54,446 calls; put wall 717.00: 25,382 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 1.62 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 3.54 vol pts (put 23.2%, call 19.7%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 21.2% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 26.7% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 22.0% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 30.1% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$101.2M net, 2.5% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-20T17:02:06+00:00)

- Call wall: 720.00 -> 720.00 (+0.00)
- Put wall: 720.00 -> 717.00 (-3.00)
- Zero gamma: 724.66 -> 724.20 (-0.46)
- Abs gamma strike: 720.00 -> 717.00 (-3.00)
- Net GEX: -$7.56B -> -$9.59B (-$2.03B)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
