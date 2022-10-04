import os
import random
import sys
import time
from enum import Enum
from shutil import get_terminal_size


TICKS_PER_SECOND = 60


def clear() -> None:
    """Clear the terminal based on OS."""
    if sys.platform == "nt":
        os.system("cls")
    else:
        os.system("clear")


class Direction(Enum):
    """Mapping of direction to int."""

    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3


class Empty(str):
    """String subclass to return character representing empty space."""

    CHAR = "  "

    def __new__(cls) -> str:
        return str.__new__(cls, cls.CHAR)


class Neuron(str):
    """String subclass to return character representing a neuron."""

    CHAR = "██"
    CHANCE_OF_DEATH = 35

    def __new__(cls) -> str:
        return str.__new__(cls, cls.CHAR)


class Grid:
    """Class to store grid."""

    def __init__(self, width, height) -> None:
        """Initialise the grid with empty cells."""
        self._grid = [[Empty() for _ in range(width)] for _ in range(height)]

    def __str__(self) -> str:
        """Return the string representation of the grid."""
        return "\n".join(["".join(row) for row in self._grid])

    @property
    def neurons(self) -> tuple[tuple[Neuron, tuple[int, int]]]:
        """Return 2D tuple of Neurons."""
        return tuple(
            (element, (x, y))
            for y, row in enumerate(self._grid)
            for x, element in enumerate(row)
            if isinstance(element, Neuron)
        )

    def set_neuron(self, x, y) -> None:
        """Set x, y to a Neuron."""
        self._grid[y][x] = Neuron()

    def tick(self) -> None:
        """Randomly kill or move all Neurons."""
        for neuron_data in self.neurons:
            neuron = neuron_data[0]
            x, y = neuron_data[1]

            if random.randint(1, 100) <= Neuron.CHANCE_OF_DEATH:
                self._grid[y][x] = Empty()
                continue

            direction = random.choice(list(Direction))
            if direction == Direction.UP:
                y -= 1
            elif direction == Direction.RIGHT:
                x += 1
            elif direction == Direction.DOWN:
                y += 1
            elif direction == Direction.LEFT:
                x -= 1
            try:
                self._grid[y][x] = Neuron()
            except IndexError:
                pass


def main() -> None:
    """Run the program with two example Neurons."""
    # Set the grid size proportional to the terminal
    width, height = get_terminal_size()
    grid = Grid(width // len(Neuron.CHAR), height)
    grid.set_neuron(15, 15)  # Example placement
    grid.set_neuron(35, 35)
    while grid.neurons:
        clear()
        print(grid)  # Output the string representation of the grid
        grid.tick()
        time.sleep(1 / TICKS_PER_SECOND)


if __name__ == "__main__":
    while True:
        main()
