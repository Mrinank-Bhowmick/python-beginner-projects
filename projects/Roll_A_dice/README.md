# Roll A Dice

A console game where the player rolls a virtual dice and is given a task or riddle based on the number rolled. The player's name, roll, and answer are recorded in a MySQL database.

## Example

```text
Your name: Alice
Hey Alice! Welcome to Roll A Dice game🎲
Rules:
1. You have to roll a dice.
2. Whatever number comes in, an associated task will be given to you.
3. You have to perform the task.
4. After you're done, press enter.
5. Don't forget to have fun🥳

Choose any one:
    1. Move ahead with the game
    2. Exit
    1
🎲 -  5
Yayyyy!! You got 5!.
 What has two banks but no money🤔?
Your ans: River bank
Viola! You are right
Have a good day!
Your response has been recorded ✅!
```

## How to run on localhost

```sh
pip install mysql-connector-python
python dice.py
```

You must have a MySQL server running and update the connection credentials in `dice.py`.

## Dependencies

- mysql-connector-python
- random (standard library)
