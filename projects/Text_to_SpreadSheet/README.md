# Text to Spreadsheet

A script that reads every `.txt` file in a directory and writes each file's lines into a separate column of an Excel worksheet, saving the result as an `.xlsx` file.

## How to run

```
pip install openpyxl
python textToSheet.py
```

## Dependencies

openpyxl

## Pyodide-runnable

No — it walks the real local directory with `os.listdir()` and writes an `.xlsx` file to disk.
