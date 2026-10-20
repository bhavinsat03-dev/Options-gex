# SPY gamma exposure report

As of 2026-10-20T19:30:24+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 768.02 | The underlying price used for every calculation in this run. |
| Net GEX | -$12.31B | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 768.00, 770.00, 780.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 768.00, 760.00, 765.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 768.00: 2026-10-20 91%, 2026-10-23 3%, 2026-10-21 2%; 770.00: 2026-10-23 35%, 2026-10-21 19%, 2026-10-30 17%; 780.00: 2026-10-30 33%, 2026-10-23 24%, 2026-11-20 15% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 768.00: 2026-10-20 93%, 2026-10-21 3%, 2026-10-23 1%; 760.00: 2026-10-30 66%, 2026-10-23 12%, 2026-11-20 10%; 765.00: 2026-10-30 43%, 2026-10-23 24%, 2026-11-20 12% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 768.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 770.55 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $73.34B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $3.16B | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$1.87B | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±1.18 (0.2%) -> 766.84 to 769.20, exp 2026-10-20 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 2,090,634 calls / 6,079,224 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 800.00 (135,595); puts 745.00 (228,702) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 768 calls, 24,559 OI: 2026-10-20 27% (6,520), 2026-11-20 17% (4,284), 2026-10-23 15% (3,791); put wall 768 puts, 23,841 OI: 2026-11-20 21% (5,053), 2026-10-20 18% (4,307), 2026-10-23 14% (3,330); max call OI 800 calls, 135,595 OI: 2026-11-20 40% (53,605), 2026-10-30 36% (49,272), 2026-10-23 7% (9,483); max put OI 745 puts, 228,702 OI: 2026-10-30 55% (124,939), 2026-10-23 16% (37,711), 2026-11-20 14% (32,440) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 768.00: 24,559 calls; put wall 768.00: 23,841 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 2.91 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 1.96 vol pts (put 14.6%, call 12.6%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 26.0% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 25.3% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 25.1% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 23.6% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$248.1M net, 3.4% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-20T17:02:06+00:00)

- Call wall: 770.00 -> 768.00 (-2.00)
- Put wall: 760.00 -> 768.00 (+8.00)
- Zero gamma: 771.22 -> 770.55 (-0.67)
- Abs gamma strike: 769.00 -> 768.00 (-1.00)
- Net GEX: -$7.22B -> -$12.31B (-$5.08B)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
