# Sudoku Solver

A console Sudoku generator and solver. It randomly generates a valid Sudoku board, removes cells to create a puzzle, then solves it with a backtracking algorithm, printing the full, unsolved, and solved boards.

## Example

```text
=======full board========
5 3 4  | 6 7 8  | 9 1 2
6 7 2  | 1 9 5  | 3 4 8
1 9 8  | 3 4 2  | 5 6 7
- - - - - - - - - - - - -
8 5 9  | 7 6 1  | 4 2 3
4 2 6  | 8 5 3  | 7 9 1
7 1 3  | 9 2 4  | 8 5 6
- - - - - - - - - - - - -
9 6 1  | 5 3 7  | 2 8 4
2 8 7  | 4 1 9  | 6 3 5
3 4 5  | 2 8 6  | 1 7 9

======solvable board=====
5 3 0  | 6 7 0  | 9 1 0
0 7 2  | 1 9 5  | 3 4 8
1 0 8  | 3 0 2  | 5 6 7
- - - - - - - - - - - - -
...

======solved board=======
5 3 4  | 6 7 8  | 9 1 2
6 7 2  | 1 9 5  | 3 4 8
...
```

## How to run on localhost

```
python main.py
```

## Dependencies

Standard library only.
