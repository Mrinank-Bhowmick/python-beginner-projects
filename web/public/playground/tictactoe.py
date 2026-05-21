# Tic-Tac-Toe
# You are X, the computer is O. Enter a cell number 1-9 to play.

import random

board = [" "] * 9
wins = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6),
]


def show():
    print()
    for row in range(3):
        cells = []
        for col in range(3):
            i = row * 3 + col
            cells.append(board[i] if board[i] != " " else str(i + 1))
        print("  " + " | ".join(cells))
        if row < 2:
            print("  ---------")
    print()


def winner():
    for a, b, c in wins:
        if board[a] != " " and board[a] == board[b] == board[c]:
            return board[a]
    return None


print("Tic-Tac-Toe — you are X.")
show()

while True:
    move = input("Your move (1-9): ").strip()
    if not move.isdigit() or not (1 <= int(move) <= 9):
        print("Please enter a number from 1 to 9.")
        continue
    spot = int(move) - 1
    if board[spot] != " ":
        print("That cell is taken — try another.")
        continue

    board[spot] = "X"
    show()

    if winner() == "X":
        print("You win! 🎉")
        break
    if " " not in board:
        print("It's a draw! 🤝")
        break

    cpu = random.choice([i for i, v in enumerate(board) if v == " "])
    board[cpu] = "O"
    print(f"Computer played {cpu + 1}.")
    show()

    if winner() == "O":
        print("Computer wins! 🤖")
        break
    if " " not in board:
        print("It's a draw! 🤝")
        break
