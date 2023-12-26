class Expense:
    def __init__(self, name, amount, category):
        self.name = name
        self.amount = amount
        self.category = category


class FinanceManager:
    def __init__(self):
        self.expenses = []

    def add_expense(self, name, amount, category):
        expense = Expense(name, amount, category)
        self.expenses.append(expense)

    def calculate_total_expenses(self):
        total_expenses = sum(expense.amount for expense in self.expenses)
        return total_expenses

    def list_expenses(self):
        for expense in self.expenses:
            print(
                f"Name: {expense.name}, Amount: {expense.amount}, Category: {expense.category}"
            )


# Sample usage
if __name__ == "__main__":
    finance_manager = FinanceManager()

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
