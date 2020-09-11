"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to
print out a calendar for April in 2015, but if you omit either the year or both values,
it should use today’s date to get the month and year.
"""

import sys
import calendar
from datetime import datetime

# a_string = input("Enter two integers, one for month and a second for year, separated by a space:")

# numbers = []
# for word in a_string.split():
#    if word.isdigit():
#       numbers.append(int(word))

# if len(a_string) == 0:
#     print(calendar.prmonth(datetime.now().year, datetime.now().month))
# elif len(numbers) == 1:
#     pass
#     # print(calendar.prmonth(datetime.now().year, numbers[0]))
# elif len(numbers) == 2:
#     print(calendar.prmonth(numbers[1], numbers[0]))
# else:
#     print("ERROR: The expected input format is two integers, one for month and a second for year, separated by a space")

args = sys.argv
now = datetime.now()
month = now.month
year = now.year

if(len(args) == 1):
     pass
# user inputs one argument
elif(len(args) == 2):
     month = int(args[1])
elif(len(args) == 3):
    month = int(args[1])
    year = int(args[2])
else:
     print("wrong format")
if month < 1 or month > 12:
     print("error: Invalid month")

tc = calendar.TextCalendar()
tc.prmonth(year, month)
