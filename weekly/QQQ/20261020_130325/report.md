# QQQ gamma exposure report

As of 2026-10-20T17:03:25+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 718.28 | The underlying price used for every calculation in this run. |
| Net GEX | -$3.86B | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 720.00, 719.00, 718.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 719.00, 718.00, 710.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 720.00: 2026-10-20 63%, 2026-10-21 21%, 2026-10-23 11%; 719.00: 2026-10-20 85%, 2026-10-23 6%, 2026-10-21 6%; 718.00: 2026-10-20 79%, 2026-10-21 12%, 2026-10-23 5% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 719.00: 2026-10-20 92%, 2026-10-23 4%, 2026-10-21 2%; 718.00: 2026-10-20 87%, 2026-10-21 6%, 2026-10-22 4%; 710.00: 2026-10-23 78%, 2026-10-21 13%, 2026-10-22 5% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 719.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 720.72 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $14.12B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $227.5M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$1.07B | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±2.85 (0.4%) -> 715.44 to 721.13, exp 2026-10-20 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 555,532 calls / 802,221 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 735.00 (35,226); puts 710.00 (57,610) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 720 calls, 15,536 OI: 2026-10-20 30% (4,678), 2026-10-23 29% (4,501), 2026-10-21 29% (4,434); put wall 719 puts, 15,187 OI: 2026-10-20 57% (8,623), 2026-10-23 23% (3,482), 2026-10-26 8% (1,234); max call OI 735 calls, 35,226 OI: 2026-10-23 71% (24,855), 2026-10-20 17% (5,970), 2026-10-21 7% (2,641); max put OI 710 puts, 57,610 OI: 2026-10-23 70% (40,195), 2026-10-20 13% (7,256), 2026-10-21 9% (5,434) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 720.00: 15,536 calls; put wall 719.00: 15,187 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 1.44 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 1.71 vol pts (put 20.5%, call 18.8%, exp 2026-10-27) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 39.5% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 55.3% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 5.2% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 0.0% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | $0 net, 0.0% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
