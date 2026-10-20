# QQQ gamma exposure report

As of 2026-10-20T13:50:37+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 712.63 | The underlying price used for every calculation in this run. |
| Net GEX | -$8.47B | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 720.00, 730.00, 740.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 710.00, 700.00, 715.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 720.00: 2026-11-20 33%, 2026-10-21 21%, 2026-10-23 15%; 730.00: 2026-11-20 29%, 2026-10-23 25%, 2026-10-30 22%; 740.00: 2026-10-30 56%, 2026-11-20 21%, 2026-10-23 9% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 710.00: 2026-10-23 37%, 2026-10-20 23%, 2026-10-30 11%; 700.00: 2026-10-30 45%, 2026-11-20 21%, 2026-10-23 13%; 715.00: 2026-10-20 47%, 2026-10-30 20%, 2026-10-23 13% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 710.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 726.53 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $75.99B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $1.07B | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$1.30B | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±5.13 (0.7%) -> 707.50 to 717.76, exp 2026-10-20 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 1,743,135 calls / 2,832,195 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 760.00 (91,745); puts 700.00 (220,085) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 720 calls, 54,446 OI: 2026-11-20 51% (27,621), 2026-10-30 11% (5,906), 2026-10-20 9% (4,678); put wall 710 puts, 121,029 OI: 2026-10-23 33% (40,195), 2026-11-06 18% (22,257), 2026-10-30 18% (21,613); max call OI 760 calls, 91,745 OI: 2026-11-20 35% (32,188), 2026-11-06 27% (25,189), 2026-10-30 18% (16,872); max put OI 700 puts, 220,085 OI: 2026-10-30 41% (89,790), 2026-11-20 27% (60,395), 2026-10-23 8% (17,729) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 720.00: 54,446 calls; put wall 710.00: 121,029 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 1.62 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 4.79 vol pts (put 24.8%, call 20.1%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 12.2% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 28.6% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 25.2% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 33.9% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$117.8M net, 2.8% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-20T01:26:50+00:00)

- Call wall: 720.00 -> 720.00 (+0.00)
- Put wall: 700.00 -> 710.00 (+10.00)
- Zero gamma: 732.91 -> 726.53 (-6.38)
- Abs gamma strike: 720.00 -> 710.00 (-10.00)
- Net GEX: -$5.13B -> -$8.47B (-$3.34B)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
