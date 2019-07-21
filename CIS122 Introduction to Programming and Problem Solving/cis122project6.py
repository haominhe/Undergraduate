from turtle import *
import random

# Problem 0
def transcribe(S):
    '''(string) -> string

    This fuction has one parameter, a string S, which will have DNA nucleotides
    (capital letter As, C, Gs, and Ts). There may be other characters, too, though
    they will be ignored by your transcribe function -- these might be spaces or
    other characters that are not really DNA nucleotides.
    Then, transcribe should return as output the messenger RNA that would be produced
    from that string S. The correct output simply uses replacement:
    'A's in the input become 'U's in the output.
    'C's in the input become 'G's in the output.
    'G's in the input become 'C's in the output.
    'T's in the input become 'A's in the output.
    Any other input characters should not appear in the output.

    >>> transcribe('ACGT TGCA')
    'UGCAACGU'
    >>> transcribe('GATTACA')
    'CUAAUGU'
    >>> transcribe('cs5') # lowercase doesn't count
    ''

    '''
    i = 0
    S1 = ''
    while i < len(S):
        if S[i] == 'A':
            S1 += 'U'
        elif S[i] == 'C':
            S1 += 'G'
        elif S[i] == 'G':
            S1 += 'C'
        elif S[i] == 'T':
            S1 += 'A'
        i += 1
    return S1



# Problem 1
def rover_loc():
    '''() -> int

    return random number for rover location

    >>> rover_loc()
    200 [for example]
    '''
    return random.randint(-275, 275)

def water_content():
    '''() -> int

    return random measure of water content on mars

    >>> water_content
    150 [for example]
    '''
    return random.randint(1, 290)

def temp():
    '''() -> int

    return random measure of temp on mars

    >>> temp()
    -100 [for example]
    '''
    return random.randint(-178, 1)

# (challenge)
def display(wc, t, x, y):
    '''(int, int, int, int) -> None

    display values of wc and t at pos x,y
    '''
    pu(); setpos(x-25, y+20); pd()
    write(wc, font=('Arial', 12, 'normal'))
    pu(); setpos(x, y+20); pd()
    write(t, font=('Arial', 12, 'normal'))
    # return turtle to original position
    pu(); setpos(x,y); pd()

    return #None


def mars_explore():
    '''() -> None

    remote control exploration of Mars:
        get new position (call rover_loc)
        go to the new position
        collect data there (call water_content/temp)
        display data there (optional display call)

    data is printed; no value is returned
    ''' 
    next_x = rover_loc()   # get next position (x,y)
    next_y = rover_loc()   # for rover explore path

    seth(towards(next_x, next_y))# nice - point rover
    stamp()                      # to show direction
    
    setpos(next_x,next_y)       # move the rover

    # gather data at this location
    wc = water_content()        
    t = temp()

    # print the data 
    print(next_x,"\t", next_y, "\t", wc, "\t", t)

    # (challenge) display data in turtle window
    display(wc, t, next_x, next_y)
    return #None

def square(side, scolor):
    '''(number, str) -> None

    draw a square with sides length side
    and filled in with color
    no value is ret'd

    >>> square(100, 'red')
    >>> square(25, 'cyan')
    '''
    fillcolor(scolor)
    begin_fill()
    
    fd(side)
    lt(90)

    fd(side)
    lt(90)

    fd(side)
    lt(90)

    fd(side)
    lt(90)

    end_fill()

    return #None

def mars_explore_main(num_trips):
    '''(num) -> None
    This frunction has one parameter,
    num_trips. It calls the mars_explore
    fuction num_trips times.
    
    main function for mars_explore:
        set up print and graphical output
        then call mars_explore repeatedly

    data is printed; no value is returned

    >>> mars_explore_main(100)
    '''
    
    # label for print output   
    print("xpos", "\t",
          "ypos", "\t",
          "water", "\t",
          "temp")           

    # set up graphical output
    reset()
    speed(0)
    title("Mars Rover")
    display_color = "blue"
    color(display_color)
    square(10, display_color)   # draw the rover

    # explore five places on Mars

    i = 0
    while i < num_trips:
        mars_explore()
        i += 1
 
    return #None


# Problem 2 Turtle Spirolaterals
def spirolateral(name):
    '''(string) -> None

    Draw a spirolateral of the input name.
    No value is returned.

    For example,
    spirolateral('Ducks')
    '''
    name = name.upper() 
    start = ord('A')
    multiplier = 5

    ctr = 0
    while ctr < len(name):
        ch = name[ctr]
        letter_place = ord(ch) - start + 1
        fd(letter_place * multiplier)
        rt(90)
        ctr += 1

    return #None

