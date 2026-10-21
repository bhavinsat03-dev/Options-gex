# QQQ gamma exposure report

As of 2026-10-21T00:53:48+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 717.63 | The underlying price used for every calculation in this run. |
| Net GEX | -$2.23B | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 735.00, 720.00, 730.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 710.00, 711.00, 720.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 735.00: 2026-10-23 91%, 2026-10-26 3%, 2026-10-21 2%; 720.00: 2026-10-21 55%, 2026-10-23 31%, 2026-10-22 8%; 730.00: 2026-10-23 59%, 2026-10-21 20%, 2026-10-22 13% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 710.00: 2026-10-23 77%, 2026-10-21 14%, 2026-10-22 5%; 711.00: 2026-10-23 95%, 2026-10-21 3%, 2026-10-22 1%; 720.00: 2026-10-23 61%, 2026-10-21 22%, 2026-10-22 8% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 710.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 726.90 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $13.12B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $206.4M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$1.23B | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±7.28 (1.0%) -> 710.36 to 724.90, exp 2026-10-21 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 409,058 calls / 621,696 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 735.00 (29,256); puts 710.00 (50,354) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 735 calls, 29,256 OI: 2026-10-23 85% (24,855), 2026-10-21 9% (2,641), 2026-10-26 2% (656); put wall 710 puts, 50,354 OI: 2026-10-23 80% (40,195), 2026-10-21 11% (5,434), 2026-10-22 5% (2,284); max call OI 735 calls, 29,256 OI: 2026-10-23 85% (24,855), 2026-10-21 9% (2,641), 2026-10-26 2% (656); max put OI 710 puts, 50,354 OI: 2026-10-23 80% (40,195), 2026-10-21 11% (5,434), 2026-10-22 5% (2,284) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 735.00: 29,256 calls; put wall 710.00: 50,354 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 1.52 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 1.88 vol pts (put 21.9%, call 20.0%, exp 2026-10-27) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 0.0% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 91.3% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 8.7% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 0.0% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | $0 net, 0.0% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
