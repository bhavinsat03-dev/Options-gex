# MU gamma exposure report

As of 2026-10-21T15:30:48+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 910.98 | The underlying price used for every calculation in this run. |
| Net GEX | $42.9M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | positive gamma | Dealer hedging tends to offset price moves, a condition historically associated with lower realized volatility. |
| Call walls (top 3) | 910.00, 900.00, 920.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 910.00, 900.00, 850.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 910.00: 2026-10-21 69%, 2026-11-20 16%, 2026-10-23 9%; 900.00: 2026-10-21 47%, 2026-10-23 22%, 2026-11-20 14%; 920.00: 2026-10-21 64%, 2026-10-23 22%, 2026-10-30 5% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 910.00: 2026-10-21 78%, 2026-10-23 10%, 2026-11-20 5%; 900.00: 2026-10-23 44%, 2026-11-20 17%, 2026-10-21 15%; 850.00: 2026-11-20 36%, 2026-10-23 29%, 2026-10-30 13% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 910.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 906.82 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $14.82B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $62.9M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$300.2M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±12.25 (1.3%) -> 898.73 to 923.23, exp 2026-10-21 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 493,039 calls / 522,982 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 1,000.00 (23,637); puts 850.00 (20,962) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 910 calls, 11,238 OI: 2026-11-20 64% (7,202), 2026-10-21 14% (1,559), 2026-10-23 10% (1,153); put wall 910 puts, 5,983 OI: 2026-11-20 29% (1,735), 2026-10-21 26% (1,545), 2026-10-23 19% (1,131); max call OI 1000 calls, 23,637 OI: 2026-10-23 29% (6,972), 2026-11-20 25% (5,967), 2026-10-30 20% (4,758); max put OI 850 puts, 20,962 OI: 2026-11-20 33% (6,994), 2026-10-23 25% (5,180), 2026-10-21 14% (2,842) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 910.00: 11,238 calls; put wall 910.00: 5,983 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 1.06 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | -0.21 vol pts (put 50.7%, call 51.0%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 26.0% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 26.9% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 19.6% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 27.5% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$15.5M net, 2.4% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-21T13:48:32+00:00)

- Call wall: 900.00 -> 910.00 (+10.00)
- Put wall: 900.00 -> 910.00 (+10.00)
- Zero gamma: 907.93 -> 906.82 (-1.11)
- Abs gamma strike: 900.00 -> 910.00 (+10.00)
- Net GEX: -$101.6M -> $42.9M (+$144.5M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
