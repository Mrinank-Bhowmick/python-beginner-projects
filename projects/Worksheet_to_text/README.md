# Worksheet to Text

Reads an Excel workbook and writes each column of data into its own plain-text file (`text-1.txt`, `text-2.txt`, ...).

## Example

Given a `worksheet.xlsx` with three columns, running `python sheetToTextFile.py` creates three text files:

```
text-1.txt  — contents of column A
text-2.txt  — contents of column B
text-3.txt  — contents of column C
```

Each file contains the cell values from its column written consecutively with no delimiter.

## How to run on localhost

```bash
pip install openpyxl
python sheetToTextFile.py
```

## Dependencies

- openpyxl
