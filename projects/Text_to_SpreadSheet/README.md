# Text to Spreadsheet

A script that reads every `.txt` file in a directory and writes each file's lines into a separate column of an Excel worksheet, saving the result as an `.xlsx` file.

## Example

Suppose the current directory contains `notes.txt` and `tasks.txt`:

```
notes.txt       tasks.txt
---------       ---------
Buy milk        Fix bug #42
Call Alice      Write tests
```

After running the script, `text-to-cols.xlsx` is created with:

```
Column A      Column B
--------      --------
Buy milk      Fix bug #42
Call Alice    Write tests
```

Each `.txt` file becomes one column in the Excel worksheet.

## How to run on localhost

```
pip install openpyxl
python textToSheet.py
```

## Dependencies

openpyxl
