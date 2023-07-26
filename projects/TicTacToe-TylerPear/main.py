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
        while valid == False:
            move = input("Type a valid move:")
            if move in ["TL", "TM", "TR", "ML", "MM", "MR", "BL", "BM", "BR"]:
                valid = True
                return move


def examine_move(board, x, y, msg):
    taken = False

    if "X" in board[x][y] or "O" in board[x][y]:
        taken = True
    else:
        board[x][y] = msg

    return taken


def change_board(move, board, player):
    taken = False

    # TOP ROW

    if move == "TL":
        taken = examine_move(board, 0, 0, f" {player}|")
    elif move == "TM":
        taken = examine_move(board, 0, 1, f" {player} | ")
    elif move == "TR":
        taken = examine_move(board, 0, 2, f"{player}")

    # MIDDLE ROW

    if move == "ML":
        taken = examine_move(board, 2, 0, f" {player}|")
    elif move == "MM":
        taken = examine_move(board, 2, 1, f" {player} | ")
    elif move == "MR":
        taken = examine_move(board, 2, 2, f"{player}")

    # BOTTOM ROW

    if move == "BL":
        taken = examine_move(board, 4, 0, f" {player}|")
    elif move == "BM":
        taken = examine_move(board, 4, 1, f" {player} | ")
    elif move == "BR":
        taken = examine_move(board, 4, 2, f"{player}")

    if taken:
        move = input("That spot is taken! Pick another spot: ")
        change_board(move, board, player)

    return board


def change_player(i):
    if i % 2 == 0:
        return "O"
    else:
        return "X"


def check_for_win(board, player):
    # Check Lists
    if board[0] == [f" {player}|", f" {player} | ", f"{player}"]:
        return True
    elif board[2] == [f" {player}|", f" {player} | ", f"{player}"]:
        return True
    elif board[4] == [f" {player}|", f" {player} | ", f"{player}"]:
        return True

    # Check Columns
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

    # Check Diagonal
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


def player_won(board):
    xwon = check_for_win(board, "X")
    owon = check_for_win(board, "O")

    if xwon or owon:
        return True
    else:
        return False


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

    if catsgame == False:
        if player == "X":
            print("Congrats! X Wins!")
        elif player == "O":
            print("Congrats! O Wins!")
