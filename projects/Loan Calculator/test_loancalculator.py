import unittest
from main import calculate_loan_payment, get_months


def test_calculate_loan_payment():
    # Define the expected monthly payment
    expected_payment = 167.75198511394362

    # Define the input parameters for the function
    principal = 2000
    annual_interest_rate = 1.2
    months = 12

    # Calculate the monthly payment using the function you want to test
    monthly_payment = calculate_loan_payment(principal, annual_interest_rate, months)

    # Use the assert statement to check if the calculated payment matches the expected payment
    assert monthly_payment == expected_payment


if __name__ == '__main__':
    test_calculate_loan_payment()
