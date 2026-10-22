# IWM gamma exposure report

As of 2026-10-22T19:00:50+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 275.65 | The underlying price used for every calculation in this run. |
| Net GEX | -$1.78B | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 280.00, 278.00, 276.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 270.00, 277.00, 275.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 280.00: 2026-10-29 27%, 2026-10-23 24%, 2026-11-20 17%; 278.00: 2026-10-30 51%, 2026-10-23 34%, 2026-10-26 7%; 276.00: 2026-10-22 44%, 2026-10-23 40%, 2026-10-30 4% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 270.00: 2026-11-20 64%, 2026-10-30 20%, 2026-11-06 8%; 277.00: 2026-10-23 90%, 2026-11-20 5%, 2026-10-30 1%; 275.00: 2026-10-23 40%, 2026-11-20 37%, 2026-10-30 10% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 270.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 279.40 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $18.92B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $523.5M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$549.2M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±0.73 (0.3%) -> 274.92 to 276.38, exp 2026-10-22 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 1,108,443 calls / 2,282,247 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 280.00 (74,796); puts 270.00 (241,008) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 280 calls, 74,796 OI: 2026-11-20 24% (17,588), 2026-10-29 20% (15,170), 2026-10-23 20% (15,135); put wall 270 puts, 241,008 OI: 2026-11-20 70% (168,381), 2026-10-30 14% (33,986), 2026-11-06 7% (16,546); max call OI 280 calls, 74,796 OI: 2026-11-20 24% (17,588), 2026-10-29 20% (15,170), 2026-10-23 20% (15,135); max put OI 270 puts, 241,008 OI: 2026-11-20 70% (168,381), 2026-10-30 14% (33,986), 2026-11-06 7% (16,546) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 280.00: 74,796 calls; put wall 270.00: 241,008 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 2.06 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 2.09 vol pts (put 22.0%, call 19.9%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 2.0% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 23.1% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 28.6% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 46.3% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | $17.8M net, 0.8% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-22T16:30:29+00:00)

- Call wall: 280.00 -> 280.00 (+0.00)
- Put wall: 270.00 -> 270.00 (+0.00)
- Zero gamma: 279.33 -> 279.40 (+0.07)
- Abs gamma strike: 277.00 -> 270.00 (-7.00)
- Net GEX: -$1.52B -> -$1.78B (-$263.2M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
