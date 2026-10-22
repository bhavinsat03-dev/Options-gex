# AMD gamma exposure report

As of 2026-10-22T16:30:29+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 513.00 | The underlying price used for every calculation in this run. |
| Net GEX | -$248.7M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 520.00, 550.00, 600.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 500.00, 520.00, 510.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 520.00: 2026-10-23 77%, 2026-11-20 13%, 2026-11-06 3%; 550.00: 2026-11-20 40%, 2026-10-23 25%, 2026-10-30 17%; 600.00: 2026-11-20 56%, 2026-10-30 18%, 2026-11-06 13% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 500.00: 2026-10-23 53%, 2026-11-20 17%, 2026-10-30 14%; 520.00: 2026-10-23 70%, 2026-10-30 12%, 2026-11-20 9%; 510.00: 2026-10-23 66%, 2026-10-30 12%, 2026-11-13 8% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 520.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 541.07 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $6.92B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $14.2M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$97.1M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±16.10 (3.1%) -> 496.91 to 529.11, exp 2026-10-23 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 399,815 calls / 401,605 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 600.00 (18,620); puts 440.00 (21,223) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 520 calls, 5,169 OI: 2026-10-23 43% (2,214), 2026-11-20 38% (1,975), 2026-11-13 7% (368); put wall 500 puts, 16,946 OI: 2026-11-20 36% (6,098), 2026-10-23 27% (4,606), 2026-10-30 15% (2,536); max call OI 600 calls, 18,620 OI: 2026-11-20 33% (6,130), 2026-10-23 32% (5,898), 2026-10-30 17% (3,081); max put OI 440 puts, 21,223 OI: 2026-11-20 92% (19,471), 2026-10-23 3% (549), 2026-11-06 3% (547) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 520.00: 5,169 calls; put wall 500.00: 16,946 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 1.00 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | -1.85 vol pts (put 61.2%, call 63.1%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 0.0% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 40.6% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 23.8% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 35.6% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$3.1M net, 1.5% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-22T13:50:59+00:00)

- Call wall: 520.00 -> 520.00 (+0.00)
- Put wall: 500.00 -> 500.00 (+0.00)
- Zero gamma: 546.25 -> 541.07 (-5.18)
- Abs gamma strike: 520.00 -> 520.00 (+0.00)
- Net GEX: -$177.1M -> -$248.7M (-$71.6M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
