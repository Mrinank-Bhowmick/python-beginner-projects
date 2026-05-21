# Rename Images

A console tool that walks a given directory and lets the user interactively rename each image file (jpg, png, jpeg).

## How to run

```sh
python rename_images.py
```

## Dependencies

Standard library only (uses `os`).

## Pyodide-runnable

No - it walks and renames files on the real filesystem with `os.listdir`/`os.rename`, which is not available in the browser sandbox.
