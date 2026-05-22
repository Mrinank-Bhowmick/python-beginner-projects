# Ping Pong

A two-player Pong game built with Python's `turtle` graphics. Player A uses `W`/`S` and Player B uses the arrow keys to move their paddles; the ball bounces around the screen and the score updates on goals.

## Example

1. An 800x600 green window titled "The Pong Game" opens with two white paddles and a red ball.
2. The score display at the top reads "Player A: 0                    Player B: 0".
3. Player A presses `W` / `S` to move the left paddle up or down; Player B uses the Up / Down arrow keys for the right paddle.
4. The ball bounces off the top and bottom walls and off each paddle.
5. When the ball passes the right edge, Player A scores a point; when it passes the left edge, Player B scores. The score display updates immediately.
6. The ball resets to the centre after each goal and play continues.

## How to run on localhost

```
python ping_pong.py
```

## Dependencies

Standard library only (`turtle`).
