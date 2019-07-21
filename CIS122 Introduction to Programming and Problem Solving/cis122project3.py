# Problem 0
# Part 1
def max_trans(a,b,c):
    '''(number,number,number) -> number

    This function returns the maximum weight
    that can be transported along this road.
    This function should take the values of a, b,
    and c as input.
    
    >>> max_trans(95.9,56,75)
    56
    >>> max_trans(100,58,65.3)
    58
    >>> max_trans(15.8,56,23)
    15.8

    '''
    maxweight = min(a,b,c)
    return maxweight 
    
# Part 2 
def max_trans2(a,b,c,d,e):
    '''(number,number,number,number,number) -> number

    This function returns the maximum weight
    that can be transported between the two cities.
    This function should take the values of a, b,
    c, d, and e as input.

    >>> max_trans2(126, 238, 326, 413, 515)
    413
    >>> max_trans2(222, 110, 411, 54, 73)
    110
    >>> max_trans2(227, 337, 135, 56, 73)
    135
    '''
    maxweight = max(min(a,b,c),min(d,e))
    return maxweight


# Problem 1
def tip_calc(bill):
    '''(number) -> None

    This function has one parameter, a restaurant
    bill total,and prints suggestions for tips at
    18% of the total bill.
    
    >>> tip_calc(28.60)
    $ 5.15
    >>> tip_calc(48)
    $ 8.64
    >>> tip_calc(10)
    $ 1.8
    '''
    tip = round((0.18 * bill),2)
    print('$',tip)
    return #None


# Problem 2
def nice_name():
    '''() -> None

    The function prompts the user for
    their name, and then display their name
    prominently for all to see.
    This function takes a string and prints
    a string.
    
    >>> nice_name()
    What is your name? Hermione
    
    ************
    * HERMIONE *
    ************
    '''
    name = input('What is your name? ')
    name = name.upper()
    print('*'*len(name) + '*'*4)
    print('* ' + name + ' *' ) 
    print('*'*len(name) + '*'*4)
    return #None


# Problem 3
def monogram():
    '''() -> string,string,string

    This function  asks a user for three inputs:
    their first name, middle initial, and last name,
    and returns 3 initials in "monogram order" (first,
    last, middle).

    >>> monogram()
    First name:Hao
    Middle initial:M
    Last name:He
    >>>('H', 'H', 'M')


    '''
    firstname = input('First name:')
    middleinitial = input('Middle initial:')
    lastname = input('Last name:')

    return firstname[0],lastname[0],middleinitial[0]


# Problem 4
from turtle import *
def sun_and_earth():
    '''() -> None

    This function uses Turtle Graphics to illustrate
    the relative size of the sun and the earth by
    drawing two circles.
    The diameter of the Sun is 1,392,000 km, while
    the equatorial diameter of the Earth is 12,756 km
    (a ratio of about 109:1). 

 
    '''
    SizeSun = 1392000
    SizeEarth = 12756
    circle(SizeSun / SizeEarth)
    circle(SizeEarth / SizeEarth)

    return #None


# Problem Challenge
def print_anagram(original, answer):
    '''string, string -> None

    This function takes two parameters and
    prints them.

    '''
    print('original:' + original)
    print('anagram:' + answer)
    return #None


def anagram():
    '''() -> None

    This function takes original words or phrases
    to make new words or phrases.

    >>> anagram()
    original:lemon
    anagram:melon
    original:eat
    anagram:tea

    '''
    original ='lemon'
    answer = original[2] + original[1] + original[0] + original[3:]
    print_anagram(original, answer)
#1
    original = 'eat'
    answer = original[2] + original[:2]
    print_anagram(original, answer)

#2
    original = 'brush'
    answer = original[3] + original[4] + original[1] + original[2] + original[0]
    print_anagram(original, answer)
#3
    original = 'rail'
    answer = original[::-1]
    print_anagram(original, answer)
#4
    original = 'skate'
    answer = original[1] + original[4] + original[2] + original[3] + original[0]
    print_anagram(original, answer)
#5
    original = 'wand'
    answer = original[3] + original[1] + original[0] + original[2] 
    print_anagram(original, answer)
#6
    original = 'alice'
    answer = original[3:] + original[1] + original[2] + original[0] 
    print_anagram(original, answer)
#7
    original = 'dorothea'
    answer = original[4:7] + original[1] + original[0] + original[3] + original[2] + original[7]
    print_anagram(original, answer)
#8
    original = 'supersonic'
    answer = original[2:5] + original[9] + original[1] + original[0] + original[0] + original[8] + original[6] + original[7]
    print_anagram(original, answer)
#9
    original = 'hormone'
    answer = original[3] + original[1] * 2 + original[2] + original[0] + original[6] + original[5] 
    print_anagram(original, answer)

#10
    original = 'spectrum'
    answer = original[3] + original[5] + original[6] + original[7] + original[1] + original[2] + original[4] + original[0]
    print_anagram(original, answer)
#11
    original = 'stale lamb'
    answer = original[8] + original[4] + original[2] + original[1] + original[9] + original[2] + original[3]*2 + original[0]
    print_anagram(original, answer)
#12
    original = 'listen'
    answer = original[2] + original[1] + original[0] + original[4] + original[5] + original[3]
    print_anagram(original, answer)
    
    return #None

    
























    
