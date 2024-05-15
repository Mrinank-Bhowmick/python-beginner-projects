def display_cal(year_input, month_input):
    """
    Display a calendar for the desired year and month.

    Parameters:
    year_input (int): The year for which the calendar is to be displayed.
    month_input (int): The month for which the calendar is to be displayed.

    """
    import calendar

    print(calendar.month(year_input, month_input))


def fetch_year():
    """
    Prompts the user for a valid year and returns the year as an integer.
    """
    while True:
        try:
            year_input = int(input("Enter year: "))
            if year_input < 0:
                raise ValueError("Year must be a positive integer")
            return year_input
        except ValueError:
            print("Invalid input. Please enter a valid year.")


def fetch_month():
    """
    Function that asks the user to enter a month, validates the input, and returns the valid month.
    """
    while True:
        try:
            month_input = int(input("Enter month: "))
            if month_input < 1 or month_input > 12:
                raise ValueError("Month must be between 1 and 12")
            return month_input
        except ValueError:
            print("Invalid input. Please enter a valid month.")


year_input = fetch_year()
month_input = fetch_month()

display_cal(year_input, month_input)