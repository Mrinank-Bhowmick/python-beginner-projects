import random
import time


def main():
    print("Welcome Hand Cricket")
    print("You will be playing against the computer")
    try:
        overs = int(input("Enter the number of overs (1-10): "))
        user_choice = input("Enter 1 to bat first, 2 to bowl first: ")
        difficulty = int(input("Select difficulty level (1-Easy, 2-Medium, 3-Hard): "))

        user_score, computer_score = play_game(overs, user_choice, difficulty)

        who_won(user_score, computer_score)
    except ValueError:
        print("Invalid input, exiting game")


def play_game(overs, user_choice, difficulty=1):
    user_score = 0
    computer_score = 0
    user_wickets = 10
    computer_wickets = 10

    print("\nMatch Summary")
    print("=============")
    print(f"Overs: {overs}")

    for over in range(overs):
        print(
            f"\nOver {over + 1}, User: {user_wickets} wickets left, Computer: {computer_wickets} wickets left"
        )

        if user_choice == "1":
            user_score, user_wickets = user_bat(user_score, user_wickets, over)

            if computer_wickets > 0:
                computer_score, computer_wickets = computer_bat(
                    computer_score, computer_wickets, difficulty, over
                )
        else:
            if computer_wickets > 0:
                computer_score, computer_wickets = computer_bat(
                    computer_score, computer_wickets, difficulty, over
                )

            user_score, user_wickets = user_bat(user_score, user_wickets, over)

        display_scoreboard(user_score, computer_score, over)

    return user_score, computer_score


def user_bat(user_score, user_wickets, over):
    print("You are batting")
    balls = 0
    while balls < 6 and user_wickets > 0:
        user_runs = int(
            input(f"Over {over + 1}, Ball {balls + 1}: Enter your shot (1-6): ")
        )
        computer_runs = random.randint(1, 6)

        print(f"You chose {user_runs}, Computer chose {computer_runs}")

        if user_runs == computer_runs:
            print("You are out!")
            user_wickets -= 1
            if user_wickets > 0:
                print(f"You have {user_wickets} wickets left.")
        else:
            user_score += user_runs
            print(f"Your score is {user_score}")
        balls += 1

    return user_score, user_wickets


def computer_bat(computer_score, computer_wickets, difficulty=1, over=None):
    print("Computer is batting")
    balls = 0
    while balls < 6 and computer_wickets > 0:
        if difficulty == 1:
            computer_runs = random.randint(1, 3)
        elif difficulty == 2:
            computer_runs = random.randint(1, 5)
        else:
            computer_runs = random.randint(1, 6)

        user_runs = int(
            input(
                f"Computer is batting. Over {over + 1}, Ball {balls + 1}: Enter your delivery (1-6): "
            )
        )

        print(f"You chose {user_runs}, Computer chose {computer_runs}")

        if user_runs == computer_runs:
            print("Computer is out!")
            computer_wickets -= 1
            if computer_wickets > 0:
                print(f"Computer has {computer_wickets} wickets left.")
        else:
            computer_score += computer_runs
            print(f"Computer's score is {computer_score}")
        balls += 1

    return computer_score, computer_wickets


def display_scoreboard(user_score, computer_score, over):
    print("\nScoreboard")
    print("==========")
    print(f"Over {over + 1}:")
    print(f"You: {user_score} runs")
    print(f"Computer: {computer_score} runs")


def who_won(user_score, computer_score):
    print("\nMatch Result")
    print("============")
    print("Your score =", user_score)
    print("Computer's score =", computer_score)
    if user_score > computer_score:
        print("You won")
    elif computer_score > user_score:
        print("You lost")
    else:
        print("The match ended in a draw")
    print("Thank you for playing and have a good day :) ")


if __name__ == "__main__":
    main()
