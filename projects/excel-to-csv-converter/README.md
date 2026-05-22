# Excel to CSV Converter

Converts every sheet of every `.xlsx` file in a folder into separate CSV files.

## Example

Given a folder containing `sales_data.xlsx` with two sheets named `Q1` and `Q2`, running the script produces:

```
sales_data_Q1.csv
sales_data_Q2.csv
```

Each CSV file contains the rows and columns from its corresponding sheet.

## How to run on localhost

```
pip install openpyxl
python excelToCsv.py
```

## Dependencies

- `openpyxl`
- `csv`, `os` (standard library)
