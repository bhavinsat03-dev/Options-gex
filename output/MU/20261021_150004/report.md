# MU gamma exposure report

As of 2026-10-21T19:00:04+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 911.18 | The underlying price used for every calculation in this run. |
| Net GEX | -$82.0M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 910.00, 915.00, 900.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 910.00, 900.00, 850.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 910.00: 2026-10-21 78%, 2026-11-20 12%, 2026-10-23 6%; 915.00: 2026-10-21 80%, 2026-10-23 16%, 2026-10-30 1%; 900.00: 2026-10-21 38%, 2026-10-23 25%, 2026-11-20 17% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 910.00: 2026-10-21 91%, 2026-10-23 4%, 2026-11-20 2%; 900.00: 2026-10-23 54%, 2026-11-20 19%, 2026-10-30 11%; 850.00: 2026-11-20 37%, 2026-10-23 26%, 2026-10-30 13% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 910.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 911.68 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $13.16B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $66.1M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$281.5M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±11.38 (1.2%) -> 899.79 to 922.56, exp 2026-10-21 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 493,042 calls / 523,017 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 1,000.00 (23,637); puts 850.00 (20,962) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 910 calls, 11,238 OI: 2026-11-20 64% (7,202), 2026-10-21 14% (1,559), 2026-10-23 10% (1,153); put wall 910 puts, 5,983 OI: 2026-11-20 29% (1,735), 2026-10-21 26% (1,545), 2026-10-23 19% (1,131); max call OI 1000 calls, 23,637 OI: 2026-10-23 29% (6,972), 2026-11-20 25% (5,967), 2026-10-30 20% (4,758); max put OI 850 puts, 20,962 OI: 2026-11-20 33% (6,994), 2026-10-23 25% (5,180), 2026-10-21 14% (2,842) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 910.00: 11,238 calls; put wall 910.00: 5,983 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 1.06 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | -2.94 vol pts (put 49.4%, call 52.3%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 30.1% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 24.4% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 18.8% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 26.7% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$17.0M net, 2.4% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-21T16:30:50+00:00)

- Call wall: 910.00 -> 910.00 (+0.00)
- Put wall: 910.00 -> 910.00 (+0.00)
- Zero gamma: 910.72 -> 911.68 (+0.96)
- Abs gamma strike: 910.00 -> 910.00 (+0.00)
- Net GEX: -$8.0M -> -$82.0M (-$74.0M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
