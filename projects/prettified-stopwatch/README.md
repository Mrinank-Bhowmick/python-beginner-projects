# Prettified Stopwatch

A console stopwatch that records lap times. Press ENTER to start, ENTER again to mark each lap, and Ctrl-C to stop. Results are copied to the system clipboard.

## How to run

```sh
pip install pyperclip
python stopwatch.py
```

## Dependencies

- pyperclip
- time (standard library)

## Pyodide-runnable

No - it relies on `pyperclip` for system clipboard access, which is not available in the Pyodide sandbox.
