# Program to display calendar


def display_calendar(year, month):
    import calendar

    print(calendar.month(year, month))


year = int(input("Enter year: "))
month = int(input("Enter month: "))

display_calendar(year, month)
