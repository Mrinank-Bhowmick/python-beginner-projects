import random


def get_user_choice():
    while True:
        try:
            user_choice = int(input("Choose any number from 1 to 6: "))
            if 1 <= user_choice <= 6:
                return user_choice
            else:
                print("Please choose a number from 1 to 6.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 6.")


def play_innings(player, overs, max_wickets):
    runs = 0
    wickets = 0
    balls = 0

    print(f"\n{player}'s Innings Begins")

    while wickets < max_wickets and balls < overs * 6:
        try:
            user_choice = get_user_choice()
            computer_choice = random.randint(1, 6)

            print(f"Your choice: {user_choice}\nComputer's choice: {computer_choice}")

            if user_choice == computer_choice:
                wickets += 1
            else:
                runs += user_choice

            balls += 1

            if balls % 6 == 0:
                over_number = balls // 6
                print(f"End of Over {over_number}")
                print(
                    f"Over {over_number} Summary: {player} scored {runs} runs with {wickets} wickets."
                )

            print(f"Total Score: {runs}/{wickets}")
            print(f"Balls remaining: {overs * 6 - balls}")

        except KeyboardInterrupt:
            print("\nGame interrupted. Exiting.")
            exit()
        except Exception as e:
            print(f"An error occurred: {e}")
            print("Please try again.")

    print("\nEnd of Innings")
    print(f"Final Score for {player}:\nRuns = {runs}\nWickets = {wickets}")

    return runs, wickets


print("~ Welcome to the Game of Cricket ~")

print("\nInstructions:")
print("1. You have to select any number from 1 to 6.")
print("2. The computer will also select a number.")
print(
    "3. While batting, if your number and computer's number are different, you'll add to your runs."
)
print("   If they are the same, you'll lose a wicket.")
print(
    "4. While bowling, if your number and computer's number are different, the computer adds to its runs."
)
print("   If they are the same, the computer loses a wicket.")
print(
    "5. Each player will get 2 wickets and 2 overs (12 balls) for batting and bowling."
)
print("6. The innings will end after either three wickets fall or the overs end.")
print("7. The player with the maximum runs wins.")

print("\n---------- Start Game ----------")

# Toss
toss_result = random.choice(["Heads", "Tails"])
user_toss_choice = input("Choose heads or tails: ").capitalize()
toss_winner = "User" if user_toss_choice == toss_result else "Computer"
print(f"\nToss Result: {toss_result}")
print(f"{toss_winner} won the toss")

if toss_winner == "User":
    user_choice = input("Choose to bat or bowl: ").lower()
    computer_choice = "bowl" if user_choice == "bat" else "bat"
else:
    computer_choice = random.choice(["bat", "bowl"])
    user_choice = "bowl" if computer_choice == "bat" else "bat"

print(
    f"{toss_winner} chose to {user_choice} and the computer chose to {computer_choice}"
)

user_runs, user_wickets = play_innings("You", 2, 2)
computer_runs, computer_wickets = play_innings("Computer", 2, 2)

print("\n~~~~~~~~~~ Result ~~~~~~~~~~")
print(f"Your total runs: {user_runs}")
print(f"Computer's total runs: {computer_runs}")

if user_runs > computer_runs:
    print(f"Congratulations! You won the Match by {user_runs - computer_runs} runs.")
elif user_runs < computer_runs:
    print(
        f"Better luck next time! The Computer won the Match by {computer_runs - user_runs} runs."
    )
else:
    print("The Match is a Tie. No one Wins.")