def spirolateral_main(name):
    '''(string) -> None

    This function that takes one input, name, and calls spirolateral
    (passing name as the input arg) as many times as there are
    letters in name. No value is returned. In the example below,
    spirolateral_main calls spirolateral five times.

    spirolateral_main('Ducks')
    '''
    reset()
    i = 0
    while i < len(name):
        spirolateral(name)
        i += 1
    return #None



# Problem 3
# a
def rats1(startw):
    '''(number) -> number

    This function has one parameter, startw. If the rat gains weight
    at rate of 4 percent a week, calculate how many weeks it would take
    for the weight of the first rat to become 25 percent heavier than it
    was originally. Print the start weight and final weight (rounded to
    one decimal place) and the number of weeks. The function should return
    the value of the number of weeks.

    >>> rats1(10)
    At start (week 0),
    rat1 weight is 10.
    At week 6,
    rat1 weight is 12.7.
    6

    '''
    rate = 4 / 100
    weeks = 0
    final_w = startw
    while final_w < startw + startw * 0.25:
        weeks += 1
        final_w +=  final_w * rate
    final_w = round(final_w,1)
    string = ('At start (week 0),\nrat1 weight is {}.\nAt week {},\nrat1 weight is {}.')
    print(string.format(startw, weeks, final_w))
    return weeks

# b
def rats2(startw):
    '''(number) -> number

    This function has one parameter, startw. Both rat1 and rat2 have
    the same initial weight (startw), but rat1 is expected to gain weight
    at a faster rate than rat2 (5 percent and 3 percent per week).
   
    Calculate how many weeks it will take for rat1 to be 10 percent heavier
    than rat2. Print the start weight and final weight (rounded to one decimal
    place) and the number of weeks. The function should return the value of
    the number of weeks.

    >>> rats2(10)
    At week 5,
    rat1 weight is 12.8 and
    rat2 weight is 11.6.
    5

    '''
    rate1 = 5 / 100
    rate2 = 3 / 100
    rate3 = 10 / 100
    final_w1 = startw 
    final_w2 = startw 
    weeks = 0
    while final_w1 < final_w2 + final_w2 * rate3:
        weeks += 1
        final_w1 += final_w1 * rate1
        final_w2 += final_w2 * rate2
    final_w1 = round(final_w1,1)
    final_w2 = round(final_w2,1)

    string = ('At week {},\nrat1 weight is {} and\nrat2 weight is {}.')
    print(string.format(weeks, final_w1, final_w2))
    return weeks



# Problem 4 Frequency count
def letter_freq(typestr):
    '''(string) -> None

    This function letter_freq, has one parameter, that takes one input
    parameter of type string, and for each vowel ('a', 'e', 'I', 'o', 'u')
    prints how many times the vowel occurs in the input string.
    No value (None) is returned.

    >>> letter_freq('The quick brown fox')
    a: 0
    e: 1 
    i: 1
    o: 2
    u: 1

    '''
    typestr = typestr.lower()
  
    a = typestr.count('a')
    e = typestr.count('e')
    i = typestr.count('i')
    o = typestr.count('o')
    u = typestr.count('u')

    typestr1 = ('a: {}\ne: {} \ni: {}\no: {}\nu: {}')
    print(typestr1.format(a,e,i,o,u))
    return #None



# Challenge: implement letter_freq without using a Python string method.
def letter_Chal(typestr):
    '''(string) -> None

    This function letter_Chal, has one parameter , that takes one input
    parameter of type string, and for each vowel ('a', 'e', 'I', 'o', 'u')
    prints how many times the vowel occurs in the input string.
    No value (None) is returned.

    >>> letter_Chal('The quick brown fox')
    a: 0
    e: 1 
    i: 1
    o: 2
    u: 1

    '''
    typestr = typestr.lower()
    a = 0
    e = 0
    i = 0
    o = 0
    u = 0
    Xcounter = 0
    while Xcounter < len(typestr):
        if typestr[Xcounter] == 'a':
            a += 1
        if typestr[Xcounter] == 'e':
            e += 1
        if typestr[Xcounter] == 'i':
            i += 1
        if typestr[Xcounter] == 'o':
            o += 1
        if typestr[Xcounter] == 'u':
            u += 1
                      
        Xcounter += 1

    typestr1 = ('a: {}\ne: {} \ni: {}\no: {}\nu: {}')
    print(typestr1.format(a,e,i,o,u))
    return #None




# Challenge – CS Circles/Recursion
def countdownBy2(n):
    '''(number) -> None

    This function has one parameter that is a number and the function
    returns no value(None).
    The function counts down from n and prints 'Blastoff', but counts
    down by 2.
    
    >>> countdownBy2(7)
    7
    5
    3
    1
    Blastoff!
    '''
    if n == 0 or n == -1:
        print('Blastoff!')
    else:
        print(n)
        countdownBy2(n - 2)
    return #None


    
        

    
    

































