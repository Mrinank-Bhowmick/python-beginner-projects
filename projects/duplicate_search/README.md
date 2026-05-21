# Duplicate File Search

Recursively searches a directory for duplicate files by comparing MD5 checksums, then interactively lets you delete unwanted copies.

## How to run

```
python main.py [directory]
```

If no directory is given, it searches the current directory.

## Dependencies

Standard library only (`hashlib`, `sys`, `collections`, `pathlib`).

## Pyodide-runnable

No — it walks and deletes files on the real filesystem, which is not meaningful in the Pyodide browser sandbox.
