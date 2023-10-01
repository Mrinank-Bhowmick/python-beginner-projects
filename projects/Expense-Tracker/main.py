import sqlite3
import csv 

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
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




def convert_to_excel():
    # Convert expense data from database to excel
    
    # Define SQL query to select all data from 'expenses' table
    query = "Select * from expenses"
    
    # Execute the query and fetch data
    cursor.execute(query)
    data = cursor.fetchall()
    
    # Add column headers to the data
    data = [('Id', 'Date', 'Description', 'Amount')] + data
        
    # Write data to a CSV file named 'expenses.csv'
    with open('expenses.csv', 'w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(data)
        
def convert_to_pdf():
    # Convert expense data from database to PDF
    
    # Define SQL query to select all data from 'expenses' table
    query = "SELECT * FROM expenses"
    
    # Execute the query and fetch data
    cursor.execute(query)
    data = cursor.fetchall()
    
    # Add column headers to the data
    data = [('Id', 'Date', 'Description', 'Amount')] + data

    # Define PDF filename as 'expenses.pdf' and set page size to letter
    pdf_filename = 'expenses.pdf'
    pdf = SimpleDocTemplate(pdf_filename, pagesize=letter)
    
    # Create a table from the data
    table = Table(data)
    
    # Define style for the table
    style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                        ('GRID', (0, 0), (-1, -1), 1, colors.black)])
    table.setStyle(style)
    
    # Define a title for the PDF
    styles = getSampleStyleSheet()
    title = Paragraph("<b>Expenses</b>", styles['Title'])

    # Build the PDF with title and table
    pdf.build([title, table])



def main_menu():
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expenses")
        print("4. Delete Expense")
        print("5. Update Expense Description")
        print("6. Data Export to Excel")
        print("7. Data Export to PDF")
        print("8. Data Filter")
        print("9. Quit")

        choice = input("Enter your choice (1-9): ")

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
            convert_to_excel()
        elif choice == "7":
            convert_to_pdf()
        elif choice == "8":
            data_filter()
        elif choice == "9":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main_menu()

conn.close()
