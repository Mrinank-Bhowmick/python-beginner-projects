# === Minesweeper · annotated for the pyBegin playground ===
# A beginner-friendly walkthrough — original project by @myudak.

import random
import re


# Board class holds the grid, bombs, and dig logic
class Board:
    def __init__(self, dim_size, num_bombs):
        # Store grid dimensions and bomb count
        self.dim_size = dim_size
        self.num_bombs = num_bombs

        # Build the grid and assign neighbor counts
        self.board = self.make_new_board()
        self.assign_values_to_board()

        # Track which cells the player has uncovered
        self.dug = set()

    # Create an empty grid and randomly place bombs
    def make_new_board(self):
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]

        # Plant bombs at random positions
        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            loc = random.randint(
                0, self.dim_size**2 - 1
            )
            row = (
                loc // self.dim_size
            )
            col = (
                loc % self.dim_size
            )

            if board[row][col] == "*":
                continue

            board[row][col] = "*"
            bombs_planted += 1

        return board

    # Fill non-bomb cells with neighbor bomb counts
    def assign_values_to_board(self):
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c] == "*":
                    continue
                self.board[r][c] = self.get_num_neighboring_bombs(r, c)

    # Count bombs in the 8 cells surrounding a position
    def get_num_neighboring_bombs(self, row, col):
        num_neighboring_bombs = 0
        for r in range(max(0, row - 1), min(self.dim_size - 1, row + 1) + 1):
            for c in range(max(0, col - 1), min(self.dim_size - 1, col + 1) + 1):
                if r == row and c == col:
                    continue
                if self.board[r][c] == "*":
                    num_neighboring_bombs += 1

        return num_neighboring_bombs

    # Dig a cell; recurse into empty neighbors automatically
    def dig(self, row, col):
        self.dug.add((row, col))

        # Return False immediately if a bomb is hit
        if self.board[row][col] == "*":
            return False
        elif self.board[row][col] > 0:
            return True

        # Recursively dig all untouched neighbors
        for r in range(max(0, row - 1), min(self.dim_size - 1, row + 1) + 1):
            for c in range(max(0, col - 1), min(self.dim_size - 1, col + 1) + 1):
                if (r, c) in self.dug:
                    continue
                self.dig(r, c)

        return True

    # Build a printable string of the visible board
    def __str__(self):
        visible_board = [
            [None for _ in range(self.dim_size)] for _ in range(self.dim_size)
        ]
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if (row, col) in self.dug:
                    visible_board[row][col] = str(self.board[row][col])
                else:
                    visible_board[row][col] = " "

        # Assemble a formatted string with column headers
        string_rep = ""
        widths = []
        for idx in range(self.dim_size):
            columns = map(lambda x: x[idx], visible_board)
            widths.append(len(max(columns, key=len)))

        indices = [i for i in range(self.dim_size)]
        indices_row = "   "
        cells = []
        for idx, col in enumerate(indices):
            format = "%-" + str(widths[idx]) + "s"
            cells.append(format % (col))
        indices_row += "  ".join(cells)
        indices_row += "  \n"

        for i in range(len(visible_board)):
            row = visible_board[i]
            string_rep += f"{i} |"
            cells = []
            for idx, col in enumerate(row):
                format = "%-" + str(widths[idx]) + "s"
                cells.append(format % (col))
            string_rep += " |".join(cells)
            string_rep += " |\n"

        str_len = int(len(string_rep) / self.dim_size)
        string_rep = indices_row + "-" * str_len + "\n" + string_rep + "-" * str_len

        return string_rep


# Main game loop: show board, get input, dig, repeat
def play(dim_size=10, num_bombs=10):
    # Set up a fresh board
    board = Board(dim_size, num_bombs)

    safe = True

    # Keep playing until all safe cells are dug
    while len(board.dug) < board.dim_size**2 - num_bombs:
        print(board)
        user_input = re.split(
            ",(\\s)*", input("Where would you like to dig? Input as row,col: ")
        )
        row, col = int(user_input[0]), int(user_input[-1])
        if row < 0 or row >= board.dim_size or col < 0 or col >= dim_size:
            print("Invalid location. Try again.")
            continue

        # Dig the chosen cell and check if it was a bomb
        safe = board.dig(row, col)
        if not safe:
            break

    # Announce win or reveal the board on loss
    if safe:
        print("CONGRATULATIONS!!!! YOU ARE VICTORIOUS!")
    else:
        print("SORRY GAME OVER :(")
        board.dug = [
            (r, c) for r in range(board.dim_size) for c in range(board.dim_size)
        ]
        print(board)


if __name__ == "__main__":
    play()
