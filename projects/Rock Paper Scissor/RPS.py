import os
import time


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_player_choice(player_name):
    choice = input(f"{player_name}, enter your choice (rock, paper, or scissors): ").strip().lower()
    return choice


def determine_winner(player1_choice, player2_choice):
    if player1_choice == player2_choice:
        return "It's a tie!"
    elif (player1_choice == "rock" and player2_choice == "scissors") or \
            (player1_choice == "scissors" and player2_choice == "paper") or \
            (player1_choice == "paper" and player2_choice == "rock"):
        return "Player 1 wins!"
    else:
        return "Player 2 wins!"


if __name__ == "__main__":
    clear_screen()
    print("Welcome to the Rock-Paper-Scissors game!")

    player1_name = input("Enter Player 1's name: ")
    player2_name = input("Enter Player 2's name: ")

    while True:
        clear_screen()

        print("Both players, make your selections now...")
        time.sleep(2)

        player1_choice = get_player_choice(player1_name)
        clear_screen()

        print(f"{player1_name} chose: {player1_choice}\n")

        time.sleep(2)

        player2_choice = get_player_choice(player2_name)
        clear_screen()

        print(f"{player1_name} chose: {player1_choice}\n")
        print(f"{player2_name} chose: {player2_choice}\n")

        result = determine_winner(player1_choice, player2_choice)
        print(result)

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

    print("Thanks for playing!")
