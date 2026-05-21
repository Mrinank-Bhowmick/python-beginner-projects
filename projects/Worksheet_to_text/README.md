# Worksheet to Text

Reads an Excel workbook and writes each column of data into its own plain-text file (`text-1.txt`, `text-2.txt`, ...).

## How to run

```bash
pip install openpyxl
python sheetToTextFile.py
```

## Dependencies

- openpyxl

## Pyodide-runnable

No — it reads a local `worksheet.xlsx` file from the real filesystem, which is not available in the Pyodide browser sandbox.
