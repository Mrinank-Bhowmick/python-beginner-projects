# Roll A Dice

A console game where the player rolls a virtual dice and is given a task or riddle based on the number rolled. The player's name, roll, and answer are recorded in a MySQL database.

## How to run

```sh
pip install mysql-connector-python
python dice.py
```

You must have a MySQL server running and update the connection credentials in `dice.py`.

## Dependencies

- mysql-connector-python
- random (standard library)

## Pyodide-runnable

No - it connects to a MySQL database server, which cannot run in the browser sandbox.
