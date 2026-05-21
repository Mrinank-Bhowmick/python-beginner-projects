# Multiplayer Socket Games

A two-player networked game system using TCP sockets. `server.py` hosts the games and `client.py` connects to it. Players can choose between a multiplayer Hangman game and a Rock-Paper-Scissors game.

## How to run

Start the server first, then run a client on each player's machine:

```
python server.py
python client.py
```

## Dependencies

Standard library only (`socket`, `_thread`).

## Pyodide-runnable

No — it uses raw TCP sockets and threading to communicate between machines, which is not possible in a browser sandbox.
