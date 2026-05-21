# Merge PDFs

A CLI tool that lists PDF files in a directory, lets you include/exclude files interactively, and merges the selected PDFs into a single file.

## How to run

```
pip install -r requirements.txt
python main.py [directory]
```

## Dependencies

pikepdf.

## Pyodide-runnable
No — it walks the real file system and uses pikepdf to read and write PDF files on disk.
