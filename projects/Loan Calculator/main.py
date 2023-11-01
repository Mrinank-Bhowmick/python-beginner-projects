TOTAL_PERCENT = 100
MONTH = 12


def calculate_loan_payment(principal, annual_interest_rate, months):
    """
    Convert annual interest rate to monthly rate
    Args:
        principal(float): The principal amount for the loan
        annual_interest_rate(float): The interest rate for the amount annually.
        months(int): The timeframe for the loan repayment in months.

    Returns:
    monthly_payment(float): The amount of money that needs to be paid monthly.
    """

    monthly_interest_rate = annual_interest_rate / MONTH / 100

    # Calculate monthly payment
    if monthly_interest_rate == 0:
        monthly_payment = principal / months
    else:
        monthly_payment = (
                principal
                * (monthly_interest_rate * (1 + monthly_interest_rate) ** months)
                / ((1 + monthly_interest_rate) ** months - 1)
        )

    return monthly_payment


def get_months():
    """
    This function gets the loan repayment in months.
    Returns:
    months(int): The timeframe for the loan repayment in months.
    Error Message: Displays an error message if the user inputs are invalid.
    """
    while True:
        try:
            months = int(input("Enter the loan term (in months): "))
            if months < 0:
                print("Enter a valid interest rate in percentage")
            else:
                return months
        except ValueError:
            print("Enter a valid numeric value for loan term in months")


def get_interest_rate():
    """
    This function gets the interest rate for a year.
    Returns:
    annual_interest_rate(float): The interest rate for the amount annually.
    Error Message: Displays an error message if the user inputs are invalid.
    """
    while True:
        try:
            annual_interest_rate = float(input("Enter the annual interest rate (as a percentage): "))
            if annual_interest_rate < 0 or annual_interest_rate > TOTAL_PERCENT:
                print("Enter a valid interest rate in percentage")
            else:
                return annual_interest_rate
        except ValueError:
            print("Enter a valid numeric percentage for interest rate")


def get_principal():
    """
    This function fetches the principal amount for the loan
    Returns:
    principal(float): The principal amount for the loan.
    Error Message: Displays an error message if the user inputs are invalid.
    """
    while True:
        try:
            principal = float(input("Enter the loan amount: $"))
            if principal <= 0:
                print("Enter a valid amount for the principal")
            else:
                return principal
        except ValueError:
            print("Invalid Input. Please enter a numeric value for the principal.")


def main():
    print("Welcome to the Loan Calculator!")

    # Get user input
    principal = get_principal()
    annual_interest_rate = get_interest_rate()
    months = get_months()

    # Calculate monthly payment
    monthly_payment = calculate_loan_payment(principal, annual_interest_rate, months)

    # Display the result
    print(f"Your monthly payment will be: ${monthly_payment:.2f}")


if __name__ == "__main__":
    main()
