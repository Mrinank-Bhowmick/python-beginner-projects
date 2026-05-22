# Tetris Game

A classic Tetris game built with Pygame. Falling tetrominoes can be moved, rotated, and hard-dropped; full lines are cleared for points, and the game ends when pieces stack to the top.

## Example

1. The Pygame window opens showing an empty Tetris grid with the current score displayed.
2. A random tetromino (e.g. an L-piece) appears at the top of the grid and falls downward.
3. Press the left/right arrow keys to move the piece horizontally, or the up arrow to rotate it.
4. Press the down arrow to soft-drop the piece faster.
5. When a full horizontal line is formed, it is cleared and the score increases.
6. The game ends when pieces stack up and reach the top of the grid.

## How to run on localhost

```
pip install pygame
python tetrisGame.py
```

## Dependencies

pygame
