# Program to display calendar


def display_calendar(y, m):
    import calendar

    print(calendar.month(y, m))


y = int(input("Enter year: "))
m = int(input("Enter month: "))

display_calendar(y, m)
