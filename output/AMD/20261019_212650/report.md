# AMD gamma exposure report

As of 2026-10-20T01:26:50+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 538.05 | The underlying price used for every calculation in this run. |
| Net GEX | -$61.8M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 620.00, 550.00, 600.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 550.00, 530.00, 500.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 620.00: 2026-11-20 53%, 2026-10-30 29%, 2026-10-23 8%; 550.00: 2026-10-23 49%, 2026-11-20 22%, 2026-10-21 13%; 600.00: 2026-11-20 40%, 2026-10-23 22%, 2026-10-30 20% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 550.00: 2026-11-20 32%, 2026-10-23 30%, 2026-10-30 20%; 530.00: 2026-10-23 36%, 2026-11-20 19%, 2026-10-30 15%; 500.00: 2026-11-20 35%, 2026-10-23 26%, 2026-10-30 19% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 550.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 553.19 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $7.08B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $27.5M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$107.0M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±19.47 (3.6%) -> 518.57 to 557.52, exp 2026-10-21 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 353,098 calls / 367,679 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 620.00 (25,923); puts 440.00 (20,933) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 620 calls, 25,923 OI: 2026-11-20 43% (11,269), 2026-10-30 28% (7,145), 2026-10-23 19% (4,894); put wall 550 puts, 11,927 OI: 2026-11-20 49% (5,845), 2026-10-23 18% (2,094), 2026-10-30 17% (2,021); max call OI 620 calls, 25,923 OI: 2026-11-20 43% (11,269), 2026-10-30 28% (7,145), 2026-10-23 19% (4,894); max put OI 440 puts, 20,933 OI: 2026-11-20 92% (19,296), 2026-10-23 4% (780), 2026-11-06 2% (316) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 620.00: 25,923 calls; put wall 550.00: 11,927 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 1.04 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 0.47 vol pts (put 58.7%, call 58.2%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 0.0% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 48.6% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 17.4% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 34.0% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$3.3M net, 1.1% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-20T01:21:36+00:00)

- Call wall: 620.00 -> 620.00 (+0.00)
- Put wall: 550.00 -> 550.00 (+0.00)
- Zero gamma: 553.19 -> 553.19 (+0.00)
- Abs gamma strike: 550.00 -> 550.00 (+0.00)
- Net GEX: -$61.7M -> -$61.8M (-$25.5K)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
