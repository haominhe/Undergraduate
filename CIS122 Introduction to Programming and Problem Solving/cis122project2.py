# Problem 0
def kilo_to_miles(x):
    """  (number) -> float
    
    This fuction has one parameter, a distance in kilometers,
    and returns the distance in miles.
    (There are 1.6 kilometers per mile.)
    
    >>> kilo_to_miles(5)
    3.125
    >>> kilo_to_miles(10)
    6.25
    >>> kilo_to_miles(0)
    0.0
    """
    
    return x / 1.6


# Problem 1
def tip_calc(bill):
    """ (number) -> (float, float, float)

    This function has one parameter, a restaurant bill total,
    and returns suggestions for tips at 15%, 18% and 20% of the total bill.
    
    >>> tip_calc(10)
    (1.5, 1.7999999999999998, 2.0)
    >>> tip_calc(28.60)
    (4.29, 5.148, 5.720000000000001)
    >>> tip_calc(50)
    (7.5, 9.0, 10.0)
    """
    return (bill * 0.15,bill*0.18,bill*0.2)


# Problem 2
# a)
def convert_to_celsius(Fahrenheit):
    '''(number) -> float

    This function will have one input,
    a Fahrenheit temperature,
    and return its Celsius equivalent.

    >>> convert_to_celsius(212)
    100.0
    >>> convert_to_celsius(32)
    0.0
    >>> convert_to_celsius(70)
    21.11111111111111
    '''
    return (Fahrenheit-32) * 5/9

# b)
def convert_to_fahrenheit(Celsius):
    '''(number) -> float

    This function will have one input,
    a Celsius temperature,
    and return its Fahrenheit equivalent.

    >>> convert_to_fahrenheit(100)
    212.0
    >>> convert_to_fahrenheit(0)
    32.0
    >>> convert_to_fahrenheit(21.1)
    69.98
    '''
    return Celsius * 9/5+ 32


# Problem 3
# a)
def chirps_to_ftemp(chirpsin14sec):
    '''(int) -> int

    This function takes as input the number of cricket chirps in a 14 second interval,
    and returns the outdoor temperature in Fahrenheit degrees.

    >>> chirps_to_ftemp(30)
    70
    >>> chirps_to_ftemp(55)
    95
    >>> chirps_to_ftemp(0)
    40
    '''
    return chirpsin14sec + 40

# b)
def chirps_to_ctemp(chirpsin25sec):
    '''(int) -> float

    This function takes an input the number of cricket chirps in a 25 second interval,
    and returns the outdoor temperature in Celsius.
    
    >>> chirps_to_ctemp(48)
    20.0
    >>> chirps_to_ctemp(93)
    35.0
    >>> chirps_to_ctemp(0)
    4.0
    '''
    return chirpsin25sec / 3 + 4

# c)
def chirps_to_ctemp2(chirpsin14sec2):
    '''(int) -> float

    This function takes as input the number of cricket chirps in a 14 second interval,
    and returns the outdoor temperature in Celsius.

    >>> chirps_to_ctemp2(30)
    21.11111111111111
    >>> chirps_to_ctemp2(55)
    35.0
    >>> chirps_to_ctemp2(0)
    4.444444444444445
    '''
    Fahrenheit = chirpsin14sec2 + 40
    Celsius = convert_to_celsius(Fahrenheit)
    return Celsius


# Problem 4
def minimum_payment(balance):
    '''(number) -> number

    A credit card company computes a customer's "minimum payment" according to the following rule.
    The minimum payment is equal to either $15 or 2.5% of the customer's balance (.025 * balance),
    whichever is greater; but if this exceeds the balance, then the minimum payment is the balance.
    This function takes an input balance, then uses Python's built in min and max functions to
    determine the minimum payement, which is returned.
    
    >>> minimum_payment(1000)
    25.0
    >>> minimum_payment(800)
    20.0
    >>> minimum_payment(25)
    15
    >>> minimum_payment(10)
    10
    '''
    return min(max(15, 0.025*balance), balance)

# Extra Credit Challenge
# a) Binary to Decimal
>>> int('100011',2)
35
>>> int('11',2)
3
>>> int('101010',2)
42
>>> int('111111',2)
63

# Decimal to Binary
>>> bin(64)
'0b1000000'
>>> bin(44)
'0b101100'
>>> bin(22)
'0b10110'
>>> bin(1)
'0b1'

# b)
>>> 8^12
4
>>> 64^32
96
>>> 1^0
1
>>> 15^1
14
