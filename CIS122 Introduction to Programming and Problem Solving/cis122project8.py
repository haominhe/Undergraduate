import doctest 

# Problem 0 
def same_first_last(L):
    '''(list) -> boolean

    Precondition: len(L) >= 2

    Returns True if the first item of the list is
    the same as the last; else returns False.

    >>> same_first_last([3,4,2,8,3])
    True
    >>> same_first_last(['apple','banana','pear'])
    False
    >>> same_first_last([4.0,4.5])
    False
    '''
    if L[0] == L[-1]:
        return True
    else:
        return False
    


# Problem 1
def is_longer(L1,L2):
    '''(list,list) -> boolean

    Return True if the length of L1 is longer than
    the length of L2; else return False.

    >>> is_longer([1,2,3],[4,5])
    True
    >>> is_longer(['abcdef'],['ab','cd'])
    False
    >>> is_longer(['a','b','c'],[1,2,3])
    False
    '''
    if len(L1) > len(L2):
        return True
    else:
        return False



# Problem 2
# (a) & (b)
def mySum(listnum):
    '''(list) -> number

    This function has one parameter, a list of numbers, listnum.
    mySum returns the sum of the numbers in the input list.

    >>> mySum([1,2,3])
    6
    >>> mySum([1,2,3,4,5,6,7,8,9])
    45
    >>> mySum([1,2,3,0,0,0,1])
    7
    >>> mySum([71,2.3,35])
    108.3
    >>> mySum([-58,0.7,0,6])
    -51.3
    '''
    ctr = 0; plusnum = 0
    while ctr < len(listnum):
        plusnum += listnum[ctr]
        ctr += 1
    return plusnum
print(doctest.testmod())



# Problem 3
# (a) & (b)
def odd(L):
    '''(list) -> number

    This function takes a list L as its argument, and returns
    length of the list integer divided by 2.

    >>> odd([5,6,3,7])
    2
    >>> odd([5,6,3,7,8,59,9])
    3
    >>> odd([8,0,100,12,1])
    2
    >>> odd([1,2,3,4,5,6])
    3
    '''
    oddL = len(L) // 2
    return oddL

def middle(L):
    '''(list) -> item / number

    This function takes a list L as its argument, and returns
    the item in the middle position of L, when L has an odd
    length. Otherwise, middle should return 999999.

    >>> middle([8,0,100,12,1])
    100
    >>> middle([8,0,100,12,1,8])
    999999
    >>> middle([1,2,3,4,5])
    3
    >>> middle([1,2,3,4,5,6])
    999999
    >>> middle([-5,-4,-3,-2,-1,0,1,2,3,4,5,6])
    999999
    >>> middle([-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6])
    0
    '''
    position = odd(L)
    if len(L) % 2 == 1:
        return L[position]
    else:
        return 999999
print(doctest.testmod())



# Problem 4
def check(S):
    '''(string) -> boolean

    This function takes a string S as input. First, if the string
    does not follow the format "#### #### #### ####" where each #
    is a digit, then it should return False. Then, if the sum of
    the digits is divisible by 10, then the procedure should return
    True, else it should return False. Zero is not considered to be
    divisible by 10, that is, a string of all zeros should return False.

    >>> check('2768 3424 2345 2358')
    False
    >>> check('9384 3495 3297 0121')
    True
    >>> check('1876 0954 325009182')
    False
    >>> check('0000000000000000')
    False
    >>> check('0000 0000 0000 000')
    False
    >>> check('0 0 0 0000000000000')
    False
    >>> check('')
    False
    >>> check('0000 0000')
    False
    >>> check('0123 4567 8902 4568')
    True
    >>> check('0123 4567 89AB EFGH')
    False
    >>> check('0123 4567 89AB 5555')
    False
    '''
    L = S.split()
    if  len(L) != 4:
           return False

    for item in L:
        if not item.isdigit():
            return False 

    for part in L:
        if len(part) != 4:
            return False

    summ = 0
    for part in L:
        for num in part:
            summ += int(num)
    
    if summ == 0:
           return False
    elif summ % 10 != 0:
           return False
    else:
           return True
    



# Challenge
def nestedListContains(nl,target):
    '''(list) -> boolean

    This function takes a nested list nl of integers and an integer
    target, and indicates whether target is contained anywhere in the
    nested list. The code returnd the boolean value True when it is
    contained in the nested list, and False if it is not contained in it.

    >>> nestedListContains([1,[2,[3],4]],3)
    True
    >>> nestedListContains([1,[2,[3],4]],5)
    False
    '''
    for item in nl:
        
        if isinstance(item,int):
            
            if item == target:
                
                return True
        else:
            return nestedListContains(item, target)
    # end for loop          
    return False         
    
       
    
            
    

    





















