# Connect Four

A two-player Connect Four game with a graphical board rendered using pygame; players drop colored pieces by clicking columns until one connects four in a row.

## Example

1. The pygame window opens showing a 7-column by 6-row blue grid with black holes.
2. Player 1 (red) moves the mouse over the board — a red circle tracks the cursor along the top row.
3. Player 1 clicks a column; a red piece drops to the lowest available row in that column.
4. Player 2 (yellow) clicks a column; a yellow piece drops.
5. Players alternate until one connects four pieces horizontally, vertically, or diagonally.
6. The winning message (e.g. "Player 1 wins!!") appears in red at the top of the window, then the game pauses for 3 seconds and closes.

## How to run on localhost

```
pip install pygame numpy
python main.py
```

## Dependencies

- `pygame`
- `numpy`
