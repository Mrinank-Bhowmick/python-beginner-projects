# === Sudoku Solver · annotated for the pyBegin playground ===
# A beginner-friendly walkthrough — original project by @saltX5.

from random import sample


# Generate a randomized valid Sudoku board
def generate_board(num):
    base = 3
    side = base * base

    def pattern(r, c):
        return (base * (r % base) + r // base + c) % side

    def shuffle(s):
        return sample(s, len(s))

    # Shuffle row groups, rows within groups, and columns
    rBase = range(base)
    rows = [g * base + r for g in shuffle(rBase) for r in shuffle(rBase)]
    cols = [g * base + c for g in shuffle(rBase) for c in shuffle(rBase)]
    nums = shuffle(range(1, base * base + 1))

    # Build the full randomized board
    board_tmp = [[nums[pattern(r, c)] for c in cols] for r in rows]

    # Show the complete solution first
    print("=======full board========")
    print_board(board_tmp)

    # Remove cells to create the puzzle
    squares = side * side
    if num == 0:
        empties = squares * 3 // 4
    else:
        empties = 81 - num
    # Set chosen positions to 0 (empty)
    for p in sample(range(squares), empties):
        board_tmp[p // side][p % side] = 0

    return board_tmp


# Print the board with grid dividers
def print_board(bo):
    for i in range(len(bo)):
        # Print horizontal divider every 3 rows
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")
        for j in range(len(bo[0])):
            # Print vertical divider every 3 columns
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")
    print("")


# Check if placing num at pos is valid
def possible(bo, pos, num):
    # Check the row for duplicates
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check the column for duplicates
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check the 3x3 box for duplicates
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False
    return True


# Find the next empty (zero) cell
def next_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return i, j


# Solve the board using backtracking recursion
def solve(bo):
    slot = next_empty(bo)
    if not slot:
        return True
    else:
        row, col = slot
    # Try each number 1–9 in the empty cell
    for i in range(1, 10):
        if possible(bo, (row, col), i):
            bo[row][col] = i

            # Recurse; if solved, bubble True up
            if solve(bo):
                return True

            # Undo the placement and try next number
            bo[row][col] = 0
    return False


# Define the board to solve (all zeros = fully generated)
board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]

# Generate a random puzzle board
board = generate_board(0)

# Display the unsolved puzzle
print("======solvable board=====")
print_board(board)

# Solve the puzzle in-place
solve(board)

# Display the solved board
print("======solved board=======")
print_board(board)
