# AMD gamma exposure report

As of 2026-10-21T19:00:04+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 552.98 | The underlying price used for every calculation in this run. |
| Net GEX | $186.0M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | positive gamma | Dealer hedging tends to offset price moves, a condition historically associated with lower realized volatility. |
| Call walls (top 3) | 550.00, 555.00, 552.50 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 550.00, 540.00, 560.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 550.00: 2026-10-21 72%, 2026-10-23 19%, 2026-11-20 4%; 555.00: 2026-10-21 71%, 2026-10-23 25%, 2026-10-30 2%; 552.50: 2026-10-21 93%, 2026-10-23 6%, 2026-10-26 1% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 550.00: 2026-10-23 38%, 2026-11-20 28%, 2026-10-30 19%; 540.00: 2026-10-23 49%, 2026-10-30 19%, 2026-11-20 16%; 560.00: 2026-11-20 38%, 2026-10-23 38%, 2026-10-30 14% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 550.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 543.35 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $7.70B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $32.3M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | $288.1M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±6.81 (1.2%) -> 546.16 to 559.78, exp 2026-10-21 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 416,704 calls / 416,720 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 620.00 (27,084); puts 500.00 (19,178) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 550 calls, 12,608 OI: 2026-10-23 34% (4,259), 2026-11-20 28% (3,549), 2026-10-21 23% (2,899); put wall 550 puts, 11,863 OI: 2026-11-20 49% (5,872), 2026-10-30 17% (1,995), 2026-10-23 16% (1,894); max call OI 620 calls, 27,084 OI: 2026-11-20 42% (11,450), 2026-10-30 27% (7,325), 2026-10-23 18% (4,920); max put OI 500 puts, 19,178 OI: 2026-11-20 31% (5,970), 2026-10-23 25% (4,830), 2026-10-21 14% (2,734) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 550.00: 12,608 calls; put wall 550.00: 11,863 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 1.00 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | -2.94 vol pts (put 57.9%, call 60.8%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 20.5% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 34.9% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 18.7% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 25.8% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$1.2M net, 1.0% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-21T16:30:50+00:00)

- Call wall: 550.00 -> 550.00 (+0.00)
- Put wall: 550.00 -> 550.00 (+0.00)
- Zero gamma: 543.73 -> 543.35 (-0.38)
- Abs gamma strike: 550.00 -> 550.00 (+0.00)
- Net GEX: $155.1M -> $186.0M (+$30.9M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
