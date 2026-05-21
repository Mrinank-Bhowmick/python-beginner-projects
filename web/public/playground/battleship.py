# === Py-Battleship · annotated for the pyBegin playground ===
# A beginner-friendly walkthrough — original project by @robertlent.

# Import random number generator
from random import randint

# Set up the board list and default size
board = []
size = 5


# Ask the player to start a new game
def new_game():
    global size
    answer = input("Do you want to start a new game of Battleship? ").lower()

    # Validate the yes/no answer
    if answer not in ["yes", "y", "no", "n"]:
        new_game()
    else:
        if answer == "yes" or answer == "y":
            # Ask for board size between 5 and 15
            while True:
                try:
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

            # Build the board grid with "O" cells
            for x in range(0, size):
                board.append(["O"] * size)
            game()
        elif answer == "no" or answer == "n":
            print("Thank you for playing!\n")
            input("Press the 'Enter' key to exit the game.")
            quit()


# Print the current board to the screen
def print_board(board):
    for row in board:
        print(" ".join(row))


# Pick a random row index
def random_row(board):
    return randint(0, len(board) - 1)


# Pick a random column index
def random_col(board):
    return randint(0, len(board[0]) - 1)


# Run the main game loop
def game():
    global board
    print(
        "Welcome to Battleship.\n\nA ship, one cell long, has been randomly placed on the below %dx%d grid.\nYou have %d turns to find it.\n"
        % (size, size, size)
    )

    # Place the battleship at a random position
    ship_row = random_row(board)
    ship_col = random_col(board)

    # The next two lines are for debugging purposes. They display the position of the battleship.
    # print(ship_row + 1)
    # print(ship_col + 1)

    print_board(board)

    # Give the player one turn per size unit
    for turn in range(size):
        print("\nTurn", turn + 1, "of", size, "\n")

        # Ask for a valid row guess
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

        # Ask for a valid column guess
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

        # Check if the player found the ship
        if guess_row == ship_row and guess_col == ship_col:
            input(
                "Congratulations! You sank my battleship!\n\nPress enter to continue."
            )
            board = []
            new_game()
            break
        else:
            # Handle out-of-bounds guess
            if (guess_row > size or guess_row < 0) or (
                guess_col > size or guess_col < 0
            ):
                print("Oops, that's not even in the ocean.")
            # Handle repeated guess
            elif board[guess_row][guess_col] == "X":
                print("You guessed that one already. Good job, you wasted a turn.\n")
                print_board(board)
            else:
                # Mark the miss and show the board
                print("Miss!\n")
                board[guess_row][guess_col] = "X"
                print_board(board)
    else:
        # All turns used — game over
        input("\nGame Over\n\nPress enter to continue.")
        board = []
        new_game()


new_game()
