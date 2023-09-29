import sqlite3

# Connect to the database
conn = sqlite3.connect("expenses.db")
cursor = conn.cursor()

# Define SQL statements
create_table_sql = """CREATE TABLE IF NOT EXISTS expenses (id INTEGER PRIMARY KEY AUTOINCREMENT, date TEXT, description TEXT, amount REAL)"""
insert_expense_sql = "INSERT INTO expenses (date, description, amount) VALUES (?, ?, ?)"
select_expenses_sql = "SELECT * FROM expenses ORDER BY date;"
delete_expense_by_id_sql = "DELETE FROM expenses WHERE id=?"
update_expense_by_id_sql = "UPDATE expenses SET description=? WHERE id=?"

# Check if the database exists, create it if not
if not conn.execute(
    "SELECT name FROM sqlite_master WHERE type='table' AND name='expenses';"
).fetchone():
    cursor.execute(create_table_sql)
    conn.commit()


def add_expense():
    global cursor

    # Get input from user
    print("Enter date (YYYY-MM-DD): ")
    date = input().split()[0] + "-01"
    print("Enter description: ")
    description = input()
    print("Enter amount: ")
    amount = float(input())

    try:
        cursor.execute(insert_expense_sql, (date, description, amount))
        conn.commit()
        print("Expense added successfully.")
    except Exception as e:
        print("Error adding expense: {}".format(e))


def delete_expense():
    global cursor

    # Get ID from user
    print("Enter ID to delete: ")
    id = int(input())

    try:
        cursor.execute(delete_expense_by_id_sql, (id,))
        conn.commit()
        print("Expense deleted successfully.")
    except Exception as e:
        print("Error deleting expense: {}".format(e))


def update_expense():
    global cursor

    # Get ID and new description from user
    print("Enter ID to update: ")
    id = int(input())
    print("Enter new description: ")
    description = input()

    try:
        cursor.execute(update_expense_by_id_sql, (description, id))
        conn.commit()
        print("Expense updated successfully.")
    except Exception as e:
        print("Error updating expense: {}".format(e))


def view_expenses():
    # Fetch and display expenses
    expenses = conn.execute(select_expenses_sql).fetchall()
    if not expenses:
        print("No expenses recorded yet.")
    else:
        print("Expenses:")
        for expense in expenses:
            print(
                f"ID: {expense[0]}, Date: {expense[1]}, Description: {expense[2]}, Amount: Rs: {expense[3]}"
            )


def total_expenses():
    # Calculate and display total expenses
    total = conn.execute("SELECT SUM(amount) FROM expenses;").fetchone()[0]
    print(f"Total expenses: {total}$")


def main_menu():
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expenses")
        print("4. Delete Expense")
        print("5. Update Expense Description")
        print("6. Quit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expenses()
        elif choice == "4":
            delete_expense()
        elif choice == "5":
            update_expense()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main_menu()

conn.close()
