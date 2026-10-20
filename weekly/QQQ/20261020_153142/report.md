# QQQ gamma exposure report

As of 2026-10-20T19:31:42+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 717.82 | The underlying price used for every calculation in this run. |
| Net GEX | -$3.48B | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 718.00, 720.00, 717.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 718.00, 710.00, 711.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 718.00: 2026-10-20 91%, 2026-10-21 6%, 2026-10-23 2%; 720.00: 2026-10-21 58%, 2026-10-23 29%, 2026-10-22 8%; 717.00: 2026-10-20 77%, 2026-10-23 13%, 2026-10-21 7% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 718.00: 2026-10-20 93%, 2026-10-21 3%, 2026-10-22 2%; 710.00: 2026-10-23 78%, 2026-10-21 13%, 2026-10-22 5%; 711.00: 2026-10-23 95%, 2026-10-21 3%, 2026-10-22 1% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 718.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 719.91 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $15.34B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $208.7M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$882.2M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±1.76 (0.2%) -> 716.06 to 719.58, exp 2026-10-20 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 555,532 calls / 802,221 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 735.00 (35,226); puts 710.00 (57,610) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 718 calls, 5,592 OI: 2026-10-20 36% (1,999), 2026-10-21 26% (1,479), 2026-10-23 22% (1,249); put wall 718 puts, 9,662 OI: 2026-10-20 37% (3,589), 2026-10-23 20% (1,918), 2026-10-22 19% (1,855); max call OI 735 calls, 35,226 OI: 2026-10-23 71% (24,855), 2026-10-20 17% (5,970), 2026-10-21 7% (2,641); max put OI 710 puts, 57,610 OI: 2026-10-23 70% (40,195), 2026-10-20 13% (7,256), 2026-10-21 9% (5,434) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 718.00: 5,592 calls; put wall 718.00: 9,662 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 1.44 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 2.64 vol pts (put 20.6%, call 18.0%, exp 2026-10-27) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 33.1% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 61.1% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 5.8% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 0.0% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | $0 net, 0.0% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
