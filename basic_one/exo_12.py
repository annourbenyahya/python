#Python program that prints the calendar for a given month and year.

import calendar

year = int(input("Enter year: "))
month = int(input("Enter month: "))

print(calendar.month(year, month))
