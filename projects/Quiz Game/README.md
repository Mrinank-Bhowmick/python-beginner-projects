# Quiz Game

A console-based quiz game that asks three questions, scores the player's answers, and stores each player's name and score in a local SQLite database (`quiz_game.db`). Previous scores are displayed after each game. Run `setup_db.py` once first to create the database and table.

## Example

```text
Welcome to AskPython Quiz
Are you ready to play the Quiz? (yes/no) :yes
Question 1: What is your Favourite programming language?python
correct
Question 2: Do you follow any author on AskPython? yes
correct
Question 3: What is the name of your favourite website for learning Python?askpython
correct
Thank you for Playing this small quiz game, you attempted 3 questions correctly!
Marks obtained: 100%
Enter your name: Bob
Previous scores:
Name: Bob, Score: 3, Date: 2024-01-15 10:23:45
BYE!
```

## How to run on localhost

```sh
python setup_db.py
python main.py
```

## Dependencies

Standard library only (uses `sqlite3`).
