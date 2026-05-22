# Budget Manager

A personal budget manager desktop app. It lets you add and delete transactions, categorise them, and view a running balance, storing everything in a local SQLite database.

## Example

1. Run `python main.py`. The "Personal Budget Manager" window opens with fields for Date, Description, Amount ($), and Category, plus a transaction list and a balance display showing `Current Balance: $0.00`.
2. Fill in the fields — e.g. Date: `2024-01-15`, Description: `Salary`, Amount: `3000`, Category: `Income` — then click **Add Transaction**. A confirmation dialog appears and the new entry is shown in the list.
3. Add an expense: Date: `2024-01-16`, Description: `Groceries`, Amount: `-120`, Category: `Food`. The balance label updates to reflect the running total.
4. Click a transaction in the list to select it, then click **Delete Transaction** to remove it. The balance recalculates immediately.

## How to run on localhost

```
python main.py
```

## Dependencies

Standard library only (`tkinter`, `sqlite3`).
