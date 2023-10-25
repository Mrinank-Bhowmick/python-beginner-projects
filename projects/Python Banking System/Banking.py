import random


class Bank:
    def __init__(self):
        """
        Initializes a Bank object with dictionaries to store user accounts and transaction history.
        """
        self.accounts = {}  # Dictionary to store user accounts
        self.transactions = {}  # Dictionary to store transaction history

    def create_account(self, account_holder, initial_balance):
        """
        Creates a new bank account for a user.

        Args:
            account_holder (str): The name of the account holder.
            initial_balance (float): The initial balance for the account.

        Returns:
            BankAccount: The created BankAccount object.
        """
        account_number = self.generate_account_number()
        account = BankAccount(account_number, account_holder, initial_balance)
        self.accounts[account_number] = account
        self.transactions[account_number] = []
        return account

    def generate_account_number(self):
        """
        Generates a random 8-digit account number.

        Returns:
            str: The generated account number.
        """
        return "".join(random.choice("0123456789") for _ in range(8))

    def get_account(self, account_number):
        """
        Retrieves a BankAccount object based on the account number.

        Args:
            account_number (str): The account number to look up.

        Returns:
            BankAccount: The BankAccount object if found, else None.
        """
        return self.accounts.get(account_number)

    def perform_transaction(self, account_number, transaction_type, amount):
        """
        Performs a transaction (deposit or withdrawal) on a user's account.

        Args:
            account_number (str): The account number for the transaction.
            transaction_type (str): The type of transaction (deposit or withdraw).
            amount (float): The transaction amount.

        Returns:
            str: A message indicating the result of the transaction.
        """
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

    def get_transaction_history(self, account_number):
        """
        Retrieves the transaction history for a user's account.

        Args:
            account_number (str): The account number to look up.

        Returns:
            list: A list of tuples representing transaction history (type, amount).
        """
        return self.transactions.get(account_number, [])


class BankAccount:
    def __init__(self, account_number, account_holder, initial_balance):
        """
        Initializes a BankAccount object.

        Args:
            account_number (str): The account number.
            account_holder (str): The name of the account holder.
            initial_balance (float): The initial balance for the account.
        """
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        """
        Deposits funds into the account.

        Args:
            amount (float): The amount to be deposited.
        """
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        """
        Withdraws funds from the account.

        Args:
            amount (float): The amount to be withdrawn.
        """
        if 0 < amount <= self.balance:
            self.balance -= amount

    def get_balance(self):
        """
        Retrieves the current balance of the account.

        Returns:
            float: The account balance.
        """
        return self.balance


def main():
    """
    Main function to run the Python Banking System.
    """
    bank = Bank()

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
