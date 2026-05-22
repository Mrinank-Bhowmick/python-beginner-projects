# Prettified Stopwatch

A console stopwatch that records lap times. Press ENTER to start, ENTER again to mark each lap, and Ctrl-C to stop. Results are copied to the system clipboard.

## Example

```text
Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch. Press Ctrl-C to quit.

Started.

Lap #  1:  3.14  (  3.14)
Lap #  2:  7.82  (  4.68)
Lap #  3: 12.05  (  4.23)
^C
Done.
Results available in clipboard
```

Each ENTER press records a lap. The first column is total elapsed time, the second (in parentheses) is the individual lap time. All results are copied to the clipboard on exit.

## How to run on localhost

```sh
pip install pyperclip
python stopwatch.py
```

## Dependencies

- pyperclip
- time (standard library)
