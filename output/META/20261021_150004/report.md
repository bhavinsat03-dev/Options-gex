# META gamma exposure report

As of 2026-10-21T19:00:04+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 706.68 | The underlying price used for every calculation in this run. |
| Net GEX | $135.7M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | positive gamma | Dealer hedging tends to offset price moves, a condition historically associated with lower realized volatility. |
| Call walls (top 3) | 700.00, 750.00, 800.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 750.00, 680.00, 700.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 700.00: 2026-11-20 71%, 2026-10-23 17%, 2026-10-30 7%; 750.00: 2026-11-20 45%, 2026-10-23 38%, 2026-10-30 8%; 800.00: 2026-11-20 64%, 2026-11-06 12%, 2026-10-23 11% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 750.00: 2026-10-23 81%, 2026-11-20 13%, 2026-10-30 4%; 680.00: 2026-10-30 53%, 2026-10-23 27%, 2026-11-20 13%; 700.00: 2026-10-23 38%, 2026-11-20 24%, 2026-10-30 15% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 750.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 678.90 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $14.19B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $70.9M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$302.0M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±38.27 (5.4%) -> 668.41 to 744.96, exp 2026-10-21 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 468,936 calls / 321,176 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 800.00 (42,042); puts 750.00 (16,239) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 700 calls, 26,866 OI: 2026-11-20 80% (21,627), 2026-10-23 10% (2,722), 2026-10-30 6% (1,564); put wall 750 puts, 16,239 OI: 2026-10-23 77% (12,500), 2026-11-20 16% (2,615), 2026-10-30 4% (623); max call OI 800 calls, 42,042 OI: 2026-11-20 57% (23,764), 2026-10-23 20% (8,483), 2026-11-06 11% (4,515); max put OI 750 puts, 16,239 OI: 2026-10-23 77% (12,500), 2026-11-20 16% (2,615), 2026-10-30 4% (623) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 700.00: 26,866 calls; put wall 750.00: 16,239 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 0.68 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | -0.61 vol pts (put 43.8%, call 44.4%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 1.3% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 34.9% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 17.0% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 46.8% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | $49.3K net, 0.7% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-21T16:30:50+00:00)

- Call wall: 700.00 -> 700.00 (+0.00)
- Put wall: 750.00 -> 750.00 (+0.00)
- Zero gamma: 676.14 -> 678.90 (+2.76)
- Abs gamma strike: 750.00 -> 750.00 (+0.00)
- Net GEX: $192.8M -> $135.7M (-$57.1M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
