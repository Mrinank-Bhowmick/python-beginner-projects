# Define a list of valid PINs and corresponding account balances
pins = [1234, 5678, 9012]
balances = [1000, 5000, 2000]

# Define functions for validating PIN, checking balance, withdrawing money, depositing money, and displaying menu
def validate_pin(pin):
    if pin in pins:
        return True
    else:
        return False

def check_balance(pin):
    index = pins.index(pin)
    balance = balances[index]
    print("Your balance is:", balance)

def withdraw(pin, amount):
    index = pins.index(pin)
    balance = balances[index]
    if amount > balance:
        print("Insufficient funds")
    else:
        balance -= amount
        balances[index] = balance
        print("Withdrawal successful. Your new balance is:", balance)

def deposit(pin, amount):
    index = pins.index(pin)
    balance = balances[index]
    balance += amount
    balances[index] = balance
    print("Deposit successful. Your new balance is:", balance)

def display_menu():
    print("Welcome to the ATM")
    print("1. Check balance")
    print("2. Withdraw")
    print("3. Deposit")
    print("4. Exit")

# Define a while loop to keep the program running until the user chooses to exit
while True:
    # Get user input and call appropriate functions
    pin = int(input("Enter your PIN: "))
    if validate_pin(pin):
        display_menu()
        choice = int(input("Enter your choice: "))
        if choice == 1:
            check_balance(pin)
        elif choice == 2:
            amount = int(input("Enter amount to withdraw: "))
            withdraw(pin, amount)
        elif choice == 3:
            amount = int(input("Enter amount to deposit: "))
            deposit(pin, amount)
        elif choice == 4:
            print("Thank you for using the ATM")
            break
        else:
            print("Invalid choice")
    else:
        print("Invalid PIN")