# File Organizer

A command-line tool that organizes a directory by file type. It scans the given directory and moves files into category folders (Music, Videos, Documents, Pictures, etc.) based on their extensions.

## How to run

```
python main.py <directory_path> [-v]
```

`-v` enables verbose output.

## Dependencies

Standard library only (`argparse`, `os`, `logging`, `shutil`).

## Pyodide-runnable

No — it walks and moves files on the real filesystem, which is not available in a browser sandbox.
