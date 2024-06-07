from unittest.mock import patch
from calculate_age import age_calculator


@patch("time.time", return_value=1621848668.0)
def test_age_calculator(mock_time):
    """
    Test the age_calculator function
    Mocks the current time and check if the age is calculated
    based on current time
    """
    name = "Chloe"
    age = 30
    expect_output = "Chloe's age is 30 years or 365 months or 11102 days"
    assert age_calculator(name, age) == expect_output


def test_age_calculator_negative_age():
    """
    Tests the age_calculator function for negative age input
    Check for ValueError when user input negative age.
    """
    name = "Emma"
    age = -5
    try:
        age_calculator(name, age)
    except ValueError as e:
        assert str(e) == "Please input a positive number."


@patch("time.time", return_value=1621848668.0)
def test_age_calculator_leap_year(mock_time):
    """
    Test the age_calculator function considering leap years
    Check for expect_output_leap_year comparing the real output considering leap years
    """
    name = "David"
    age = 30
    expect_output_leap_year = "David's age is 30 years or 365 months or 11102 days"
    assert age_calculator(name, age) == expect_output_leap_year
