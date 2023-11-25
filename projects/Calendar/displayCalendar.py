# Display Calendar

import calendar


def user_validation(year, month):
    """
    To check user input validation in type and range of input.
    """
    try:
        year = int(year)
        month = int(month)
        if year < 0 or month < 1 or month > 12:
            print("Invalid input. Please enter a valid year and month.")
            return None
        else:
            return year, month
    except ValueError:
        print("Invalid input. Please enter numerical values for year and month.")
        return None


def display_calendar(year, month):
    """
    To display calendar
    """
    print(calendar.month(year, month))


# Main Play
if __name__ == "__main__":
    print("This is Calendar Display, Please enter numerical values for year and month.")
    print("Year value must be more than 0.")
    print("Month value must be in the range of 1 to 12.")

    while True:
        input_year = input("Enter year: ")
        input_month = input("Enter month: ")
        result = user_validation(input_year, input_month)

        if result:
            year, month = result
            break

    display_calendar(year, month)