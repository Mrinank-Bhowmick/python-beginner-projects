# Number Guessing App

A two-mode number guessing game. In mode 1 the player guesses a random number chosen by the computer; in mode 2 the computer guesses the number the player picked, using feedback (too high / too low / correct).

## Example

**Mode 1 — player guesses the computer's number:**

```text
Select gaming mode
 Press 1 to guess the number
Press 2 to choose the number
1
Enter any number: 10
OOPS! Too high!
Guess again: 5
OOPS! Too low
Guess again: 7
Congratulations!! You guessed the number 7 correctly
```

**Mode 2 — computer guesses the player's number:**

```text
2
Enter your number: 15
Is 9 too high (h), too low (l), or correct (c)? 
=>l
Is 12 too high (h), too low (l), or correct (c)? 
=>l
Is 14 too high (h), too low (l), or correct (c)? 
=>l
Is 15 too high (h), too low (l), or correct (c)? 
=>c
Yay! The computer guessed your number, 15, correctly!
```

## How to run on localhost

```
python main.py
```

## Dependencies

Standard library only (`random`).
