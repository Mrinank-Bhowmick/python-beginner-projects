# Excel to CSV Converter

Converts every sheet of every `.xlsx` file in a folder into separate CSV files.

## How to run

```
pip install openpyxl
python excelToCsv.py
```

## Dependencies

- `openpyxl`
- `csv`, `os` (standard library)

## Pyodide-runnable

No — it scans the real filesystem for Excel files and writes CSV files to disk.
