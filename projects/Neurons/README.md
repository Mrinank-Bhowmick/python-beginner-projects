# Neurons

A terminal animation that simulates "neurons" on a grid. Each neuron randomly dies or moves in one of four directions on every tick, producing an evolving pattern printed to the terminal.

## How to run

```
python main.py
```

## Dependencies

Standard library only.

## Pyodide-runnable

Yes — after a small edit removing the `os.system` terminal-clear (and the now-unused `os`/`sys` imports), it is a pure-stdlib program that only prints to the console.
