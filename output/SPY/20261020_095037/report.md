# SPY gamma exposure report

As of 2026-10-20T13:50:37+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 766.10 | The underlying price used for every calculation in this run. |
| Net GEX | -$11.12B | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 766.00, 770.00, 768.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 760.00, 765.00, 750.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 766.00: 2026-10-20 83%, 2026-10-23 5%, 2026-10-21 3%; 770.00: 2026-10-23 31%, 2026-10-30 17%, 2026-10-21 14%; 768.00: 2026-10-20 61%, 2026-10-23 11%, 2026-10-21 9% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 760.00: 2026-10-30 63%, 2026-10-23 13%, 2026-11-20 9%; 765.00: 2026-10-20 40%, 2026-10-30 27%, 2026-10-23 14%; 750.00: 2026-10-30 41%, 2026-11-20 32%, 2026-10-23 9% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 765.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 771.68 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $81.63B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $3.03B | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$3.15B | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±3.18 (0.4%) -> 762.92 to 769.28, exp 2026-10-20 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 2,090,639 calls / 6,079,224 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 800.00 (135,595); puts 745.00 (228,702) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 766 calls, 17,208 OI: 2026-10-20 37% (6,384), 2026-10-23 14% (2,366), 2026-10-30 13% (2,165); put wall 760 puts, 214,367 OI: 2026-10-30 61% (130,192), 2026-11-20 14% (30,725), 2026-10-23 8% (17,116); max call OI 800 calls, 135,595 OI: 2026-11-20 40% (53,605), 2026-10-30 36% (49,272), 2026-10-23 7% (9,483); max put OI 745 puts, 228,702 OI: 2026-10-30 55% (124,939), 2026-10-23 16% (37,711), 2026-11-20 14% (32,440) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 766.00: 17,208 calls; put wall 760.00: 214,367 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 2.91 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 3.50 vol pts (put 16.2%, call 12.7%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 16.8% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 28.0% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 28.5% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 26.7% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$260.4M net, 3.9% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-20T01:26:50+00:00)

- Call wall: 770.00 -> 766.00 (-4.00)
- Put wall: 750.00 -> 760.00 (+10.00)
- Zero gamma: 773.76 -> 771.68 (-2.08)
- Abs gamma strike: 760.00 -> 765.00 (+5.00)
- Net GEX: -$8.83B -> -$11.12B (-$2.29B)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
