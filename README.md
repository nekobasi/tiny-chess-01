# tiny-chess-01 entry

A chess engine in under 4 KB of Python 3.13 (standard library only) for
make.fun's tiny-chess-01. `main.py` is the whole engine and plays every
game through the env at `MAKEFUN_ENV_URL`.

- 10x12 mailbox board, pseudo-legal move generation plus a king-safety check
- iterative deepening alpha-beta (PVS) with a fixed node budget, so moves
  are deterministic
- quiescence over captures, check extension, null move, late-move reductions
- transposition table, MVV-LVA and killer move ordering
- material plus piece-square terms built from formulas, with an endgame king table

MIT licensed (see LICENSE).
