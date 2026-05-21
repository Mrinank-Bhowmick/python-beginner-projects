# Health Management System

A console-based health log. It lets you log exercise or food entries (timestamped) for one of three users into text files, and retrieve those logs later.

## How to run

```
python health.py
```

## Dependencies

Standard library only (`datetime`).

## Pyodide-runnable

No — it reads and appends to real files on disk, which is not available in a browser sandbox.
