# Subtitle Synchronizer

A console tool that shifts all timestamps in an SRT subtitle file by a given number of milliseconds, reading from `input.srt` and writing the synchronized result to `output.srt`.

## How to run

```
python main.py
```

Place an `input.srt` file in the same folder before running.

## Dependencies

Standard library only.

## Pyodide-runnable

No — it reads `input.srt` and writes `output.srt` from the real local filesystem, which is not accessible under Pyodide.
