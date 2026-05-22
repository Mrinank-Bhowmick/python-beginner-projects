# Space Battle

A Space Invaders style game built with Pygame. Move a UFO around the screen, shoot down descending enemies, and play with sound effects and background music.

## Example

1. Run `python main.py`. An 800×600 Pygame window titled "Space invaders" opens with a space background and background music.
2. Use the arrow keys to move your UFO around the screen; press Space to fire a bullet upward.
3. Ten enemy UFOs descend in rows, bouncing left and right and moving down each time they reach a screen edge.
4. Each enemy hit increments the score displayed in the top-left corner (`score:1`, `score:2`, …).
5. If an enemy reaches the bottom of the screen or collides with the player, a "Game-Over" message appears. Press 1 to restart.

## How to run on localhost

```
pip install pygame
python main.py
```

## Dependencies

pygame
