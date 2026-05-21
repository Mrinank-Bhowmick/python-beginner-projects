# === Personal Finance Tracker · annotated for the pyBegin playground ===
# A beginner-friendly walkthrough — original project by @Manishak798.

# Represent a single expense with name, amount, category
class Expense:
    def __init__(self, name, amount, category):
        self.name = name
        self.amount = amount
        self.category = category


# Manage a list of expenses and calculations
class FinanceManager:
    # Start with an empty expense list
    def __init__(self):
        self.expenses = []

    # Create and store a new Expense object
    def add_expense(self, name, amount, category):
        expense = Expense(name, amount, category)
        self.expenses.append(expense)

    # Sum all stored expense amounts
    def calculate_total_expenses(self):
        total_expenses = sum(expense.amount for expense in self.expenses)
        return total_expenses

    # Print every expense's details
    def list_expenses(self):
        for expense in self.expenses:
            print(
                f"Name: {expense.name}, Amount: {expense.amount}, Category: {expense.category}"
            )


if __name__ == "__main__":
    # Create the finance manager instance
    finance_manager = FinanceManager()

    # Show menu and handle user choices in a loop
    while True:
        print("Personal Finance Manager")
        print("1. Add Expense")
        print("2. List Expenses")
        print("3. Calculate Total Expenses")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Expense Name: ")
            amount = float(input("Expense Amount: "))
            category = input("Expense Category: ")
            finance_manager.add_expense(name, amount, category)

        elif choice == "2":
            finance_manager.list_expenses()

        elif choice == "3":
            total_expenses = finance_manager.calculate_total_expenses()
            print(f"Total Expenses: {total_expenses}")

        elif choice == "4":
            break
