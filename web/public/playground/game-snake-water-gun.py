# === Snake Water and Gun · annotated for the pyBegin playground ===
# A beginner-friendly walkthrough — original project by @Yashparwal1.

import random

# Show game title and rules
print("GAME NAME - Snake, Water and Gun")
print(
    "GAME RULES :\n[ + ]. Choose s for Snake, w for Water and g for Gun\n[ + ].If any game draws, it'll be counted\n[ + ]. If you pressed other than s, w and g key, it'll be counted."
)
print(
    "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-"
)
ready = input(
    "So, Be ready the game is starting\n=========Press Enter to start========="
)

# Set up scores and game counter
totalchances = 3
user_score = 0
computer_score = 0
gameno = 0

lst = ["s", "w", "g"]
print("[ s ] - Snake\n[ w ] - Water\n[ g ] - Gun\n")

# Repeat for each round of the game
while gameno < totalchances:
    gameno = gameno + 1
    print(f"=========Game {gameno} is starting=========")

    # Get player and computer choices
    user = input("CHOOSE WISELY:= ")
    computer = random.choice(lst)

    # Check all win/draw/lose combinations
    if user == "s" and computer == "s":
        print(f"Your Choice = {user} and Computer Choice = {computer}")
        print("!!! Match Draw !!!")
        print(f"===> Youe Score: {user_score}")
        print(f"===> Computer Score: {computer_score}")

    elif user == "s" and computer == "w":
        user_score = user_score + 1
        print(f"Your Choice = {user} and Computer choice = {computer}")
        print("!!! You WON !!!")
        print(f"===> Youe Score: {user_score}")
        print(f"===> Computer Score: {computer_score}")

    elif user == "s" and computer == "g":
        computer_score = computer_score + 1
        print(f"Your Choice = {user} and Computer choice = {computer}")
        print("!!! Computer WON !!!")
        print(f"===> Youe Score: {user_score}")
        print(f"===> Computer Score: {computer_score}")

    elif user == "w" and computer == "w":
        print(f"Your Choice = {user} and Computer Choice = {computer}")
        print("!!! Match Draw !!!")
        print(f"===> Youe Score: {user_score}")
        print(f"===> Computer Score: {computer_score}")

    elif user == "w" and computer == "s":
        computer_score = computer_score + 1
        print(f"Your Choice = {user} and Computer Choice = {computer}")
        print("!!! Computer WON !!!")
        print(f"===> Youe Score: {user_score}")
        print(f"===> Computer Score: {computer_score}")

    elif user == "w" and computer == "g":
        user_score = user_score + 1
        print(f"Your Choice = {user} and Computer Choice = {computer}")
        print("!!! You WON !!!")
        print(f"===> Youe Score: {user_score}")
        print(f"===> Computer Score: {computer_score}")

    elif user == "g" and computer == "g":
        print(f"Your Choice = {user} and Computer Choice = {computer}")
        print("!!! Match Draw !!!")
        print(f"===> Youe Score: {user_score}")
        print(f"===> Computer Score: {computer_score}")

    elif user == "g" and computer == "s":
        user_score = user_score + 1
        print(f"Your Choice = {user} and Computer Choice = {computer}")
        print("!!! You WON !!!")
        print(f"===> Youe Score: {user_score}")
        print(f"===> Computer Score: {computer_score}")

    elif user == "g" and computer == "w":
        computer_score = computer_score + 1
        print(f"Your Choice = {user} and Computer Choice = {computer}")
        print("!!! Computer WON !!!")
        print(f"===> Youe Score: {user_score}")
        print(f"===> Computer Score: {computer_score}")

    else:
        print("(*)---Please choose correct option---(*)")

# Show final scores and series winner
print("|*|*|*|*|*|*|*| GAME OVER |*|*|*|*|*|*|*|")
print(
    "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-"
)
print(
    f"Your Total Score is : {user_score} and Computer's Total Score is : {computer_score}"
)
if user_score > computer_score:
    print(
        "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-"
    )
    print(
        "Hurrey!!! You Won the Series\nHere is a gift for you.... ❤❤❤🎂🎂🎂\nSee you next time.Bye......"
    )
else:
    print(
        "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-"
    )
    print(
        "Sorry!!! You lose the series\nDon't worry you'll still get a gift.... 😝LOL😝 Come next time "
    )

out = input("<=== Press any key to exit ===>")
