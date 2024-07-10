import pytest
from utilize_date import judge_leap_year, month_days


def test_judge_leap_year():
    """
    judge_leap_year function tests whether a given year is a leap year.

    A leap year is divisible by 4 and, if divisible by 100, must also be divisible by 400.
    """
    assert judge_leap_year(2000) == True
    assert judge_leap_year(2008) == True
    assert judge_leap_year(2023) == False
    assert judge_leap_year(1900) == False
    assert judge_leap_year(2400) == True
    assert judge_leap_year(2100) == False


def test_month_days():
    """
    The month_days function tests whether if returns the correct number of days for a given month

    For Feb, both leap years and common years are considered.
    """
    assert month_days(7, False) == 31
    assert month_days(4, True) == 30
    assert month_days(2, True) == 29
    assert month_days(2, False) == 28
    assert month_days(1, False) == 31
    assert month_days(11, True) == 30


# "pytest -s test_utilize_date.py" to test this file
