# Sudoku Solver (GUI)

A Pygame-based Sudoku game. It generates a random grid you can play interactively, supports hints, tracks wrong answers and elapsed time, and can visually solve the puzzle with a backtracking animation.

## Example

1. The window opens showing a 9×9 Sudoku grid with some cells pre-filled and the rest blank.
2. Click an empty cell to select it, then type a digit (1–9) to place your answer.
3. A wrong answer increments the "Strikes" counter displayed at the top.
4. Press the spacebar or click the Solve button to watch the backtracking algorithm fill in the remaining cells with a visual animation.
5. Elapsed time is shown in the top-right corner throughout the game.

## How to run on localhost

```
pip install pygame
python SudokuGUI.py
```

## Dependencies

pygame
