# IWM gamma exposure report

As of 2026-10-20T17:02:06+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 275.31 | The underlying price used for every calculation in this run. |
| Net GEX | -$1.19B | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 275.00, 276.00, 280.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 270.00, 275.00, 265.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 275.00: 2026-10-20 37%, 2026-10-21 31%, 2026-10-23 12%; 276.00: 2026-10-20 46%, 2026-10-23 27%, 2026-10-21 14%; 280.00: 2026-10-29 31%, 2026-10-23 25%, 2026-11-20 19% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 270.00: 2026-11-20 62%, 2026-10-30 23%, 2026-10-23 6%; 275.00: 2026-11-20 36%, 2026-10-20 18%, 2026-10-23 17%; 265.00: 2026-11-20 66%, 2026-10-30 23%, 2026-11-06 4% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 275.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 281.25 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $17.89B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $526.2M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$320.4M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±1.18 (0.4%) -> 274.13 to 276.48, exp 2026-10-20 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 1,017,047 calls / 2,103,722 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 290.00 (62,953); puts 270.00 (204,752) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 275 calls, 44,607 OI: 2026-10-21 24% (10,614), 2026-10-23 16% (7,280), 2026-11-06 12% (5,229); put wall 270 puts, 204,752 OI: 2026-11-20 69% (142,217), 2026-10-30 17% (34,707), 2026-10-23 4% (7,540); max call OI 290 calls, 62,953 OI: 2026-11-20 70% (43,985), 2026-10-30 18% (11,541), 2026-10-23 5% (3,083); max put OI 270 puts, 204,752 OI: 2026-11-20 69% (142,217), 2026-10-30 17% (34,707), 2026-10-23 4% (7,540) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 275.00: 44,607 calls; put wall 270.00: 204,752 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 2.07 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 1.57 vol pts (put 20.0%, call 18.4%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 6.3% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 24.8% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 26.0% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 42.9% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | $285.4K net, 0.4% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-20T13:57:35+00:00)

- Call wall: 274.00 -> 275.00 (+1.00)
- Put wall: 270.00 -> 270.00 (+0.00)
- Zero gamma: 280.60 -> 281.25 (+0.65)
- Abs gamma strike: 274.00 -> 275.00 (+1.00)
- Net GEX: -$893.4M -> -$1.19B (-$296.6M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
