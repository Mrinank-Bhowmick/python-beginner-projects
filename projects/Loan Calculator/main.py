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
    principal = float(input("Enter the loan amount: $"))
    annual_interest_rate = float(input("Enter the annual interest rate (as a percentage): "))
    months = int(input("Enter the loan term (in months): "))
    
    # Calculate monthly payment
    monthly_payment = calculate_loan_payment(principal, annual_interest_rate, months)
    
    # Display the result
    print(f"Your monthly payment will be: ${monthly_payment:.2f}")

if __name__ == "__main__":
    main()
