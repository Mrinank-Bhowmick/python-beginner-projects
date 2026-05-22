# Game of Cricket

A text-based cricket game played against the computer. You pick a number from 1 to 6 each ball; matching the computer's number loses a wicket, otherwise you score runs. Includes a toss and a two-over innings for each side.

## Example

```text
~ Welcome to the Game of Cricket ~

---------- Start Game ----------
Choose heads or tails: heads

Toss Result: Heads
User won the toss
Choose to bat or bowl: bat

You's Innings Begins
Choose any number from 1 to 6: 4
Your choice: 4
Computer's choice: 2
Total Score: 4/0
Balls remaining: 11
Choose any number from 1 to 6: 3
Your choice: 3
Computer's choice: 3
Total Score: 4/1
Balls remaining: 10
...
~~~~~~~~~~ Result ~~~~~~~~~~
Your total runs: 22
Computer's total runs: 18
Congratulations! You won the Match by 4 runs.
```

## How to run on localhost

```
python main.py
```

## Dependencies

Standard library only (`random`).
