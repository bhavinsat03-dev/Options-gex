# QQQ gamma exposure report

As of 2026-10-22T13:52:14+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 712.09 | The underlying price used for every calculation in this run. |
| Net GEX | -$5.27B | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 720.00, 722.00, 715.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 710.00, 711.00, 715.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 720.00: 2026-10-23 73%, 2026-10-22 10%, 2026-10-26 8%; 722.00: 2026-10-23 37%, 2026-10-22 35%, 2026-10-26 14%; 715.00: 2026-10-23 56%, 2026-10-22 33%, 2026-10-26 5% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 710.00: 2026-10-23 69%, 2026-10-22 27%, 2026-10-26 2%; 711.00: 2026-10-23 89%, 2026-10-22 10%, 2026-10-26 0%; 715.00: 2026-10-22 47%, 2026-10-23 45%, 2026-10-26 4% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 710.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 721.16 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $14.29B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $113.5M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$913.4M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±5.81 (0.8%) -> 706.28 to 717.90, exp 2026-10-22 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 574,689 calls / 836,176 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 735.00 (35,951); puts 710.00 (58,726) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 720 calls, 8,747 OI: 2026-10-23 62% (5,419), 2026-10-22 16% (1,431), 2026-10-26 8% (733); put wall 710 puts, 58,726 OI: 2026-10-23 79% (46,596), 2026-10-22 13% (7,910), 2026-10-26 3% (1,989); max call OI 735 calls, 35,951 OI: 2026-10-23 72% (25,886), 2026-10-22 18% (6,564), 2026-10-29 3% (1,243); max put OI 710 puts, 58,726 OI: 2026-10-23 79% (46,596), 2026-10-22 13% (7,910), 2026-10-26 3% (1,989) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 720.00: 8,747 calls; put wall 710.00: 58,726 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 1.46 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 0.78 vol pts (put 25.4%, call 24.6%, exp 2026-10-29) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 21.6% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 60.4% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 18.0% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 0.0% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | $0 net, 0.0% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
