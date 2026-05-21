# Find Unneeded Files

Walks a folder tree and reports files or subfolders whose size exceeds a given threshold, to help locate large items that could be cleaned up.

## How to run

```
python find_unneeded.py
```

## Dependencies

Standard library only (`os`).

## Pyodide-runnable

No — it walks the real filesystem and reads file sizes, which is not available in a browser sandbox.
