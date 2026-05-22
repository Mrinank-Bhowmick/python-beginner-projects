# Flappy Bird Game

A clone of the classic Flappy Bird game built with Pygame. Tap the space bar to flap the bird through gaps in the pipes; the game tracks score and high score.

## Example

1. The game window (288×512) opens showing a night-sky background, a scrolling floor, and a blue bird in the centre.
2. Press space bar to flap the bird upward; gravity pulls it down continuously.
3. Green pipes scroll in from the right with gaps to fly through. The score increments while the bird stays alive.
4. If the bird hits a pipe or the floor, a hit sound plays and the game-over screen appears showing `Score:` and `High Score:`.
5. Press space bar again to restart with the score reset to 0.

## How to run on localhost

```
pip install pygame
python main.py
```

## Dependencies

- pygame
