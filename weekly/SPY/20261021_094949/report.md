# SPY gamma exposure report

As of 2026-10-21T13:49:49+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 771.17 | The underlying price used for every calculation in this run. |
| Net GEX | $1.65B | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | positive gamma | Dealer hedging tends to offset price moves, a condition historically associated with lower realized volatility. |
| Call walls (top 3) | 770.00, 773.00, 771.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 769.00, 770.00, 766.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 770.00: 2026-10-21 56%, 2026-10-23 26%, 2026-10-22 12%; 773.00: 2026-10-21 70%, 2026-10-23 14%, 2026-10-22 11%; 771.00: 2026-10-21 74%, 2026-10-23 14%, 2026-10-22 6% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 769.00: 2026-10-23 65%, 2026-10-21 26%, 2026-10-22 5%; 770.00: 2026-10-21 52%, 2026-10-23 29%, 2026-10-22 8%; 766.00: 2026-10-26 64%, 2026-10-21 15%, 2026-10-23 10% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 770.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 769.85 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $17.03B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $552.2M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$2.12B | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±3.24 (0.4%) -> 767.93 to 774.41, exp 2026-10-21 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 736,626 calls / 1,162,793 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 790.00 (45,816); puts 745.00 (48,110) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 770 calls, 28,306 OI: 2026-10-23 45% (12,696), 2026-10-21 27% (7,735), 2026-10-22 14% (3,901); put wall 769 puts, 40,820 OI: 2026-10-23 76% (30,902), 2026-10-21 12% (5,101), 2026-10-22 4% (1,709); max call OI 790 calls, 45,816 OI: 2026-10-23 79% (36,043), 2026-10-22 5% (2,336), 2026-10-26 5% (2,112); max put OI 745 puts, 48,110 OI: 2026-10-23 79% (38,052), 2026-10-21 7% (3,265), 2026-10-22 6% (2,993) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 770.00: 28,306 calls; put wall 769.00: 40,820 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 1.58 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 3.23 vol pts (put 14.2%, call 11.0%, exp 2026-10-28) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 34.2% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 49.7% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 16.1% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 0.0% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | $0 net, 0.0% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
