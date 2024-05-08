# Program to display calendar


def display_calendar(year, month):
    """
    Display a calendar for the given year and month.

    Parameters:
    year (int): The year for which the calendar is to be displayed.
    month (int): The month for which the calendar is to be displayed.

    """
    import calendar

    print(calendar.month(year, month))


def get_valid_year():
    """
    Function to prompt the user for a valid year input and return the valid year as an integer.
    """
    while True:
        try:
            year = int(input("Enter year: "))
            if year < 0:
                raise ValueError("Year must be a positive integer")
            return year
        except ValueError:
            print("Invalid input. Please enter a valid year.")


def get_valid_month():
    """
    A function that prompts the user to enter a month, validates the input, and returns the valid month.
    """
    while True:
        try:
            month = int(input("Enter month: "))
            if month < 1 or month > 12:
                raise ValueError("Month must be between 1 and 12")
            return month
        except ValueError:
            print("Invalid input. Please enter a valid month.")


year = get_valid_year()
month = get_valid_month()

display_calendar(year, month)

