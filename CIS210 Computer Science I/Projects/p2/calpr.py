"""
Week 2, Project 2, Part 2. 2014/10/8
Print the calendar for a month.
Authors: Haomin He
Credits: Prof. Michal Young and Rickie

This program will take two integers, a month number (1-12)
and a year number (1-2100) from the command line. It will
then print a calendar in the format.

Limitations: Treats February as always having 28 days.
"""

import argparse
import datetime # To determine what day of week a month
				# begins on.  
# Note: For this project, module calendar
# is not permitted.  It basically has a function
# to do the whole assignment in one line. 

MONTHLEN = [ 0, # No month zero
	31, # 1. January
	28, # 2. February (ignoring leap years)
	31, # 3. March
	30, # 4. April
	31, # 5. May
	30, # 6. June
	31, # 7. July
	31, # 8. August
	30, # 9. September
	31, #10. October
	30, #11. November
	31, #12. December
	]

parser = argparse.ArgumentParser(description="Print calendar")
parser.add_argument("month", type=int, 
                        help="Month number (1-12)")
parser.add_argument("year", type=int, 
                        help="Year (1800-2525)")
args = parser.parse_args()  # gets arguments from command line
month = args.month
year = args.year


# What day of the week does year,month begin on? 
a_date = datetime.date(year, month, 1)
starts_weekday = a_date.weekday()
## a_date.weekday() gives 0=Monday, 1=Tuesday, etc.
## Roll to start week on Sunday
starts_weekday = (1 + starts_weekday) % 7  


month_day = 1   			## Next day to print
days_left = MONTHLEN[month]  ## Left days to print

print(" Su Mo Tu We Th Fr Sa")

for i in range(7): # First partial week.
	if i < starts_weekday :
		print("   ", end="")
	else:
		# Logic for printing one day, moving to next
		print(format(month_day, "3d"), end="")
		month_day += 1
		days_left -= 1
print() # Newline


while days_left >= 7: # There is at least a full week left to print.
        for i in range(7):
                print(format(month_day, "3d"), end="")
                month_day += 1
                days_left -= 1
        print() # Newline


while days_left > 0: # There are more days to print. 
        print(format(month_day, "3d"), end="")
        month_day += 1
        days_left -= 1
print() # Newline
	
