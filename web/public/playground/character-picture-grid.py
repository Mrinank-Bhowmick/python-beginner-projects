# === Character Picture Grid · annotated for the pyBegin playground ===
# A beginner-friendly walkthrough — original project by @ibra-kdbra.

# Rotate a 2D grid 90 degrees clockwise
def rotate90(grid):
    return list(zip(*grid[::-1]))


# Print every row of a 2D grid
def print2DGrid(grid):
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            print(grid[row][col], end="")

        print()


if __name__ == "__main__":

    # Define the character picture as a 2D list
    grid = [
        [".", ".", ".", ".", ".", "."],
        [".", "O", "O", ".", ".", "."],
        ["O", "O", "O", "O", ".", "."],
        ["O", "O", "O", "O", "O", "."],
        [".", "O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "."],
        ["O", "O", "O", "O", ".", "."],
        [".", "O", "O", ".", ".", "."],
        [".", ".", ".", ".", ".", "."],
    ]

    # Rotate the grid and print the result
    gridRotated = rotate90(grid)
    print2DGrid(gridRotated)
