# MU gamma exposure report

As of 2026-10-21T16:30:50+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 910.05 | The underlying price used for every calculation in this run. |
| Net GEX | -$8.0M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 910.00, 900.00, 915.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 910.00, 900.00, 905.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 910.00: 2026-10-21 70%, 2026-11-20 16%, 2026-10-23 9%; 900.00: 2026-10-21 55%, 2026-10-23 18%, 2026-11-20 13%; 915.00: 2026-10-21 73%, 2026-10-23 21%, 2026-10-30 2% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 910.00: 2026-10-21 85%, 2026-10-23 7%, 2026-11-20 3%; 900.00: 2026-10-23 50%, 2026-11-20 18%, 2026-10-30 10%; 905.00: 2026-10-21 67%, 2026-10-23 14%, 2026-10-30 10% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 910.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 910.72 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $14.01B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $62.6M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$187.0M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±11.00 (1.2%) -> 899.05 to 921.05, exp 2026-10-21 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 493,042 calls / 523,017 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 1,000.00 (23,637); puts 850.00 (20,962) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 910 calls, 11,238 OI: 2026-11-20 64% (7,202), 2026-10-21 14% (1,559), 2026-10-23 10% (1,153); put wall 910 puts, 5,983 OI: 2026-11-20 29% (1,735), 2026-10-21 26% (1,545), 2026-10-23 19% (1,131); max call OI 1000 calls, 23,637 OI: 2026-10-23 29% (6,972), 2026-11-20 25% (5,967), 2026-10-30 20% (4,758); max put OI 850 puts, 20,962 OI: 2026-11-20 33% (6,994), 2026-10-23 25% (5,180), 2026-10-21 14% (2,842) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 910.00: 11,238 calls; put wall 910.00: 5,983 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 1.06 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | -2.01 vol pts (put 49.6%, call 51.7%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 27.5% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 25.7% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 19.4% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 27.4% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$16.4M net, 2.4% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-21T15:30:48+00:00)

- Call wall: 910.00 -> 910.00 (+0.00)
- Put wall: 910.00 -> 910.00 (+0.00)
- Zero gamma: 906.82 -> 910.72 (+3.90)
- Abs gamma strike: 910.00 -> 910.00 (+0.00)
- Net GEX: $42.9M -> -$8.0M (-$51.0M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
