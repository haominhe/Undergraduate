#Chapter 11
import doctest
#5 
def subatomic(atomic):
    smallest = 1
    name = ''
    for particle in atomic:
        probability = atomic[particle]
        if probability < smallest:
            smallest = probability
            name = particle

    return particle

#6
def count_duplicates(dictionary):
    duplicates = 0
    values = list(dictionary.values())

    for item in values:
        if values.count(item) >= 2:
            duplicates = duplicates +1

            num_occurrences = values.count(item)
            for i in range(num_occurrences):
                values.remove(item)
    return duplicates

#7
def is_balanced(dictionary):
    '''(dict of {str: float}) -> bool

    Return True if and only if color_to_factor represents a balanced color.
    >>> is_balanced({'R': 0.5, 'G': 0.4, 'B': 0.7})
    False
    >>> is_balanced({'R': 0.3, 'G': 0.5, 'B': 0.2})
    True

    '''
    
    val = list(dictionary.values())
    val = sum(val)
    if val == 1:
        return True
    else:
        return False

#8
def dict_interest(dic1,dic2):
    ''' (dict, dict) -> dict

    Return a new dictionary that contains only the key/value pairs that occur
    in both dict1 and dict2.

    >>> dict_interest({'a': 1, 'b': 2, 'c': 3}, {'a': 1, 'd': 2, 'b': 2})
    {'a': 1, 'b': 2}

    '''
    dicset = {}
    
    for k1,v1 in dic1.items():
        if k1 in dic2 and v1 == dic2[k1]:
                dicset[k1] = v1

    return dicset

#9
def db_headings(dict_of_dict):
    '''(dict of dict) -> set

    Return a set of the keys in the inner dictionaries in dict_of_dict.

    >>> db_headings({'A': {1: 'a', 2: 'b'}, 'B': {2: 'c', 3: 'd'}})
    {1, 2, 3}

    '''
    inner_keys = set()

    for key in dict_of_dict:
        for keysub in dict_of_dict[key]:
            inner_keys.add(keysub)

    return inner_keys

#10
def db_consistent(dict_of_dict):
    '''(dict of dict) -> set

    Return whether all inner dictionaries in dict_of_dict contain the same keys.

    >>> db_consistent({'A': {1: 'a', 2: 'b'}, 'B': {2: 'c', 3: 'd'}})
    False
    >>> db_consistent({'A': {1: 'a', 2: 'b'}, 'B': {2: 'c', 1: 'd'}})
    True

    '''
    inner_keys_list = [] #list 

    for key in dict_of_dict:
        inner_keys = list(dict_of_dict[key].keys())
        inner_keys.sort()
        inner_keys_list.append(inner_keys)


    for i in range(1, len(inner_keys_list)):
        if len(inner_keys_list[0]) != len(inner_keys_list[i]):
              return False

        for j in range(len(inner_keys_list[0])):
               if inner_keys_list[0][j] != inner_keys_list[i][j]:
                   return False

    return True 

#11
#a
def sparse_add(vec1,vec2):
    """ (dict of {int: int}, dict of {int: int} -> dict of {int: int})

    Return the sum of sparse vectors vector1 and vector2.

    >>> sparse_add({1: 3, 3: 4}, {2: 4, 3: 5, 5: 6})
    {1: 3, 2: 4, 3: 9, 5: 6}
    """ 
    sum1 = vec1.copy()

    for key in vec2:
        if key in sum1:
            sum1[key] = sum1[key] + vec2[key]
        else:
            sum1[key] = vec2[key]
    return sum1

#b
def sparse_dot(vec1,vec2):
    """ (dict of {int: int}, dict of {int: int} -> dict of {int: int})

    Return the dot product of sparse vectors vector1 and vector2.

    >>> sparse_dot({1: 3, 3: 4}, {2: 4, 3: 5, 5: 6})
    20
    """
    dot = 0

    for key1 in vec1:
        if key1 in vec2:
            dot = dot + vec1[key1] * vec2[key1]
    return dot
    
#c    
#Since only non-zero entries are stored, will the last entry always be non-zero?
# If not, how will the last entry be represented in the dictionary?
















print(doctest.testmod())
