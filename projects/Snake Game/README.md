# Snake Game

A classic Snake game built with Pygame. The player controls a snake that grows as it eats food, tracking a score and a high score, with game-over and play-again screens.

## Example

1. Run `python src/main.py`. A Pygame window opens showing the snake and a food item.
2. Use the arrow keys to steer the snake toward the food. Each food eaten increases the score by 1 and grows the snake.
3. If the snake hits a wall or its own body the game-over screen appears. If you set a new high score it is displayed and saved to `high_score.json`.
4. A "Play Again?" prompt appears — press Y or Enter to restart, N or Escape to quit.

## How to run on localhost

```
pip install pygame
python src/main.py
```

## Dependencies

pygame
