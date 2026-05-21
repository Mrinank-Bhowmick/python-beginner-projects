# Rock, Paper, Scissors
# Play a round against the computer's random choice.

import random

choices = ["rock", "paper", "scissors"]
beats = {"rock": "scissors", "paper": "rock", "scissors": "paper"}

you = input("Pick rock, paper or scissors: ").strip().lower()
if you not in choices:
    print("That's not a valid choice!")
else:
    cpu = random.choice(choices)
    print(f"You chose {you}, the computer chose {cpu}.")

    if you == cpu:
        print("It's a draw!")
    elif beats[you] == cpu:
        print("You win! 🎉")
    else:
        print("You lose! 😅")
