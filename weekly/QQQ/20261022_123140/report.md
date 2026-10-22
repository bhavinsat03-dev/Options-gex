# QQQ gamma exposure report

As of 2026-10-22T16:31:40+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 708.59 | The underlying price used for every calculation in this run. |
| Net GEX | -$4.74B | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 710.00, 720.00, 711.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 710.00, 711.00, 700.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 710.00: 2026-10-22 47%, 2026-10-23 37%, 2026-10-26 11%; 720.00: 2026-10-23 77%, 2026-10-26 10%, 2026-10-27 7%; 711.00: 2026-10-23 56%, 2026-10-22 36%, 2026-10-27 4% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 710.00: 2026-10-23 63%, 2026-10-22 35%, 2026-10-26 2%; 711.00: 2026-10-23 98%, 2026-10-26 0%, 2026-10-27 0%; 700.00: 2026-10-23 81%, 2026-10-26 9%, 2026-10-28 4% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 710.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 719.57 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $13.55B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $33.8M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$55.4M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±3.64 (0.5%) -> 704.95 to 712.23, exp 2026-10-22 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 574,689 calls / 836,176 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 735.00 (35,951); puts 710.00 (58,726) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 710 calls, 3,370 OI: 2026-10-23 49% (1,640), 2026-10-26 24% (820), 2026-10-22 16% (533); put wall 710 puts, 58,726 OI: 2026-10-23 79% (46,596), 2026-10-22 13% (7,910), 2026-10-26 3% (1,989); max call OI 735 calls, 35,951 OI: 2026-10-23 72% (25,886), 2026-10-22 18% (6,564), 2026-10-29 3% (1,243); max put OI 710 puts, 58,726 OI: 2026-10-23 79% (46,596), 2026-10-22 13% (7,910), 2026-10-26 3% (1,989) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 710.00: 3,370 calls; put wall 710.00: 58,726 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 1.46 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 1.43 vol pts (put 26.4%, call 24.9%, exp 2026-10-29) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 11.5% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 68.9% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 19.6% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 0.0% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | $0 net, 0.0% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
