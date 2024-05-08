import random
import time


def main():
    print("Welcome Hand Cricket")
    print("You will be playing against another player")
    try:
        overs = int(input("Enter the number of overs (1-10): "))

        # Toss to decide who bats first
        toss_winner = toss()
        if toss_winner == 1:
            print("Player 1 won the toss!")
            player1_choice = input("Player 1, choose 1 to bat first, 2 to bowl first: ")
            player2_choice = "1" if player1_choice == "2" else "2"
        else:
            print("Player 2 won the toss!")
            player2_choice = input("Player 2, choose 1 to bat first, 2 to bowl first: ")
            player1_choice = "1" if player2_choice == "2" else "2"

        difficulty = int(input("Select difficulty level (1-Easy, 2-Medium, 3-Hard): "))

        # Call the play_game function with user inputs
        player1_score, player2_score = play_game(
            overs, player1_choice, player2_choice, difficulty
        )

        # Determine and display the winner
        who_won(player1_score, player2_score)
    except ValueError:
        print("Invalid input, exiting game")


# Function to handle the toss
def toss():
    print("Toss time!")
    user_choice = input("Choose heads (1) or tails (2): ")
    toss_result = random.randint(1, 2)
    if int(user_choice) == toss_result:
        print("It's", "Heads!" if toss_result == 1 else "Tails!")
        return 1  # Player 1 wins the toss
    else:
        print("It's", "Heads!" if toss_result == 1 else "Tails!")
        return 2  # Player 2 wins the toss


# Function to handle the main gameplay for two players
def play_game(overs, player1_choice, player2_choice, difficulty=1):
    player1_score = 0
    player2_score = 0
    player1_wickets = 10
    player2_wickets = 10

    print("\nMatch Summary")
    print("=============")
    print(f"Overs: {overs}")

    for over in range(overs):
        print(
            f"\nOver {over + 1}, Player 1: {player1_wickets} wickets left, Player 2: {player2_wickets} wickets left"
        )

        if player1_choice == "1":
            # Player 1 bats first
            player1_score, player1_wickets = user_turn(
                player1_score, player1_wickets, "1", over
            )

            # Player 2 bowls
            player2_score, player2_wickets = user_turn(
                player2_score, player2_wickets, "2", over
            )
        else:
            # Player 2 bowls first
            player2_score, player2_wickets = user_turn(
                player2_score, player2_wickets, "2", over
            )

            # Player 1 bats
            player1_score, player1_wickets = user_turn(
                player1_score, player1_wickets, "1", over
            )

        # Display the scoreboard after each over
        display_scoreboard(player1_score, player2_score, over)

    # Return the final scores
    return player1_score, player2_score


# Function for a player's turn
def user_turn(player_score, player_wickets, player_choice, over):
    print(f"Player's turn - {'Batting' if player_choice == '1' else 'Bowling'}")
    balls = 0
    while balls < 6 and player_wickets > 0:
        if player_choice == "1":
            # Get user input for batting
            player_runs = int(
                input(f"Over {over + 1}, Ball {balls + 1}: Enter your {'shot'} (1-6): ")
            )
            opponent_runs = random.randint(1, 6)
        else:
            # Get user input for bowling
            opponent_choice = input(
                f"Over {over + 1}, Ball {balls + 1}: Player 2, choose 1 to bat, 2 to bowl: "
            )
            player_runs = random.randint(1, 6)
            opponent_runs = int(
                input(
                    f"Over {over + 1}, Ball {balls + 1}: Enter your {'delivery'} (1-6): "
                )
            )

        print(f"You chose {player_runs}, Opponent chose {opponent_runs}")

        # Check if the player is out or scores runs
        if player_choice == "1" and player_runs == opponent_runs:
            print("Player is out!")
            player_wickets -= 1
            if player_wickets > 0:
                print(f"Player has {player_wickets} wickets left.")
        elif (
            player_choice == "2"
            and opponent_choice == "2"
            and player_runs == opponent_runs
        ):
            print("Opponent is out!")
            player_wickets -= 1
            if player_wickets > 0:
                print(f"Opponent has {player_wickets} wickets left.")
        else:
            player_score += player_runs
            print(f"Player's score is {player_score}")
        balls += 1

    # Return the updated player score and wickets
    return player_score, player_wickets


# Function to display the scoreboard after each over
def display_scoreboard(player1_score, player2_score, over):
    print("\nScoreboard")
    print("==========")
    print(f"Over {over + 1}:")
    print(f"Player 1: {player1_score} runs")
    print(f"Player 2: {player2_score} runs")


# Function to determine and display the winner of the match
def who_won(player1_score, player2_score):
    print("\nMatch Result")
    print("============")
    print("Player 1's score =", player1_score)
    print("Player 2's score =", player2_score)
    if player1_score > player2_score:
        print("Player 1 won")
    elif player2_score > player1_score:
        print("Player 2 won")
    else:
        print("The match ended in a draw")
    print("Thank you for playing and have a good day :) ")


# Run the main function if the script is executed
if __name__ == "__main__":
    main()
