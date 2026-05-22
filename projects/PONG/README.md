# PONG

A single-player Pong game built with `pygame`. It features a difficulty menu (Easy / Medium / Hard), an AI-controlled opponent paddle, sound effects, and a score counter.

## Example

1. A 1000x800 window titled "Pong" opens showing a "Difficulty" menu with three buttons: EASY, MEDIUM, and HARD.
2. Click EASY to start a game. The screen shows two paddles, a centre dividing strip, and the ball appears after a 3-second countdown.
3. Press the Up / Down arrow keys to move your (right) paddle; the AI opponent controls the left paddle.
4. The ball bounces off walls and paddles with sound effects. Each time it passes a paddle, the scoring player's counter increments in the centre of the screen.
5. Press Escape at any time to return to the difficulty menu.

## How to run on localhost

```
pip install pygame
python main.py
```

Run from the `PONG` directory so the `assets/` files are found.

## Dependencies

- pygame
