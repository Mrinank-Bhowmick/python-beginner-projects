# === Neurons · annotated for the pyBegin playground ===
# A beginner-friendly walkthrough — original project by @Zedeldi.

import random
import time
from enum import Enum
from shutil import get_terminal_size


TICKS_PER_SECOND = 60


# Enum listing the four movement directions
class Direction(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3


# Represents an empty cell on the grid
class Empty(str):
    CHAR = "  "

    def __new__(cls) -> str:
        return str.__new__(cls, cls.CHAR)


# Represents a living neuron cell on the grid
class Neuron(str):
    CHAR = "██"
    CHANCE_OF_DEATH = 35

    def __new__(cls) -> str:
        return str.__new__(cls, cls.CHAR)


# Stores the 2-D grid of cells
class Grid:
    # Build the grid filled with empty cells
    def __init__(self, width, height) -> None:
        self._grid = [[Empty() for _ in range(width)] for _ in range(height)]

    # Return the grid as a printable string
    def __str__(self) -> str:
        return "\n".join(["".join(row) for row in self._grid])

    # Collect all neuron positions from the grid
    @property
    def neurons(self) -> tuple[tuple[Neuron, tuple[int, int]]]:
        return tuple(
            (element, (x, y))
            for y, row in enumerate(self._grid)
            for x, element in enumerate(row)
            if isinstance(element, Neuron)
        )

    # Place a neuron at the given coordinates
    def set_neuron(self, x, y) -> None:
        self._grid[y][x] = Neuron()

    # Advance one tick: kill or move each neuron randomly
    def tick(self) -> None:
        for neuron_data in self.neurons:
            neuron = neuron_data[0]
            x, y = neuron_data[1]

            # Randomly kill the neuron based on its death chance
            if random.randint(1, 100) <= Neuron.CHANCE_OF_DEATH:
                self._grid[y][x] = Empty()
                continue

            # Move the neuron in a random direction
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


# Set up two starter neurons and run the simulation
def main() -> None:
    # Size the grid to fit the terminal window
    width, height = get_terminal_size()
    grid = Grid(width // len(Neuron.CHAR), height)
    grid.set_neuron(15, 15)
    grid.set_neuron(35, 35)
    # Print and update the grid until all neurons die
    while grid.neurons:
        print(grid)
        grid.tick()
        time.sleep(1 / TICKS_PER_SECOND)


if __name__ == "__main__":
    # Restart automatically when all neurons are gone
    while True:
        main()
