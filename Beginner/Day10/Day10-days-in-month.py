# Days in Month
# create a function to check if a year is a leap year
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


# create a function that returns the days in mouth
def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2:
        if is_leap(year):
            return month_days[month-1] + 1
    """
    The above codes can be written as:
    if is_leap(year) and month == 2:
        return month_days[month-1] + 1
    *** Remember to use "and" instead of nested if ***
    """
    return month_days[month-1]


# Gather inputs
input_year = int(input("Enter a year: "))
input_month = int(input("Enter a month: "))
days = days_in_month(year=input_year, month=input_month)
print(f"There are {days} days in {input_year}.{input_month}")




