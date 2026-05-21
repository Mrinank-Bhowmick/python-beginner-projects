# === Tic-Tac-Toe (TylerPear) · annotated for the pyBegin playground ===
# A beginner-friendly walkthrough — original project by @tylerapear.

# Set up board cell templates and the 5-row board list
spot = " "
leftSpot = f"{spot} |"
middleSpot = f" {spot} | "
rightSpot = f"{spot}"
board = [
    [leftSpot, middleSpot, rightSpot],
    ["___", "____", "__"],
    [leftSpot, middleSpot, rightSpot],
    ["___", "____", "__"],
    [leftSpot, middleSpot, rightSpot],
]

i = 0
player = ""


# Print the current board to the screen
def print_board():
    print(board[0][0], end="")
    print(board[0][1], end="")
    print(board[0][2], end="\n")
    print(board[1][0], end="")
    print(board[1][1], end="")
    print(board[1][2], end="\n")
    print(board[2][0], end="")
    print(board[2][1], end="")
    print(board[2][2], end="\n")
    print(board[3][0], end="")
    print(board[3][1], end="")
    print(board[3][2], end="\n")
    print(board[4][0], end="")
    print(board[4][1], end="")
    print(board[4][2], end="\n\n")


# Ask the current player for a valid move code
def collect_input(player):
    print("KEY: TL = Top Left, TM = Top Middle, TR = Top Right")
    print("     ML = Middle Left, MM = Middle Middle, MR = Middle Right")
    print("     BL = Bottom Left, BM = Bottom Middle, BR = Bottom Right")
    move = input(f"Player {player}, Type Your Move: ")
    valid = False
    if move in ["TL", "TM", "TR", "ML", "MM", "MR", "BL", "BM", "BR"]:
        valid = True
        return move
    else:
        # Keep asking until a valid code is entered
        while valid == False:
            move = input("Type a valid move:")
            if move in ["TL", "TM", "TR", "ML", "MM", "MR", "BL", "BM", "BR"]:
                valid = True
                return move


# Check if a cell is taken; place marker if free
def examine_move(board, x, y, msg):
    taken = False

    if "X" in board[x][y] or "O" in board[x][y]:
        taken = True
    else:
        board[x][y] = msg

    return taken


# Map the move code to a board cell and update it
def change_board(move, board, player):
    taken = False

    # Top row moves
    if move == "TL":
        taken = examine_move(board, 0, 0, f" {player}|")
    elif move == "TM":
        taken = examine_move(board, 0, 1, f" {player} | ")
    elif move == "TR":
        taken = examine_move(board, 0, 2, f"{player}")

    # Middle row moves
    if move == "ML":
        taken = examine_move(board, 2, 0, f" {player}|")
    elif move == "MM":
        taken = examine_move(board, 2, 1, f" {player} | ")
    elif move == "MR":
        taken = examine_move(board, 2, 2, f"{player}")

    # Bottom row moves
    if move == "BL":
        taken = examine_move(board, 4, 0, f" {player}|")
    elif move == "BM":
        taken = examine_move(board, 4, 1, f" {player} | ")
    elif move == "BR":
        taken = examine_move(board, 4, 2, f"{player}")

    # If cell was taken, ask for a new move
    if taken:
        move = input("That spot is taken! Pick another spot: ")
        change_board(move, board, player)

    return board


# Alternate between "O" (even turns) and "X" (odd turns)
def change_player(i):
    if i % 2 == 0:
        return "O"
    else:
        return "X"


# Check all win conditions for a given player
def check_for_win(board, player):
    # Check rows
    if board[0] == [f" {player}|", f" {player} | ", f"{player}"]:
        return True
    elif board[2] == [f" {player}|", f" {player} | ", f"{player}"]:
        return True
    elif board[4] == [f" {player}|", f" {player} | ", f"{player}"]:
        return True

    # Check columns
    elif (
        board[0][0] == f" {player}|"
        and board[2][0] == f" {player}|"
        and board[4][0] == f" {player}|"
    ):
        return True
    elif (
        board[0][1] == f" {player} | "
        and board[2][1] == f" {player} | "
        and board[4][1] == f" {player} | "
    ):
        return True
    elif (
        board[0][2] == f"{player}"
        and board[2][2] == f"{player}"
        and board[4][2] == f"{player}"
    ):
        return True

    # Check diagonals
    elif (
        board[0][0] == f" {player}|"
        and board[2][1] == f" {player} | "
        and board[4][2] == f"{player}"
    ):
        return True
    elif (
        board[0][2] == f"{player}"
        and board[2][1] == f" {player} | "
        and board[4][0] == f" {player}|"
    ):
        return True

    else:
        return False


# Return True if either player has won
def player_won(board):
    xwon = check_for_win(board, "X")
    owon = check_for_win(board, "O")

    if xwon or owon:
        return True
    else:
        return False


# Main game loop — play until someone wins or 9 turns pass
if __name__ == "__main__":
    catsgame = False
    while player_won(board) == False and catsgame == False:
        i += 1
        if i == 10:
            print("Cat's Game!")
            catsgame = True
        else:
            player = change_player(i)
            board = change_board(collect_input(player), board, player)
            print_board()

    # Announce the winner if the game wasn't a draw
    if catsgame == False:
        if player == "X":
            print("Congrats! X Wins!")
        elif player == "O":
            print("Congrats! O Wins!")
