import pytest
from calculate import judge_leap_year, month_days


def test_judge_leap_year():
    assert judge_leap_year(2000) == True
    assert judge_leap_year(2008) == True
    assert judge_leap_year(2023) == False
    assert judge_leap_year(1900) == False
    assert judge_leap_year(2400) == True
    assert judge_leap_year(2100) == False


def test_month_days():
    assert month_days(7, False) == 31
    assert month_days(4, True) == 30
    assert month_days(2, True) == 29
    assert month_days(2, False) == 28
    assert month_days(1, False) == 31
    assert month_days(11, True) == 30


# "pytest -s test_calculate.py" to test this file
