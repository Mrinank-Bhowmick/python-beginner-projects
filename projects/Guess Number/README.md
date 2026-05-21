# Guess Number

A number guessing game. Two versions are included:

- `guess_number.py` — a console version where the program picks a random number 1-10 and gives higher/lower hints until you find it, with replay support.
- `guess_num_v2.py` — a Tkinter GUI version of the same game.

## How to run

```
python guess_number.py
```

or, for the GUI version:

```
python guess_num_v2.py
```

## Dependencies

Standard library only (`random`, plus `tkinter` for the GUI version).

## Pyodide-runnable

Partial — `guess_number.py` runs in Pyodide (console, `input()`/`print()` only); `guess_num_v2.py` does not because it uses Tkinter, which has no browser support.
