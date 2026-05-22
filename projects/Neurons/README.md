# Neurons

A terminal animation that simulates "neurons" on a grid. Each neuron randomly dies or moves in one of four directions on every tick, producing an evolving pattern printed to the terminal.

## Example

The terminal fills with a live-updating grid of block characters (`██`) representing neurons. On each tick every neuron either dies or moves one cell in a random direction, producing a shifting, organic-looking pattern that runs until all neurons have died, then restarts.

```text
                                                        ██
              ██
                                    ██
        ██                ██
                    ██
```

## How to run on localhost

```
python main.py
```

## Dependencies

Standard library only.
