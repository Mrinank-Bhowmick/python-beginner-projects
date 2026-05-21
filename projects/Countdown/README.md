# Countdown Timer

A simple console countdown timer: enter a number of seconds and it counts down in `MM:SS` format, printing "Time Up" when finished.

## How to run

```
python countdown.py
```

## Dependencies

Standard library only (`time`).

## Pyodide-runnable

Yes — it uses only `time` and `print`/`input`; note that `time.sleep` blocks, so the countdown updates will appear all at once at the end in a browser console.
