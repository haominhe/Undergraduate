"""CIS 211 Winter 2015
    Project 7: Functional Programming
    Haomin He

    The project this week is to write small Python functions that each use one
    or more functional programing (FP) constructs.

    Also tried Extra Credit Ideas.
"""


def codes(string):
    """1. Write a function named codes that returns a list of numeric codes for
       the characters in a string. If ch is a character (i.e. a 1-letter string)
       the builtin function named ord will return its character code.
    """
    return list(map(ord, string))


from functools import reduce
from operator import add
def vowels(string):    
    """2. Write a function named vowels that will return a string made from the
       vowels (letters A, E, I, O, and U) in a string
       Note that the vowels are returned in order, and that case is preserved. 
    """
    var = list(filter(lambda s: s in ['a','e','i','o','u','A','E','I','O','U'], string))
    return "".join(var)  # join a list into a string


from string import punctuation 
def tokens(string):
    """3. Write a function named tokens that will split an input string into
       individual words and remove the punctuation marks from the ends of the
       words. The result returned from the function should be a map object;
       to see the individual words pass this object in a call to list:
    """
    return (map(lambda x: x.strip(punctuation), string.split()))


def numbers(string):
    """4. Write a function named numbers that will use your tokens function to
       break a line into words and then return the tokens that contain nothing
       but digits
    """
    return list(filter(str.isdigit, list(tokens(string))))


def sq_ft(file):
    """5. Write a function named sq_ft that will compute the total area of a
       house by adding up the areas of the individual rooms. The argument
       passed to sq_ft will be the name of a file containing the dimensions
       of the rooms.
       sq_ft function can create a Room object from the description of each
       line in the input file and the sq_ft function call area to compute the
       area of each room.
    """
    allroom = [Room(line).area() for line in map(str.strip, list(open(file)))]
    return reduce(add, allroom)
        

class Room:
    """The constructor will initialize an object from a string with the name
       and dimensions.
    """
    def __init__(self, string):
        a, b, c = string.split()
        self.room = a
        self.dimension1 = int(b)
        self.dimension2 = int(c)
        
    def area(self):
        """a method named area that will compute the area of a room"""
        return float(self.dimension1 * self.dimension2)


#Extra Credit Ideas
from operator import xor
def checksum(string):
    """Write a function name checksum that will compute the bitwise exclusive
       OR of all the binary codes in a string. 
    """
    return reduce(xor, list(map(ord, list(string))))
    











