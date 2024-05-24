def rotate90(grid):
    """Rotates a grid 90 degrees
    Args:
        grid (list): a 2d list representing a grid
    Returns:
        grid (list): rotated copy of a 2d grid
    """
    return list(zip(*grid[::-1]))


def print2DGrid(grid):
    """Prints a 2D grid
    Args:
        grid (list): 2D grid
    Returns:
        None
    """
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            print(grid[row][col], end="")

        print()


if __name__ == "__main__":

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

    gridRotated = rotate90(grid)
    print2DGrid(gridRotated)
