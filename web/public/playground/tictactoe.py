# === Tic-Tac-Toe · annotated for the pyBegin playground ===
# A beginner-friendly walkthrough — original project by @Mrinank-Bhowmick.

import random

# Create a blank 9-cell board and define all win combos
board = [" "] * 9
wins = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6),
]


# Print the board in a 3x3 grid with separators
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


# Return "X" or "O" if a winning line exists
def winner():
    for a, b, c in wins:
        if board[a] != " " and board[a] == board[b] == board[c]:
            return board[a]
    return None


# Show opening message and initial board
print("Tic-Tac-Toe — you are X.")
show()

# Main game loop — alternate player and computer turns
while True:
    # Get a valid move from the player
    move = input("Your move (1-9): ").strip()
    if not move.isdigit() or not (1 <= int(move) <= 9):
        print("Please enter a number from 1 to 9.")
        continue
    spot = int(move) - 1
    if board[spot] != " ":
        print("That cell is taken — try another.")
        continue

    # Place player's mark and show updated board
    board[spot] = "X"
    show()

    # Check if player won or board is full
    if winner() == "X":
        print("You win! 🎉")
        break
    if " " not in board:
        print("It's a draw! 🤝")
        break

    # Computer picks a random empty cell
    cpu = random.choice([i for i, v in enumerate(board) if v == " "])
    board[cpu] = "O"
    print(f"Computer played {cpu + 1}.")
    show()

    # Check if computer won or board is full
    if winner() == "O":
        print("Computer wins! 🤖")
        break
    if " " not in board:
        print("It's a draw! 🤝")
        break
