# === Rock Paper Scissors · annotated for the pyBegin playground ===
# A beginner-friendly walkthrough — original project by @ZackeryRSmith.

import random

# Define valid choices and what each choice beats
choices = ["rock", "paper", "scissors"]
beats = {"rock": "scissors", "paper": "rock", "scissors": "paper"}

# Get the player's move and validate it
you = input("Pick rock, paper or scissors: ").strip().lower()
if you not in choices:
    print("That's not a valid choice!")
else:
    # Computer picks a random move
    cpu = random.choice(choices)
    print(f"You chose {you}, the computer chose {cpu}.")

    # Compare moves and announce the result
    if you == cpu:
        print("It's a draw!")
    elif beats[you] == cpu:
        print("You win! 🎉")
    else:
        print("You lose! 😅")
