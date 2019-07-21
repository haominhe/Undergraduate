"""
How many days from yyyy mm dd until the next mm dd
Authors: Haomin He
Credits: 

CIS 210 assignment 3, Fall 2014, 2014/10/14
Usage example: python days_till.py  2012 09 24 06 14
    (first day of fall classes until end of spring finals)
"""

import sys  # For exit with a message
import argparse # Fancier command line parsing

def is_leap(year):
    '''Determines whether given year is a leap year.
    args:
       year: an integer between 1800 and 2500.
    returns:
       True if and only if year is a leap year.
    '''
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False

def days_in_month(start_month, year):
    '''Calculate days in month of year. If the year is a leap year, Feburary should be 29 days.
       Otherwise, there are 28 days in Febuary.
    args:
       start_month: integer 1..12 indicating month, January..December.
       year: an integer between 1800 and 2500.
    returns:
       integer days in month of year. 
    '''
    if is_leap(year):
        DaysInMonthLeap = [0,31,29,31,30,
                           31,30,31,31,
                           30,31,30,31]
        return DaysInMonthLeap[start_month]
    elif is_leap(year) == False:
        DaysInMonth = [0,31,28,31,30,   # because index starts at 0,
                       31,30,31,31,     # but month is from 1 to 12
                       30,31,30,31]     # so put 0 into the list.
        return DaysInMonth[start_month]
   
def days_between(year, start_month, start_day, end_month, end_day):
    '''Determine how many days from begin date to next occurrence of end date.
    args:
       year: an integer between 1800 and 2500.
       start_month, end_month: integer 1..12 indicating month, January..December.
       start_day, end_day: integer 1..31 for day of month.  
    returns:
       days between two dates. 
    '''
    if start_month < end_month:
        totaldays = days_in_month(start_month,year) - start_day  # remainder of start month
        curmon = start_month + 1
        while curmon != end_month:
            totaldays += days_in_month(curmon,year)
            curmon = curmon + 1
        totaldays += end_day    # beginning of end month
        return totaldays
        
    elif start_month == end_month:
        if start_day <= end_day:
            totaldays = end_day - start_day
            return totaldays
        elif start_day > end_day:
            daysbtn = start_day - end_day
            if is_leap(year + 1):
                totaldays = 366 - daysbtn
            else:
                totaldays = 365 - daysbtn
            return totaldays
        
    elif start_month > end_month:
        start_month, end_month = end_month, start_month
        start_day, end_day = end_day, start_day
        totaldays = days_in_month(start_month,year) - start_day  # remainder of start month
        curmon = start_month + 1
        while curmon != end_month:
            totaldays += days_in_month(curmon,year)
            curmon = curmon + 1
        totaldays += end_day    # beginning of end month
        if is_leap(year + 1):
            finaldays = 366 - totaldays
        else:
            finaldays = 365 - totaldays
        return finaldays
    
def is_valid(valyear, valmonth, valday):
    '''Test if the number of year, month, and day are valid or not.
    args:
       valyear: an integer between 1800 and 2500. If the year is a leap year, Feburary should
                be 29 days. Otherwise, there are 28 days in Febuary. 
       valmonth: integer 1..12 indicating month, January..December.
       valday: integer 1..31 for day of month. There are 30 days in month 4,6,9,11. 
    returns:
       True if numbers pass all the validations. 
    '''
    result = True
    if valyear < 1800 or valyear > 2500:
        result = False
    if valmonth < 1 or valmonth > 12:
        result = False
    if valday < 0 or valday > days_in_month(valmonth, valyear):
        return False
    return result         

def main():
    """
    Main program gets year number from command line, 
    invokes computation, reports result on output. 
    args: none (reads from command line)
    returns: none (write to standard output)
    effects: message or result printed on standard output
    """
    ## The standard way to get arguments from the command line, 
    ##    make sure they are the right type, and print help messages
    parser = argparse.ArgumentParser(description="Compute days from yyyy-mm-dd to next mm-dd.")
    parser.add_argument('year', type=int, help="Start year, between 1800 and 2500")
    parser.add_argument('start_month', type=int, help="Starting month, integer 1..12")
    parser.add_argument('start_day', type=int, help="Starting day, integer 1..31")
    parser.add_argument('end_month', type=int, help="Ending month, integer 1..12")
    parser.add_argument('end_day', type=int, help="Ending day, integer 1..12")
    args = parser.parse_args()  # will get arguments from command line and validate them
    year = args.year
    start_month = args.start_month
    start_day = args.start_day
    end_month = args.end_month
    end_day = args.end_day
        
    if not is_valid(year, start_month, start_day) :
        sys.exit("Must start on a valid date between 1800 and 2500")
    if not is_valid(2000, end_month, end_day):
        sys.exit("Ending month and day must be part of a valid date")
    print(days_between(year, start_month, start_day, end_month, end_day))



if __name__ == "__main__":
    main()
        
