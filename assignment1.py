#!/usr/bin/env python3

'''
OPS435 Assignment 1 - Fall 2024
Program: assignment1.py 
Author: Nelson Yeh
The python code in this file (a1_nyeh2.py) is original work written by
Nelson Yeh. No code in this file is copied from any other source
except those provided by the course instructor, including any person,
textbook, or on-line resource. I have not shared this python script
with anyone or anything except for submission for grading. I understand
that the Academic Honesty Policy will be enforced and
violators will be reported and appropriate action will be taken.
'''

import sys

def day_of_week(year: int, month: int, date: int) -> str:
    "Based on the algorithm by Tomohiko Sakamoto"
    days = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat'] 
    offset = {1:0, 2:3, 3:2, 4:5, 5:0, 6:3, 7:5, 8:1, 9:4, 10:6, 11:2, 12:4}
    if month < 3:
        year -= 1
    num = (year + year//4 - year//100 + year//400 + offset[month] + date) % 7
    return days[num]


def mon_max(month:int, year:int) -> int:
    "returns the maximum day for a given month. Includes leap year check"
    # Check if the month is Feb
    if month == 2:
        # Check if it is a leap year, return 29 if it is and 28 if its not
        if leap_year(year):
            return 29
        else:
            return 28
        # Check if the month is April, June, September or November and return 30
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        # Return 31 as we checked all other months that dont have 31 days
        return 31

def after(date: str) -> str:
    '''
    after() -> date for next day in YYYY-MM-DD string format

    Return the date for the next day of the given date in YYYY-MM-DD format.
    This function takes care of the number of days in February for leap year.
    This fucntion has been tested to work for year after 1582
    '''
    str_year, str_month, str_day = date.split('-')
    year = int(str_year)
    month = int(str_month)
    day = int(str_day)
    tmp_day = day + 1  # next day

    if tmp_day > mon_max(month, year):
        to_day = tmp_day % mon_max(month, year)  # if tmp_day > this month's max, reset to 1 
        tmp_month = month + 1
    else:
        to_day = tmp_day
        tmp_month = month + 0

    if tmp_month > 12:
        to_month = 1
        year = year + 1
    else:
        to_month = tmp_month + 0

    next_date = f"{year}-{to_month:02}-{to_day:02}"

    return next_date


def usage():
    "Print a usage message to the user"
    print("Usage: assignment1.py YYYY-MM-DD YYYY-MM-DD")


def leap_year(year: int) -> bool:
    "return True if the year is a leap year"
    # Checks the definition of a leap year for the Gregorian calendar
    if year % 4 == 0 and (year % 100 != 0 or year % 400 ==0):
        return True
    else:
        return False

def valid_date(date: str) -> bool:
    "check validity of date and return True if valid"
    try:
        # Splits each value using "-" as the seperator into year, month and day
        str_year, str_month, str_day = date.split('-')
        # Converts str values into int values
        year = int(str_year)
        month = int(str_month)
        day = int(str_day)
        # Checks for invalid months. Makes sure that month is not less than 1 or greater than 12 
        if month < 1 or month > 12:
            return False
        # Checks for invalid days. Makes sure that day is not less than 1 or greater than number of days in selected month
        if day < 1 or day > mon_max(month, year):
            return False
        # Checks for invalid years. Makes sure that year is not less than 1
        if year < 1 or len(str_year) != 4:
            return False
        return True
    except ValueError:
        return False


def day_count(start_date: str, stop_date: str) -> int:
    "Loops through range of dates, and returns number of weekend days"
    # Create a tracker for counting the number of weekend days
    num_weekend_days = 0
    # Set alias for start date to alter
    tracker_date = start_date

    # Checks to make sure that first date doesnt exceed stop date
    while tracker_date <= stop_date:
        # Splits each value using "-" as the seperator into year, month and day
        str_year, str_month, str_day = tracker_date.split('-')
        # Converts str values into int values
        year = int(str_year)
        month = int(str_month)
        day = int(str_day)
        # Use day_of_week function to assign name of day
        name_of_day = day_of_week(year, month, day)
        # Checks to see if the name_of_day is sat or sun add one to the counter
        if name_of_day in ['sat','sun']:
            num_weekend_days = num_weekend_days + 1
        # Use the after function to cycle to the next date
        tracker_date = after(tracker_date)

    return num_weekend_days

if __name__ == "__main__":
    # Make sure there are 3 arguments to use the script
    if len(sys.argv) != 3:
        # Display Usage message if used incorrectly
        usage()
        # Close the program if used incorrectly
        sys.exit()
    # Assign the sys.argvs to variables
    start_date = sys.argv[1]
    end_date = sys.argv[2]
    # Make sure the dates are valid via valid date function
    if not valid_date(start_date) or not valid_date(end_date):
        usage()
        sys.exit()
    # Check to see if the start date is after the end date
    if start_date > end_date:
        # If start date is after end date flip the dates
        weekend_days = day_count(end_date, start_date)
        print("The period between " + str(end_date) + ' and ' + str(start_date) + ' includes ' + str(weekend_days) + ' weekend days.')
    else:
        # If start date is before end date run the regular program
        weekend_days = day_count(start_date, end_date)
        print("The period between " + str(start_date) + ' and ' + str(end_date) + ' includes ' + str(weekend_days) + ' weekend days.')