import sqlite3
import csv

# Connect to the database
conn = sqlite3.connect("expenses.db")
cursor = conn.cursor()

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


# Define SQL statements


def add_expense():
    global cursor

    # Get input from user
    print("Enter date (YYYY-MM-DD): ")
    date = input().split()[0]
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
    if is_empty() == True:
        print("No expenses recorded yet.")
    else:
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
    if is_empty() == True:
        print("No expenses recorded yet.")
    else:
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


# defining function for exporting to csv
def print_csv():
    # opening csv file
    with open("expense.csv", "w") as csvfile:
        #
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(
            ["ID", "DATE", "Desc", "description"]
        )  # To Define heading of rows of csv
        csvwriter.writerows(cursor)
        expenses = conn.execute(select_expenses_sql).fetchall()
        for i in expenses:
            print(i)
            csvwriter.writerow(i)  # writing querys to csv
        total = conn.execute("SELECT SUM(amount) FROM expenses;").fetchone()[
            0
        ]  # For total Expenses
        csvwriter.writerow(["", "", "Total Expenses:", total])  # Printing to CSV
        
def data_filter():
    print("Select Filter Option:")
    print("1. Filter by Date")
    print("2. Filter by Amount")
    
    option = input("Enter your choice (1 or 2): ")
    
    if option == "1":
        print("Select Date Range:")
        print("1. Today")
        print("2. Past Month")
        print("3. Past Year")
        
        date_option = input("Enter your choice (1, 2, or 3): ")
        if date_option == "1":
            # Filter for today
            filter_condition = "date = date('now')"
        elif date_option == "2":
            # Filter for past month
            filter_condition = "date >= date('now', '-1 month')"
        elif date_option == "3":
            # Filter for past year
            filter_condition = "date >= date('now', '-1 year')"
        else:
            print("Invalid input.")
            return
    elif option == "2":
        print("Select Amount Range:")
        print("1. 0 to 500")
        print("2. 500 to 2500")
        print("3. 2500 and above")
        
        amount_option = input("Enter your choice (1, 2, or 3): ")
        if amount_option == "1":
            # Filter for 0 to 500
            filter_condition = "amount >= 0 AND amount <= 500"
        elif amount_option == "2":
            # Filter for 500 to 2500
            filter_condition = "amount > 500 AND amount <= 2500"
        elif amount_option == "3":
            # Filter for 2500 and above
            filter_condition = "amount > 2500"
        else:
            print("Invalid input.")
            return
    else:
        print("Invalid input.")
        return
    # Writing a single line of sql code which takes the filter condition and returns data accordingly.
    select_expenses_sql = f"SELECT * FROM expenses WHERE {filter_condition} ORDER BY date;"
    expenses = conn.execute(select_expenses_sql).fetchall()
    
    if not expenses:
        print("No expenses recorded based on the selected filter.")
    else:
        print("Filtered Expenses:")
        for expense in expenses:
            print(
                f"ID: {expense[0]}, Date: {expense[1]}, Description: {expense[2]}, Amount: Rs: {expense[3]}"
            )


def data_filter():
    print("Select Filter Option:")
    print("1. Filter by Date")
    print("2. Filter by Amount")

    option = input("Enter your choice (1 or 2): ")

    if option == "1":
        print("Select Date Range:")
        print("1. Today")
        print("2. Past Month")
        print("3. Past Year")

        date_option = input("Enter your choice (1, 2, or 3): ")
        if date_option == "1":
            # Filter for today
            filter_condition = "date = date('now')"
        elif date_option == "2":
            # Filter for past month
            filter_condition = "date >= date('now', '-1 month')"
        elif date_option == "3":
            # Filter for past year
            filter_condition = "date >= date('now', '-1 year')"
        else:
            print("Invalid input.")
            return
    elif option == "2":
        print("Select Amount Range:")
        print("1. 0 to 500")
        print("2. 500 to 2500")
        print("3. 2500 and above")

        amount_option = input("Enter your choice (1, 2, or 3): ")
        if amount_option == "1":
            # Filter for 0 to 500
            filter_condition = "amount >= 0 AND amount <= 500"
        elif amount_option == "2":
            # Filter for 500 to 2500
            filter_condition = "amount > 500 AND amount <= 2500"
        elif amount_option == "3":
            # Filter for 2500 and above
            filter_condition = "amount > 2500"
        else:
            print("Invalid input.")
            return
    else:
        print("Invalid input.")
        return
    # Writing a single line of sql code which takes the filter condition and returns data accordingly.
    select_expenses_sql = (
        f"SELECT * FROM expenses WHERE {filter_condition} ORDER BY date;"
    )
    expenses = conn.execute(select_expenses_sql).fetchall()

    if not expenses:
        print("No expenses recorded based on the selected filter.")
    else:
        print("Filtered Expenses:")
        for expense in expenses:
            print(
                f"ID: {expense[0]}, Date: {expense[1]}, Description: {expense[2]}, Amount: Rs: {expense[3]}"
            )


# defined this funtion to check is database is empty or not
def is_empty():
    if conn.execute(select_expenses_sql).fetchall() == []:
        return True
    else:
        return False


def main_menu():
    # conn=db_init()
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expenses")
        print("4. Delete Expense")
        print("5. Update Expense Description")
        print("6. Export Expense")
        print("7. Data Filter")
        print("8. Quit")

        choice = input("Enter your choice (1-8): ")

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
            print_csv()
        elif choice == "7":
            data_filter()
        elif choice == "8":
            is_empty()
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main_menu()


conn.close()