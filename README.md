# tiny-chess-01 entry

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/nekobasi/tiny-chess-01/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/nekobasi/tiny-chess-01/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A chess engine in under 4 KB of Python 3.13 (standard library only) for
make.fun's [tiny-chess-01](https://make.fun/bounty/tiny-chess-01). `main.py` is the whole engine and plays every
game through the env at `MAKEFUN_ENV_URL`.

- 10x12 mailbox board, pseudo-legal move generation plus a king-safety check
- iterative deepening alpha-beta (PVS) with a fixed node budget, so moves
  are deterministic
- quiescence over captures, check extension, null move, late-move reductions
- transposition table, futility pruning, MVV-LVA, killer and history ordering
- material plus piece-square terms built from formulas, with an endgame king table

Search budget: 45,000 nodes per move by default (`NODES` env var overrides it).
On the kit's practice gauntlets it scored 23/30 over five sets (local Elo
estimates 1364-1654), against 1279 for the previous version.

Run: `MAKEFUN_ENV_URL=<env url> python3.13 main.py`. `main.py` is packed from a
readable source with `makefun compress`.

MIT licensed (see LICENSE).
