# Minesweeper

A console version of the classic Minesweeper game. It builds a board, randomly plants bombs, and asks the player where to dig (entered as `row,col`). Digging an empty cell recursively reveals neighbouring cells; hitting a bomb ends the game.

## How to run

```
python main.py
```

## Dependencies

Standard library only (`random`, `re`).

## Pyodide-runnable

Yes — it is a pure-stdlib console program that only uses `input()` and `print()`.
