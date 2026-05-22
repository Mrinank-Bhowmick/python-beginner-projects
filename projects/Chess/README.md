# Chess

A two-player chess game built with Pygame. It renders the board and pieces in a desktop window using the image assets in the `Assets/` folder.

## Example

1. Run `python main.py`. A Pygame window opens showing an 8×8 chessboard with all pieces in their starting positions, rendered using the image assets from the `Assets/` folder.
2. Click a piece to select it; valid move squares are highlighted on the board.
3. Click a highlighted square to move the selected piece there. The turn passes to the other player.
4. Continue taking turns until a player's king is in checkmate or the game ends.

## How to run on localhost

```
pip install pygame
python main.py
```

## Dependencies

- pygame
