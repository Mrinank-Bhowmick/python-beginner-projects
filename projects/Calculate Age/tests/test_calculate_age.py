import time
from unittest.mock import patch
from calculate_age import age_calculator

@patch('time.time', return_value=1621848668.0)
def test_age_calculator(mock_time):
    name = "Chloe"
    age = 30
    expect_output = "Chloe's age is 30 years or 365 months or 11102 days"
    assert age_calculator(name, age) == expect_output

def test_age_calculator_negative_age():
    name = "Emma"
    age = -5
    try:
        age_calculator(name, age)
    except ValueError as e:
        assert str(e) == "Please input a positive number."


def test_age_calculator_leap_year():
    name = "David"
    age = 30
    expect_output_leap_year = "David's age is 30 years or 366 months or 11115 days"
    assert age_calculator(name, age) == expect_output_leap_year
