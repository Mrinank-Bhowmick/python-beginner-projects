import os
from random import randint

board = []
size = 5


def new_game():
    global size
    os.system("cls" if os.name == "nt" else "clear")
    answer = input("Do you want to start a new game of Battleship? ").lower()

    if answer not in ["yes", "y", "no", "n"]:
        new_game()
    else:
        if answer == "yes" or answer == "y":
            while True:
                try:
                    os.system("cls" if os.name == "nt" else "clear")
                    size = int(
                        input(
                            "Enter a number between 5 and 15.\n\nThis will determine how big the playing board is and how many turns you have to find the Battleship. (5 rows, 5 columns, 5 turns, etc.): "
                        )
                    )
                    if size not in range(5, 16):
                        raise ValueError()
                except ValueError:
                    print("You did not enter a number!")
                    continue
                else:
                    break

            # Creates the playing board's size, based on the size chosen by the player.
            for x in range(0, size):
                board.append(["O"] * size)
            game()
        elif answer == "no" or answer == "n":
            os.system("cls" if os.name == "nt" else "clear")
            print("Thank you for playing!\n")
            input("Press the 'Enter' key to exit the game.")
            os.system("cls" if os.name == "nt" else "clear")
            quit()


def print_board(board):
    for row in board:
        print(" ".join(row))


def random_row(board):
    return randint(0, len(board) - 1)


def random_col(board):
    return randint(0, len(board[0]) - 1)


def game():
    global board
    os.system("cls" if os.name == "nt" else "clear")
    print(
        "Welcome to Battleship.\n\nA ship, one cell long, has been randomly placed on the below %dx%d grid.\nYou have %d turns to find it.\n"
        % (size, size, size)
    )

    # Randomly places Battleship
    ship_row = random_row(board)
    ship_col = random_col(board)

    # The next two lines are for debugging purposes. They display the position of the battleship.
    # print(ship_row + 1)
    # print(ship_col + 1)

    print_board(board)

    # Give the user the amount of turns they chose, between 5 and 10.
    for turn in range(size):
        print("\nTurn", turn + 1, "of", size, "\n")

        # Check if Guess Row and Column are numbers before continuing
        while True:
            try:
                guess_row = int(input("Guess Row: ")) - 1
                if guess_row not in range(0, size):
                    raise ValueError()
            except ValueError:
                print("Enter a valid selection!")
                continue
            else:
                break

        while True:
            try:
                guess_col = int(input("Guess Column: ")) - 1
                if guess_col not in range(0, size):
                    raise ValueError()
            except ValueError:
                print("Enter a valid selection!")
                continue
            else:
                break

        # Checks if Player wins
        if guess_row == ship_row and guess_col == ship_col:
            os.system("cls" if os.name == "nt" else "clear")
            input(
                "Congratulations! You sank my battleship!\n\nPress enter to continue."
            )
            board = []
            new_game()
            break
        else:  # Guesses are outside of playing field
            if (guess_row > size or guess_row < 0) or (
                guess_col > size or guess_col < 0
            ):
                print("Oops, that's not even in the ocean.")
            # Player previously guessed their current guesses
            elif board[guess_row][guess_col] == "X":
                os.system("cls" if os.name == "nt" else "clear")
                print("You guessed that one already. Good job, you wasted a turn.\n")
                print_board(board)
            else:  # User misses
                os.system("cls" if os.name == "nt" else "clear")
                print("Miss!\n")
                board[guess_row][guess_col] = "X"
                print_board(board)
    else:
        input("\nGame Over\n\nPress enter to continue.")
        board = []
        new_game()


new_game()
