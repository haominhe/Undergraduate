import doctest


# Problem 0
#(a) Generate a series of examples to test find_min_and_max.
#    Put them in the form of the example in the docstring.

'''(string) -> None

Find the maximum and minimum values in a non-empty string
of integers and print them. No value is returned.

>>> find_min_and_max('53489')
The minimum value is 3.
The maximum value is 9.
>>> find_min_and_max('456312')
The minimum value is 1.
The maximum value is 6.
>>> find_min_and_max('0123456789')
The minimum value is 0.
The maximum value is 9.
>>> find_min_and_max('')
The minimum value is None.
The maximum value is None.
>>> find_min_and_max('65154')
The minimum value is 1.
The maximum value is 6.
>>> find_min_and_max('0')
The minimum value is 0.
The maximum value is 0.
>>> find_min_and_max('9')
The minimum value is 9.
The maximum value is 9.
>>> find_min_and_max('09')
The minimum value is 0.
The maximum value is 9.
'''


#(b)
def find_min_and_max(values):
    '''(string) -> None

    Find the maximum and minimum values in a non-empty string
    of integers and print them. No value is returned.

    >>> find_min_and_max('45312')
    The minimum value is 1.
    The maximum value is 5.
    >>> find_min_and_max('456312')   #Add more examples. 
    The minimum value is 1.
    The maximum value is 6.
    >>> find_min_and_max('53489')
    The minimum value is 3.
    The maximum value is 9.
    >>> find_min_and_max('0123456789')
    The minimum value is 0.
    The maximum value is 9.
    >>> find_min_and_max('')
    The minimum value is None.
    The maximum value is None.
    >>> find_min_and_max('65154')
    The minimum value is 1.
    The maximum value is 6.
    >>> find_min_and_max('0')
    The minimum value is 0.
    The maximum value is 0.
    >>> find_min_and_max('9')
    The minimum value is 9.
    The maximum value is 9.
    >>> find_min_and_max('09')
    The minimum value is 0.
    The maximum value is 9.
    '''
    mini = None  #Can not use Python functions as variable names. 
    maxi = None  #Use mini and maxi as variable names and assign them to None. 

    if len(values) != 0:  #Add a if statement. So that find_min_and_max(values)
        mini = values[0]  #fuction also works on empty string. 
        maxi = values[0]
        mini = int(mini)
        maxi = int(maxi)

    for value in values:
        value = int(value)  #Change string number to integer number. 
        if value > maxi:
            maxi = value
        if value < mini:
            mini = value
    

    print('The minimum value is {}.'.format(mini))    #Add period
    print('The maximum value is {}.'.format(maxi))

    return #Nones



# Problem 1
#(a)
'''(string) -> float

returns average of values in input string values,
but zeros do not count at all

>>> my_average('23')
2.5
>>> my_average('203')
2.5
>>> my_average('6124')
3.25
>>> my_average('01235')
2.75
>>> my_average('98745663210')
5.1
>>> my_average('210')
1.5
>>> my_average('01')
1.0
>>> my_average('1')
1.0
>>> my_average('0')
0
>>> my_average('')
0
>>> my_average('000')
0

'''


#(b)
def my_average(values):
    '''(string) -> float

    Returns average of values in input string values,
    but zeros do not count at all.
    This function that computes the average product
    rating from the data set, which is a function parameter
    of type string. Zeros do not count toward the average.
    For no usable data, return 0.
                                     #Better docstring.
                                     
    >>> my_average('23')
    2.5
    >>> my_average('203')
    2.5
    >>> my_average('6124')
    3.25
    >>> my_average('01235')
    2.75
    >>> my_average('98745663210')
    5.1
    >>> my_average('210')
    1.5
    >>> my_average('01')             #Add more examples.
    1.0
    >>> my_average('1')
    1.0
    >>> my_average('0')
    0
    >>> my_average('')
    0
    >>> my_average('000')
    0

    '''
    count = 0
    total = 0
    for value in values:
        if value != '0':
            total += int(value)
            count += 1
                                #Add a tab in front of (count) to align
                                #with (total), not align with if function.
            
    if count != 0:              #Add a new if statement, so the fuction returns
        avg = total / count     #zero for no useble data. 
    else:
        return 0
 
    return avg




# Problem 2
#(a)
'''int -> None

Prints a right triangle with n lines, where the first line prints 1 'T'
and the last line prints n 'T's.

>>> ttriangle(6)
T
TT
TTT
TTTT
TTTTT
TTTTTT
>>> ttriangle(8)
T
TT
TTT
TTTT
TTTTT
TTTTTT
TTTTTTT
TTTTTTTT
>>> ttriangle(4)
T
TT
TTT
TTTT
>>> ttriangle(0)
>>> ttriangle(-1)
>>> ttriangle(1)
T

'''


#(b)
def ttriangle(n):
    '''int -> None

    Prints a right triangle with n lines, where the first line prints 1 'T'
    and the last line prints n 'T's.

    >>> ttriangle(6)
    T
    TT
    TTT
    TTTT
    TTTTT
    TTTTTT
    >>> ttriangle(8)
    T
    TT
    TTT
    TTTT
    TTTTT
    TTTTTT
    TTTTTTT
    TTTTTTTT
    >>> ttriangle(4)
    T
    TT
    TTT
    TTTT
    >>> ttriangle(0)
    >>> ttriangle(-1)
    >>> ttriangle(1)
    T

                                         #Add more examples. 
    '''
    ct = 1
    while ct <= n:          #Change the sign < to <=. 
        print('T' * ct)
        ct += 1             #Add a counter. 

    return #None




# Problem 3
def minutesToHours(minutes):
    '''(number) -> float

    convert input minutes to hours;
    return hours

    >>> minutesToHours(60)
    1.0
    >>> minutesToHours(90)
    1.5
    >>> minutesToHours(0)
    0.0
    '''
    hours = minutes / 60
    hours = round(hours, 2)
    return hours                #Change (print) to (return). 
    
def hoursToDays(hours):
    '''(number) -> float

    convert input hours to days;
    return days

    >>> hoursToDays(24)
    1.0
    >>> hoursToDays(100)
    4.17
    >>> hoursToDays(0)
    0.0
    '''
    days = hours / 24
    days = round(days,2)        #Add round function. 
    return days

def daysToYears(days):
    '''(number) -> float

    convert input days to years;
    return years

    >>> daysToYears(365)
    1.0
    >>> daysToYears(100)
    0.27
    >>> daysToYears(0)
    0.0
    '''
                                #Delete the local variable (days = 365).
    years = days / 365
    years = round(years, 2)
    return years

def minutesToYears(m):
    '''(int) -> float

    input number m minutes is converted to
    equivalent number of years. return years.
    call auxiliary functions to do each step

    >>> minutesToYears(525600)
    1.0
    >>> minutesToYears(5256000)
    10.0
    >>> minutesToYears(394200)
    0.75
    >>> minutesToYears(0)
    0.0
    '''
    h = minutesToHours(m)       #Add missing variables. 
    d = hoursToDays(h)
    y = daysToYears(d)

    return y


























