# Inventory Management

A simple supermarket inventory system with a Tkinter login window and add/display/search/update/delete operations backed by a MySQL database.

## Example

1. Run `python main.py`. A Tkinter login window titled "Authorised Login Only" opens.
2. Enter username `Admin` and password `1234`, then click Submit.
3. The main "Welcome to Super Market" inventory window appears with buttons: Add, Search, Update, Display, Delete, and Exit.
4. Clicking **Add** prompts in the console:
   ```
   Enter the product id: 101
   Enter the product name: Apple
   Enter the product cost: 50
   Enter the product quantity: 200
   Data Inserted successfully
   ```
5. Clicking **Display** prints all rows from the `inventory` table to the console.

## How to run on localhost

```
pip install -r requirements.txt
python main.py
```

Requires a local MySQL server with a `records` database and an `inventory` table.

## Dependencies

tkinter (standard library), mysql-connector-python.
