# Turtle Pattern

Draws a random walking pattern using Python's `turtle` graphics. A turtle moves in randomly chosen directions with random pen colors for 200 steps, producing a colorful abstract pattern.

## Example

1. A Turtle graphics window opens with a white canvas.
2. The turtle begins drawing from the center, moving 30 pixels at a time in a randomly chosen direction (forward, backward, left 90°, or right 90°).
3. Each step uses a new random RGB pen color, producing a multi-colored path.
4. After 200 steps the drawing is complete and the window stays open.
5. Click anywhere on the window to close it.

## How to run on localhost

```bash
python randomPattern.py
```

## Dependencies

Standard library only (`turtle`, `random`, `time`).
