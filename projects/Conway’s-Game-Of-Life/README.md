# Conway's Game of Life

An implementation of Conway's Game of Life cellular automaton, animated with matplotlib. Supports random grids as well as glider and Gosper glider gun demos via command-line flags.


## Example

1. Run with no flags: a 100x100 window opens showing a randomly populated grid that evolves each frame according to Conway's rules.
2. Run `python conwaygame.py --glider` to open a blank grid with a single glider pattern placed at position (1, 1) and watch it travel diagonally.
3. Run `python conwaygame.py --gosper` to start with a Gosper Glider Gun that continuously fires gliders across the grid.
4. Pass `--grid-size 50 --interval 100` to use a smaller 50x50 grid updated every 100 ms.
5. Pass `--mov-file output.mp4` to save the animation to a video file instead of displaying it.

## How to run on localhost

```
pip install numpy matplotlib
python conwaygame.py
```

Optional flags: `--grid-size`, `--interval`, `--glider`, `--gosper`, `--mov-file`.

## Dependencies

- `numpy`
- `matplotlib`
