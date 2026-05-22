# Multiplayer Socket Games

A two-player networked game system using TCP sockets. `server.py` hosts the games and `client.py` connects to it. Players can choose between a multiplayer Hangman game and a Rock-Paper-Scissors game.

## Example

**Rock-Paper-Scissors (Player 1 terminal):**

```text
Enter your choice(1 or 2)
2
Get ready to play Rock, Paper, Scissor
You are Player 1
Play
rock
ROCK,PAPER,0,1
Play
paper
Player 2 won
```

**Hangman (Player 1 choosing the word):**

```text
Enter your choice(1 or 2)
1
Get ready to play hangman
Choose a word
python
Word sent to server
Waiting for guess...
Guess= P
Enter the positions of occurances
1
```

## How to run on localhost

Start the server first, then run a client on each player's machine:

```
python server.py
python client.py
```

## Dependencies

Standard library only (`socket`, `_thread`).
