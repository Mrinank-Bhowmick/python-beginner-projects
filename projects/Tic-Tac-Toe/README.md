# Tic-Tac-Toe

Two implementations of the classic 3×3 game:

- **`Tic-Tac-Toe-Terminal/`** — a console version played with `input()`/`print()`.
- **`TicTacToe-GUI/`** — a Tkinter version (`tic tac.py`, plus a one-player mode
  in `oneplayermode.py`) using `X.png` / `O.jpg` images.

## Example

**Terminal version:**

```text
Welcome to Tic Tac Toe!
Do you want to be X or O?
X
The player will go first.
   |   |
-----------
   |   |
-----------
   |   |
What is your next move? (1-9)
5
   |   |
-----------
   | X |
-----------
   |   |
...
Hooray! You have won the game!
Do you want to play again? (yes or no)
no
```

**GUI version:** A Tkinter window opens with a 3×3 grid of buttons; click a cell to place your mark (X or O image tile), and the computer responds immediately.

## How to run on localhost

```bash
python Tic-Tac-Toe-Terminal/main.py     # terminal version
python TicTacToe-GUI/tic\ tac.py        # GUI version
```

## Dependencies

- Terminal version: standard library only.
- GUI version: `tkinter` (ships with the standard Python installer).
