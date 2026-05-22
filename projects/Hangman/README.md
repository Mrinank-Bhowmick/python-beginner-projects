# Hangman

The classic Hangman game in the console. Pick a difficulty (easy/medium/hard), then guess the secret word letter by letter while ASCII art tracks your remaining tries. Word lists live in `RandomWords.py`.

## Example

```text
Choose difficulty level (easy, medium, hard): medium

-------------Welcome to Hangman-------------

        --------
        |      |
        |      
        |    
        |      
        |     
        -
______
Guess the word:- e
Good job, E is in the word!
_ E _ _ _ _

Guess the word:- a
A is not in the word.
        --------
        |      |
        |      O
        |    
        |      
        |     
        -
_ E _ _ _ _

Guess the word:- PYTHON
Congrats, you guessed the word! You win!
Do you want to play Hangman? (y/n): n
```

## How to run on localhost

```
python main.py
```

## Dependencies

Standard library only (`random`).
