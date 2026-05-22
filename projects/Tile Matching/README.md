# Tile Matching Game

A memory tile-matching game built with Tkinter. Click pairs of tiles to reveal hidden colors and match them all before the 60-second timer runs out, with a live score and attempts counter.

## Example

1. The Tkinter window opens with a 4×4 grid of gray tiles, a "Score: 0" label, an "Attempts: 0" label, and a "Time: 60" countdown.
2. Click any gray tile to reveal its hidden color (e.g. lightcoral).
3. Click a second tile — if its color matches the first, both stay revealed and the score increments.
4. If the colors differ, both tiles flip back to gray after a brief pause and the attempt counter increases.
5. Match all 8 pairs before the timer reaches zero to win; a congratulations dialog appears.
6. Click "Reset Game" to start a new game or "Exit" to close the window.

## How to run on localhost

```bash
python tile_matching.py
```

## Dependencies

Standard library only (`tkinter`, `random`).
