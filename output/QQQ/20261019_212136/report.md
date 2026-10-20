# QQQ gamma exposure report

As of 2026-10-20T01:21:36+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 718.36 | The underlying price used for every calculation in this run. |
| Net GEX | -$5.13B | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 720.00, 740.00, 730.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 700.00, 720.00, 710.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 720.00: 2026-10-20 31%, 2026-11-20 27%, 2026-10-23 16%; 740.00: 2026-10-30 49%, 2026-10-23 23%, 2026-11-20 15%; 730.00: 2026-10-23 27%, 2026-11-20 23%, 2026-10-30 19% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 700.00: 2026-10-30 52%, 2026-11-20 21%, 2026-10-23 9%; 720.00: 2026-11-20 27%, 2026-10-30 24%, 2026-10-23 20%; 710.00: 2026-10-23 43%, 2026-10-30 18%, 2026-11-06 14% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 720.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 732.92 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $70.85B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $1.29B | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$1.70B | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±6.76 (0.9%) -> 711.60 to 725.12, exp 2026-10-20 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 1,626,417 calls / 2,604,192 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 760.00 (101,693); puts 700.00 (215,444) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 720 calls, 49,263 OI: 2026-11-20 52% (25,696), 2026-10-30 12% (5,816), 2026-10-23 11% (5,346); put wall 700 puts, 215,444 OI: 2026-10-30 48% (103,867), 2026-11-20 27% (57,692), 2026-10-23 7% (15,159); max call OI 760 calls, 101,693 OI: 2026-11-20 43% (43,370), 2026-11-06 25% (25,145), 2026-10-30 17% (16,833); max put OI 700 puts, 215,444 OI: 2026-10-30 48% (103,867), 2026-11-20 27% (57,692), 2026-10-23 7% (15,159) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 720.00: 49,263 calls; put wall 700.00: 215,444 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 1.60 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 4.78 vol pts (put 24.4%, call 19.7%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 0.0% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 36.1% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 26.7% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 37.3% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$83.8M net, 3.0% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-20T01:17:50+00:00)

- Call wall: 720.00 -> 720.00 (+0.00)
- Put wall: 700.00 -> 700.00 (+0.00)
- Zero gamma: 732.86 -> 732.92 (+0.06)
- Abs gamma strike: 720.00 -> 720.00 (+0.00)
- Net GEX: -$5.04B -> -$5.13B (-$84.6M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
