# Tic-Tac-Toe

Two implementations of the classic 3×3 game:

- **`Tic-Tac-Toe-Terminal/`** — a console version played with `input()`/`print()`.
- **`TicTacToe-GUI/`** — a Tkinter version (`tic tac.py`, plus a one-player mode
  in `oneplayermode.py`) using `X.png` / `O.jpg` images.

## How to run

```bash
python Tic-Tac-Toe-Terminal/main.py     # terminal version
python TicTacToe-GUI/tic\ tac.py        # GUI version
```

## Dependencies

- Terminal version: standard library only.
- GUI version: `tkinter` (ships with the standard Python installer).

## Pyodide-runnable

Partly. The terminal version (`Tic-Tac-Toe-Terminal/main.py`) is pure-stdlib and
runs in the in-browser Pyodide playground. The Tkinter GUI version does not.
