# QQQ gamma exposure report

As of 2026-10-20T22:32:22+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 717.63 | The underlying price used for every calculation in this run. |
| Net GEX | -$6.51B | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 720.00, 730.00, 740.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 720.00, 710.00, 700.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 720.00: 2026-10-21 32%, 2026-11-20 29%, 2026-10-23 16%; 730.00: 2026-10-23 30%, 2026-11-20 25%, 2026-10-30 20%; 740.00: 2026-10-30 57%, 2026-11-20 19%, 2026-10-23 10% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 720.00: 2026-10-23 28%, 2026-11-20 24%, 2026-10-30 18%; 710.00: 2026-10-23 50%, 2026-10-30 15%, 2026-11-06 12%; 700.00: 2026-10-30 50%, 2026-11-20 23%, 2026-10-23 11% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 720.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 732.95 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $67.96B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $1.28B | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$1.58B | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±7.28 (1.0%) -> 710.36 to 724.91, exp 2026-10-21 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 1,743,135 calls / 2,832,195 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 760.00 (91,158); puts 700.00 (208,401) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 720 calls, 49,768 OI: 2026-11-20 55% (27,621), 2026-10-30 12% (5,906), 2026-10-23 9% (4,501); put wall 720 puts, 127,139 OI: 2026-11-20 43% (54,516), 2026-10-30 20% (24,960), 2026-10-23 14% (18,085); max call OI 760 calls, 91,158 OI: 2026-11-20 35% (32,188), 2026-11-06 28% (25,189), 2026-10-30 19% (16,872); max put OI 700 puts, 208,401 OI: 2026-10-30 43% (89,790), 2026-11-20 29% (60,395), 2026-10-23 9% (17,729) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 720.00: 49,768 calls; put wall 720.00: 127,139 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 1.62 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 3.46 vol pts (put 23.3%, call 19.9%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 0.0% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 34.0% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 27.9% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 38.1% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$98.5M net, 3.1% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-20T19:30:24+00:00)

- Call wall: 720.00 -> 720.00 (+0.00)
- Put wall: 717.00 -> 720.00 (+3.00)
- Zero gamma: 724.20 -> 732.95 (+8.75)
- Abs gamma strike: 717.00 -> 720.00 (+3.00)
- Net GEX: -$9.59B -> -$6.51B (+$3.08B)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
