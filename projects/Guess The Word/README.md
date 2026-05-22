# Guess The Word

A word guessing game (Hangman-style without the drawing). The program picks a random programming-language word and you have six attempts to reveal it one letter at a time.

## Example

```text
Welcome to the Word Guessing Game!
You have 6 attempts to guess the word.
_ _ _ _ _ _
Guess a letter: p
Correct guess!
p _ _ _ _ _
Guess a letter: y
Correct guess!
p y _ _ _ _
Guess a letter: t
Correct guess!
p y t _ _ _
Guess a letter: h
Correct guess!
p y t h _ _
Guess a letter: o
Correct guess!
p y t h o _
Guess a letter: n
Correct guess!
p y t h o n
Congratulations! You've guessed the word: python
```

## How to run on localhost

```
python Guess_the_word.py
```

## Dependencies

Standard library only (`random`).
