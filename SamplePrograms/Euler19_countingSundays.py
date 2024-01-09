""" 
Checks if the year is leap year

>>> is_leap_year(1996)
True

>>> is_leap_year(1990)
False

>>> is_leap_year(2000)
True

>>> is_leap_year(1900)
False

"""

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 != 0 or year % 400 == 0:
            return True
    return False


def count_sundays_on_first():
    # Starting date: January 1, 1901 (Tuesday)
    day_of_week = 2  # 0 = Sunday, 1 = Monday, ..., 6 = Saturday
    count = 0

    for year in range(1901, 2001):
        for month in range(1, 13):
            # Check if it's a Sunday (day_of_week = 0) and the first day of the month (day == 1)
            if day_of_week == 0:
                count += 1

            # Calculate the number of days in the current month
            if month in {4, 6, 9, 11}:
                days_in_month = 30
            elif month == 2:
                days_in_month = 29 if is_leap_year(year) else 28
            else:
                days_in_month = 31

            # Move to the next month
            day_of_week = (day_of_week + days_in_month) % 7

    return count

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    result = count_sundays_on_first()
    print("The number of Sundays that fell on the first of the month during the twentieth century is:", result)