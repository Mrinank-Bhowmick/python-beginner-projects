# === Calculate Your Age! · annotated for the pyBegin playground ===
# A beginner-friendly walkthrough — original project by @xlo-u.

# Import time utilities
import time
from calendar import isleap


# Return True if the given year is a leap year
def judge_leap_year(year):
    if isleap(year):
        return True
    else:
        return False


# Return the number of days in a given month
def month_days(month, leap_year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2 and leap_year:
        return 29
    elif month == 2 and (not leap_year):
        return 28


# Get the user's name and age, then get today's date
name = input("input your name: ")
age = input("input your age: ")
localtime = time.localtime(time.time())

# Calculate total months lived
year = int(age)
month = year * 12 + localtime.tm_mon
day = 0

# Find the birth year and the current year
begin_year = int(localtime.tm_year) - year
end_year = begin_year + year

# Count total days across each full year lived
for y in range(begin_year, end_year):
    if judge_leap_year(y):
        day = day + 366
    else:
        day = day + 365

# Add days for each completed month this year
leap_year = judge_leap_year(localtime.tm_year)
for m in range(1, localtime.tm_mon):
    day = day + month_days(m, leap_year)

# Add the remaining days of the current month
day = day + localtime.tm_mday
print("%s's age is %d years or " % (name, year), end="")
print("%d months or %d days" % (month, day))
