# QQQ gamma exposure report

As of 2026-10-20T13:57:35+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 714.92 | The underlying price used for every calculation in this run. |
| Net GEX | -$6.24B | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 720.00, 715.00, 730.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 700.00, 710.00, 720.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 720.00: 2026-11-20 30%, 2026-10-21 24%, 2026-10-23 16%; 715.00: 2026-10-20 59%, 2026-10-23 17%, 2026-10-21 6%; 730.00: 2026-11-20 28%, 2026-10-23 25%, 2026-10-30 22% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 700.00: 2026-10-30 45%, 2026-11-20 21%, 2026-10-23 12%; 710.00: 2026-10-23 39%, 2026-10-20 17%, 2026-10-30 13%; 720.00: 2026-11-20 26%, 2026-10-23 19%, 2026-10-30 17% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 720.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 724.67 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $74.53B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $1.22B | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$1.10B | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±6.13 (0.9%) -> 708.79 to 721.06, exp 2026-10-20 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 1,743,135 calls / 2,832,195 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 760.00 (91,745); puts 700.00 (220,085) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 720 calls, 54,446 OI: 2026-11-20 51% (27,621), 2026-10-30 11% (5,906), 2026-10-20 9% (4,678); put wall 700 puts, 220,085 OI: 2026-10-30 41% (89,790), 2026-11-20 27% (60,395), 2026-10-23 8% (17,729); max call OI 760 calls, 91,745 OI: 2026-11-20 35% (32,188), 2026-11-06 27% (25,189), 2026-10-30 18% (16,872); max put OI 700 puts, 220,085 OI: 2026-10-30 41% (89,790), 2026-11-20 27% (60,395), 2026-10-23 8% (17,729) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 720.00: 54,446 calls; put wall 700.00: 220,085 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 1.62 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 7.96 vol pts (put 26.6%, call 18.7%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 13.9% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 27.7% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 24.5% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 33.9% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$81.3M net, 2.9% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-20T13:50:37+00:00)

- Call wall: 720.00 -> 720.00 (+0.00)
- Put wall: 710.00 -> 700.00 (-10.00)
- Zero gamma: 726.53 -> 724.67 (-1.86)
- Abs gamma strike: 710.00 -> 720.00 (+10.00)
- Net GEX: -$8.47B -> -$6.24B (+$2.23B)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
