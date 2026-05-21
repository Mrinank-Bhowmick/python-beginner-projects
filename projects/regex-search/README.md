# Regex Search

A console tool that prompts for a regular expression and prints every line in the `.txt` files of a folder that matches it.

## How to run

```sh
python regex-search.py
```

## Dependencies

Standard library only (uses `os` and `re`).

## Pyodide-runnable

No - it walks the real filesystem with `os.listdir` to find and open `.txt` files on disk, which is not available in the browser sandbox.
