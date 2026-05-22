# Guess Number

A number guessing game. Two versions are included:

- `guess_number.py` — a console version where the program picks a random number 1-10 and gives higher/lower hints until you find it, with replay support.
- `guess_num_v2.py` — a Tkinter GUI version of the same game.

## Example

```text
Welcome to Number Guesser. If you'd like to play, press 'Y' or press 'X' if you want to exit: Y

Enter number between 1 to 10: 5

Number is higher than 5

Enter number between 6 to 10: 8

Number is lower than 8

Enter number between 6 to 7: 7

Congrats! You've guessed the correct number! It was 7.

You have tried 3 times to find the number.
```

## How to run on localhost

```
python guess_number.py
```

or, for the GUI version:

```
python guess_num_v2.py
```

## Dependencies

Standard library only (`random`, plus `tkinter` for the GUI version).
