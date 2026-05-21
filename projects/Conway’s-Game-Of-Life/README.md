# Conway's Game of Life

An implementation of Conway's Game of Life cellular automaton, animated with matplotlib. Supports random grids as well as glider and Gosper glider gun demos via command-line flags.

## How to run

```
pip install numpy matplotlib
python conwaygame.py
```

Optional flags: `--grid-size`, `--interval`, `--glider`, `--gosper`, `--mov-file`.

## Dependencies

- `numpy`
- `matplotlib`

## Pyodide-runnable

No — it relies on `matplotlib` interactive animation (`plt.show`) and command-line argument parsing, which do not work in the Pyodide browser environment.
