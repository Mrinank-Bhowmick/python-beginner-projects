import curses
from curses import newwin, wrapper
from importlib.util import find_spec
from operator import ne
import queue
import time

maze = [
    ["#", "O", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "X", "#"],
]

maze_1 = [
    ["#", "#", "#", "#", "O", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", "#", "#", "#", "#", "X", "#", "#", "#"],
]


# to print maze in various stages as algo tries to find the path
def print_maze(maze_1, stdscr, path=[]):
    GREEN = curses.color_pair(1)
    RED = curses.color_pair(2)

    for i, row in enumerate(maze_1):
        for j, value in enumerate(row):
            if (i, j) in path:
                stdscr.addstr(i, j * 2, "X", RED)
            else:
                stdscr.addstr(i, j * 2, value, GREEN)


def find_path(maze_1, stdscr):
    start = "O"
    end = "X"

    start_pos = start_location(maze_1, start)

    q = queue.Queue()
    q.put((start_pos, [start_pos]))

    visited = set()

    while not q.empty():
        current_pos, path = q.get()
        row, col = current_pos

        stdscr.clear()
        print_maze(maze_1, stdscr, path)
        time.sleep(0.2)
        stdscr.refresh()

        if maze_1[row][col] == end:
            return path

        neighbours = find_neighbour(maze_1, row, col)

        for neighbour in neighbours:
            if neighbour in visited:
                continue

            r, c = neighbour

            if maze[r][c] == "#":
                continue

            new_path = path + [neighbour]
            q.put((neighbour, new_path))
            visited.add(neighbour)


def find_neighbour(maze_1, row, col):
    neighbours = []

    if row > 0:
        neighbours.append((row - 1, col))
    if row < len(maze_1) - 1:
        neighbours.append((row + 1, col))
    if col > 0:
        neighbours.append((row, col - 1))
    if col < len(maze_1[0]) - 1:
        neighbours.append((row, col + 1))

    return neighbours


# to find the start location in maze
def start_location(maze_1, start):
    for i, row in enumerate(maze_1):
        for j, value in enumerate(row):
            if value == start:
                return i, j
    return None


def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

    find_path(maze_1, stdscr)
    stdscr.getch()


wrapper(main)
