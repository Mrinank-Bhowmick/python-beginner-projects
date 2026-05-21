# === Python Banking System · annotated for the pyBegin playground ===

import random


# Manage all accounts and their transaction histories
class Bank:
    def __init__(self):
        # Store accounts and transaction logs in dicts
        self.accounts = {}
        self.transactions = {}

    # Create a new account and return it
    def create_account(self, account_holder, initial_balance):
        account_number = self.generate_account_number()
        account = BankAccount(account_number, account_holder, initial_balance)
        self.accounts[account_number] = account
        self.transactions[account_number] = []
        return account

    # Build a random 8-digit account number string
    def generate_account_number(self):
        return "".join(random.choice("0123456789") for _ in range(8))

    # Look up and return an account by number
    def get_account(self, account_number):
        return self.accounts.get(account_number)

    # Deposit or withdraw and record the transaction
    def perform_transaction(self, account_number, transaction_type, amount):
        account = self.get_account(account_number)
        if not account:
            return "Account not found."

        if transaction_type == "deposit":
            account.deposit(amount)
        elif transaction_type == "withdraw":
            account.withdraw(amount)
        else:
            return "Invalid transaction type."

        self.transactions[account_number].append((transaction_type, amount))
        return "Transaction completed."

    # Return the full transaction history list
    def get_transaction_history(self, account_number):
        return self.transactions.get(account_number, [])


# Represent a single bank account with balance
class BankAccount:
    def __init__(self, account_number, account_holder, initial_balance):
        # Save account details as attributes
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = initial_balance

    # Add amount to balance if positive
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    # Subtract amount if valid and sufficient funds
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount

    # Return the current balance
    def get_balance(self):
        return self.balance


def main():
    # Create a new bank instance
    bank = Bank()

    # Show menu and handle choices in a loop
    while True:
        print("\nPython Banking System")
        print("1. Create Account")
        print("2. Perform Transaction")
        print("3. Check Balance")
        print("4. Transaction History")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            account_holder = input("Enter your name: ")
            initial_balance = float(input("Enter initial balance: "))
            account = bank.create_account(account_holder, initial_balance)
            print(
                f"Account created successfully. Account Number: {account.account_number}"
            )

        elif choice == "2":
            account_number = input("Enter account number: ")
            transaction_type = input(
                "Enter transaction type (deposit/withdraw): "
            ).lower()
            amount = float(input("Enter transaction amount: "))
            result = bank.perform_transaction(account_number, transaction_type, amount)
            print(result)

        elif choice == "3":
            account_number = input("Enter account number: ")
            account = bank.get_account(account_number)
            if account:
                print(f"Account Balance: ${account.get_balance()}")
            else:
                print("Account not found.")

        elif choice == "4":
            account_number = input("Enter account number: ")
            transactions = bank.get_transaction_history(account_number)
            if transactions:
                print("Transaction History:")
                for trans_type, amount in transactions:
                    print(f"{trans_type.capitalize()}: ${amount}")
            else:
                print("Account not found or no transaction history.")

        elif choice == "5":
            print("Exiting the Python Banking System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
