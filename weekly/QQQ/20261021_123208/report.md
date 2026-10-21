# QQQ gamma exposure report

As of 2026-10-21T16:32:08+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 725.21 | The underlying price used for every calculation in this run. |
| Net GEX | $2.06B | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | positive gamma | Dealer hedging tends to offset price moves, a condition historically associated with lower realized volatility. |
| Call walls (top 3) | 725.00, 722.00, 726.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 710.00, 711.00, 720.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 725.00: 2026-10-21 84%, 2026-10-23 11%, 2026-10-22 3%; 722.00: 2026-10-22 67%, 2026-10-21 20%, 2026-10-23 10%; 726.00: 2026-10-21 86%, 2026-10-23 8%, 2026-10-22 4% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 710.00: 2026-10-23 89%, 2026-10-26 4%, 2026-10-22 4%; 711.00: 2026-10-23 97%, 2026-10-22 1%, 2026-10-27 1%; 720.00: 2026-10-23 73%, 2026-10-22 12%, 2026-10-26 11% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 725.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 721.57 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $15.44B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $270.2M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$884.1M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±3.13 (0.4%) -> 722.08 to 728.34, exp 2026-10-21 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 563,245 calls / 761,689 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 735.00 (32,661); puts 710.00 (60,970) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 725 calls, 17,006 OI: 2026-10-21 43% (7,375), 2026-10-23 39% (6,598), 2026-10-22 7% (1,146); put wall 710 puts, 60,970 OI: 2026-10-23 75% (45,832), 2026-10-21 13% (8,108), 2026-10-22 6% (3,452); max call OI 735 calls, 32,661 OI: 2026-10-23 78% (25,587), 2026-10-21 14% (4,534), 2026-10-22 2% (789); max put OI 710 puts, 60,970 OI: 2026-10-23 75% (45,832), 2026-10-21 13% (8,108), 2026-10-22 6% (3,452) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 725.00: 17,006 calls; put wall 710.00: 60,970 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 1.35 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 1.87 vol pts (put 21.0%, call 19.2%, exp 2026-10-28) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 28.5% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 60.7% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 10.8% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 0.0% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | $0 net, 0.0% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
