# Analog Clock

A Tkinter program that draws a working analog clock on a canvas — face, hour
numbers, and moving hour/minute/second hands. The clock always starts at
10 o'clock and ticks forward once per second.

![img.png](img.png)

## Example

1. Run `python analog_clock.py`. A window opens showing a circular clock face
   with hour numbers 1–12 drawn around the edge.
2. The clock starts at 10 o'clock with all three hands positioned accordingly.
3. Every second the second hand advances one tick; the minute and hour hands
   move proportionally.
4. Close the window to exit.

## How to run on localhost

```bash
python analog_clock.py
```

## Dependencies

- `tkinter` — GUI (ships with the standard Python installer)
- `math` — standard library
