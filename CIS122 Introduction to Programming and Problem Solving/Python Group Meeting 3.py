#http://interactivepython.org/runestone/static/thinkcspy/index.html
#http://cscircles.cemc.uwaterloo.ca/0-introduction/


import doctest

#Chapter 12
#Problem 1
#a Iterate over each character in the sequence from the beginning to end,
#  replacing each A, T, G, and C with its T, A, C, and G, respectively.

#b No.

#c
def complement(sequence):
    '''(str) -> str

    Return the complement of sequenc.

    >>> complement('AATTGCCGT')
    'TTAACGGCA'
    '''
    
    complement_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    sequence_complement = ''

    for char in sequence:
        sequence_complement = sequence_complement + complement_dict[char]


    return sequence_complement



#Problem 2
#a
'''
index = 0
smallest = L[0]

for i in range(1, len(L)):
    if L[i] < smallest:
        index = i
        smallest = L[i]'''

#b
def min_index(L):
    """ (list) -> (object, int)

    Return a tuple containing the smallest item from L and its index.

    >>> min_index([4, 3, 2, 4, 3, 6, 1, 5])
    (1, 6)
    """ 

    index = 0
    smallest = L[0]

    for i in range(1, len(L)):
        if L[i] < smallest:
            index = i
            smallest = L[i]

    return (smallest, index)

#c
def min_or_max_index(L, flag):
    """ (list, bool) -> tuple of (object, int)

    Return the minimum or maximum item and its index from L, depending on
    whether flag is True or False.

    >>> min_or_max_index([4, 3, 2, 4, 3, 6, 1, 5], True)
    (1, 6)
    >>> min_or_max_index([4, 3, 2, 4, 3, 6, 1, 5], False)
    (6, 5)
    """ 

    index = 0
    current_value = L[0]

    if flag:
        for i in range(1, len(L)):
            if L[i] < current_value:
                index = i
                current_value = L[i]
    else:
        for i in range(1, len(L)):
            if L[i] > current_value:
                index = i
                current_value = L[i]        

    return (current_value, index)

#Problem 3
#a
'''
- Read the description line.
- Keep reading the comment lines until we read the first piece of data.
- Add the first piece of data to an empty list.
- Read the remaining lines one at a time, appending the data to the list.
'''

#b
def hopedale_average(filename):
    ''' (str) -> float

    Return the average number of pelts produced per year for the data in Hopedale
    file named filename.
    '''
    with open(filename, 'r') as hopedale_file:
        # Read the description line.
        hopedale_file.readline()

        # Keep reading comment lines until we read the first piece of data.
        data = hopedale_file.readline().strip()
        while data.startswith('#'):
            data = hopedale_file.readline().strip()

        # Now we have the first piece of data append it to an empty list.
        pelts_list = []
        pelts_list.append(int(data))

        # Read the rest of the data.
        for data in hopedale_file:
            pelts_list.append(int(data.strip()))

    return sum(pelts_list) / len(pelts_list)



#Problem 4
def find_two_smallest(L):
    ''' (list of float) -> tuple of (int, int)

    Return a tuple of the indices of the two smallest values in list L.

    >>> find_two_smallest([809,834,477,478,307,122,96,102,324,476])
    (6, 7)
    >>> find_two_smallest([1,2])
    (0, 1)
    >>> find_two_smallest([3,2])
    (1, 0)
    >>> find_two_smallest([3,3])
    (0, 0)
    >>> find_two_smallest([3,1,3])
    (1, 0)
    >>> find_two_smallest([1,4,2,3,4])
    (0, 2)
    >>> find_two_smallest([4,3,1,5,6,2])
    (2, 5)
    >>> find_two_smallest([-2,4,3,2,5,6,-1])
    (0, 6)
    
    '''
    temp_list = sorted(L)
    smallest = temp_list[0]
    next_smallest = temp_list[1]

    min1 = L.index(smallest)
    min2 = L.index(next_smallest)

    return (min1,min2)

#Problem 5
'''If passed a list of length one, it should return a tuple containing the index of the smallest. If passed a list of length zero, it should return an empty tuple.

Return a tuple of the indices of the two smallest values in list L. 
If there is only one item in L or zero items in L, return a tuple
containing the index of that one item or an empty tuple, respectively.
'''
'''Actually, when the length is one or zero, Python tells that list out of range'''


#Problem 6
def dutch_flag(color_list):
    ''' (list of str) -> list of str

    Return rearrange the list so that the strings are in the order
    of the 'red','green','blue'.

    >>> color_list = ['red', 'green', 'blue', 'red', 'red', 'blue', 'red', 'green']
    >>> dutch_flag(['red', 'green', 'blue', 'red', 'red', 'blue', 'red', 'green'])
    >>> color_list
    ['red', 'red', 'red', 'red', 'green', 'green', 'blue', 'blue']
    '''

    color_sort = sorted(color_list)
    color_sort.reverse()

    return color_sort








##print(doctest.testmod())
