# AMD gamma exposure report

As of 2026-10-21T00:49:04+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 534.74 | The underlying price used for every calculation in this run. |
| Net GEX | -$90.6M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 550.00, 620.00, 600.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 550.00, 530.00, 540.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 550.00: 2026-10-23 49%, 2026-10-21 20%, 2026-11-20 17%; 620.00: 2026-11-20 53%, 2026-10-30 29%, 2026-11-06 6%; 600.00: 2026-11-20 39%, 2026-10-23 22%, 2026-10-30 21% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 550.00: 2026-11-20 32%, 2026-10-23 29%, 2026-10-30 19%; 530.00: 2026-10-23 32%, 2026-10-21 21%, 2026-11-20 17%; 540.00: 2026-10-23 35%, 2026-10-21 21%, 2026-10-30 17% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 550.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 548.68 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $7.68B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $30.0M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$186.2M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±14.90 (2.8%) -> 519.84 to 549.64, exp 2026-10-21 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 387,179 calls / 389,124 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 620.00 (27,040); puts 440.00 (21,032) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 550 calls, 9,809 OI: 2026-10-23 36% (3,544), 2026-11-20 36% (3,522), 2026-10-21 11% (1,083); put wall 550 puts, 12,067 OI: 2026-11-20 50% (5,974), 2026-10-30 16% (1,980), 2026-10-23 16% (1,968); max call OI 620 calls, 27,040 OI: 2026-11-20 42% (11,386), 2026-10-30 27% (7,344), 2026-10-23 18% (4,987); max put OI 440 puts, 21,032 OI: 2026-11-20 92% (19,355), 2026-10-23 3% (602), 2026-11-06 2% (426) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 550.00: 9,809 calls; put wall 550.00: 12,067 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 1.01 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | -0.10 vol pts (put 60.3%, call 60.4%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 0.0% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 50.6% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 17.8% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 31.6% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$2.6M net, 1.0% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-21T00:32:46+00:00)

- Call wall: 550.00 -> 550.00 (+0.00)
- Put wall: 550.00 -> 550.00 (+0.00)
- Zero gamma: 548.68 -> 548.68 (+0.00)
- Abs gamma strike: 550.00 -> 550.00 (+0.00)
- Net GEX: -$90.5M -> -$90.6M (-$193.5K)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
