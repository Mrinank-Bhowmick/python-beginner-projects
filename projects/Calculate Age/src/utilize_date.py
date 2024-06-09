from calendar import isleap


def judge_leap_year(year):
    """
        judge the leap year.

    Args:
        year (int): To check the year.
    return:
         bool: Ture if the year is a leap year, False otherwise.
    """
    if isleap(year):
        return True
    else:
        return False


def month_days(month, leap_year):
    """
    Returns the number of days in each month

    Args:
         month (int): The month 1-12.

    Returns:
        int: The number of days in the month.
    """
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2 and leap_year:
        return 29
    elif month == 2 and (not leap_year):
        return 28
