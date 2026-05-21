# Quiz Game

A console-based quiz game that asks three questions, scores the player's answers, and stores each player's name and score in a local SQLite database (`quiz_game.db`). Previous scores are displayed after each game. Run `setup_db.py` once first to create the database and table.

## How to run

```sh
python setup_db.py
python main.py
```

## Dependencies

Standard library only (uses `sqlite3`).

## Pyodide-runnable

Yes - it is a pure-stdlib console program; `sqlite3` is supported in Pyodide and the database is created in the in-memory virtual filesystem.
