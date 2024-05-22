import time
from utilize_date import judge_leap_year, month_days


def age_calculator(name, age):
    localtime = time.localtime(time.time())

    year = int(age)
    month = year * 12 + localtime.tm_mon
    day = 0

    begin_year = int(localtime.tm_year) - year
    end_year = begin_year + year

    for y in range(begin_year, end_year):
        if judge_leap_year(y):
            day += 366
        else:
            day += 365

    leap_year = judge_leap_year(localtime.tm_year)
    for m in range(1, localtime.tm_mon):
        day += month_days(m, leap_year)

    day += localtime.tm_mday

    return f"{name}'s age is {year} years or {month} months or {day} days"




