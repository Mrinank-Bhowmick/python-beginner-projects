def calculate_loan_payment(principal, annual_interest_rate, months):
    # Convert annual interest rate to monthly rate
    monthly_interest_rate = annual_interest_rate / 12 / 100

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


def main():
    print("Welcome to the Loan Calculator!")

    # Get user input
    principal = floatValidation("Enter the loan amount: $")
    annual_interest_rate = floatValidation(
        "Enter the annual interest rate (as a percentage): "
    )
    months = intValidtaion("Enter the loan term (in months): ")

    # Calculate monthly payment
    monthly_payment = calculate_loan_payment(principal, annual_interest_rate, months)

    # Display the result
    print(f"Your monthly payment will be: ${monthly_payment:.2f}")


def floatValidation(question):
    while True:
        try:
            value = float(input(question))
            return value
        except ValueError:
            print("Input should be a valid number")
            continue


def intValidtaion(question):
    while True:
        try:
            value = int(input(question))
            return value
        except ValueError:
            print("Input should be a valid number")


if __name__ == "__main__":
    main()
