# Organize Directory

A file organiser. Given a directory path, it sorts the files inside it into category folders (images, music, video, executables, archives, torrent, documents, code, design files) based on their file extensions.

## How to run

```
python organizer.py
```

## Dependencies

Standard library only (`os`, `shutil`).

## Pyodide-runnable

No — it walks and moves files on the real filesystem, which the browser sandbox does not provide.
