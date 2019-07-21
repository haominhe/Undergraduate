# Project 1: Warmup
# Haomin He

# 2. print_names
"""This program will read a set of names from a
   text file and print them in the terminal window,
   by the required order.
   I also tried the Extra Credit Ideas about inits.
"""

from sys import argv

class Name:
    """When a new Name object is created pass the
       constructor two strings: first and last name.
    """
    def __init__(self, first, last):
        """This function will create the first and
           last name of the Name object.
           Args:
               first: first name
               last: last name
           Returns:
               None
        """
        self._first = first
        self._last = last

    def __repr__(self):
        """First and last name are separated by a space.
           Returns:
               first name (space) last name
        """
        return self._first + " " + self._last

    def __lt__(self, other):
        """Compare two names by less than.
           Returns:
               True or False
        """
        return self._first < other._first
    
    def first(self):
        """Returns the first name.
        """
        return self._first
    
    def last(self):
        """Returns the last name.
        """
        return self._last
    
def name_list(textfile):
    """This function takes the name of a text file as
       an argument and returns a list of Name objects,
       one for each line from the file.
       Args: textfile
       Returns: a list of Name objects
    """
    
    list_names = []
    for eachname in open(textfile):
        f,l = eachname.split()
        list_names.append(Name(f,l))
    return list_names

def print_names(list_names, order):
    """This function takes a list of names and a string
       that specifies the sort order.
       Args: list of names, sort order
       Returns: None
       Prints: the sorted name list
    """

    if order == 'last':
        list_names.sort(key = Name.last)
        for each_name in list_names:
            firstN, lastN = each_name.first(), each_name.last()
            if len(argv) == 4:
                print(lastN + ",", firstN[0] + ".")
            else:
                print(lastN + ",", firstN)
        
    elif order == 'first':
        list_names.sort(key = Name.first)
        for each_name in list_names:
            firstN, lastN = each_name.first(), each_name.last()
            if len(argv) == 4:
                print(firstN[0] + ".", lastN)
            else:
                print(each_name)

            
if __name__ == "__main__":
    nlst = name_list(argv[1])
    print_names(nlst, argv[2])
    
    

