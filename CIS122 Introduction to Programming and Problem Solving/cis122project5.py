
# Problem 0 Grade Calculator
def grade_calculator():
    '''() -> None

    Prompt user to input a list of grades;
    Adjust grades to correct weight;
    Prints total grade as percent and letter.

    For example,
    grade_calculator()
    Enter project 1 grade: 12
    Enter project 2 grade: 58
    Enter project 3 grade: 44
    Enter project 4 grade: 60
    Enter midterm 1 grade: 34
    88.4 B
    
    '''
    proj_so_far = 16    #4 projects, 4 weighted pts. each
    tests_so_far = 20   #1 midterm 20 pts. weighted
    ttl_points_possible = \
                        proj_so_far + tests_so_far
 
    p1_adjust = 3  # 12 ttl pts, divide by 3 to get 4
    p2_adjust = 16 # 64 ttl pts, divide by 16 to get 4
    p3_adjust = 12 # 48 ttl pts, divide by 12 to get 4
    p4_adjust = 17 # 68 ttl pts, divide by 17 to get 4
    m1_adjust = 2  # 40 ttl pts, divide by 2 to get 20

    # initialize weighted totals
    proj_grade = 0
    exam_grade = 0

    p1 = int(input('Enter project 1 grade: '))
    p1 = p1 / p1_adjust
    proj_grade += p1

    p2 = int(input('Enter project 2 grade: '))
    p2 = p2 / p2_adjust
    proj_grade += p2

    p3 = int(input('Enter project 3 grade: '))
    p3 = p3 / p3_adjust
    proj_grade += p3

    p4 = int(input('Enter project 4 grade: '))
    p4 = p4 / p4_adjust
    proj_grade += p4

    m1 = int(input('Enter midterm 1 grade: '))
    m1 = m1 / m1_adjust
    exam_grade += m1

    my_ttl = proj_grade + exam_grade
    my_score = my_ttl / ttl_points_possible * 100
    my_score = round(my_score, 1)
    print(my_score, end=' ')
  
    if my_score >= 90:
        print('A')
    elif 80 <= my_score < 90:
        print('B')
    elif 70 <= my_score < 80:
        print('C')
    elif 60 <= my_score < 70:
        print('D')
    else:
        print('F')
    
    return #None


# Problem 1 Payday
def payday(hourly_wage,hours):
    '''(int,int) -> int

    This function has two parameters, hourly_wage and hours.
    The function should compute and return the pay.
    For the first 40 hours worked, pay is at the input hourly
    wage. Any hours over forty but less than or equal to 60
    are paid at 1 and 1⁄2 times the regular hourly wage. Any hours
    over sixty are paid at 2 times the regular hourly wage.

    >>> payday(10,35)
    350
    >>> payday(10,45)
    475
    >>> payday(10,61)
    720
    >>> payday(0,0)
    0
    '''
    if hours <= 40:
        return hours * hourly_wage
    elif 40 < hours <= 60:
        hours = hours - 40
        return int(40 * hourly_wage + hours * hourly_wage * 1.5 )
    else:
        hours = hours - 60
        return int((40 * hourly_wage) + (20 * hourly_wage * 1.5) + (hours * hourly_wage * 2 ))

    

# Problem 2 Rock, Paper, Scissors
def rps():
    '''() -> None

    This function takes no parameter and returns none.
    This function asks two players in turn for their input
    choices ('r', 'p', or 's') and prints out which player
    wins and the reason for the win.
    Rock, paper, scissors is a two-player game in which
    each player chooses one of three items (rock, paper,
    or scissors). If both players choose the same item, the
    game is tied. Otherwise, Rock crushes/wins over Scissors,
    Scissors cuts/wins over Paper, and Paper covers/wins
    over Rock.

    >>> rps()
    Welcome to Rock, Paper, Scissors!
    First player, enter 'r', 'p', or 's':r
    Second player, enter 'r', 'p', or 's':s
    r beats s - player 1 wins

    '''
    print('Welcome to Rock, Paper, Scissors!')
    firstplayer = input("First player, enter 'r', 'p', or 's':")
    secondplayer = input("Second player, enter 'r', 'p', or 's':")
    
    if firstplayer == secondplayer == 'r':
        print('The game is tied')
    elif firstplayer == secondplayer == 'p':
        print('The game is tied')
    elif firstplayer == secondplayer == 's':
        print('The game is tied')
    elif firstplayer == 'r' and secondplayer == 's':
        print('r beats s - player 1 wins')
    elif firstplayer == 's' and secondplayer == 'p':
        print('s beats p - player 1 wins')
    elif firstplayer == 'p' and secondplayer == 'r':
        print('p beats r - player 1 wins')
    elif secondplayer == 'r' and firstplayer == 's':
        print('r beats s - player 2 wins')
    elif secondplayer == 's' and firstplayer == 'p':
        print('s beats p - player 2 wins')
    elif secondplayer == 'p' and firstplayer == 'r':
        print('p beats r - player 2 wins')
    else:
        print('Please chooses one of three items (rock, paper, or scissors).')

    return #None



# Problem 3 Better R, P, S
def better_rps():
    '''() -> None

    This fuction can take both uppercase and lowercase of
    'R' or 'P' or 'S' for the Rock, Paper, Scissors game. 
    This function takes no parameter and returns none.
    This function asks two players in turn for their input
    choices ('r', 'p', or 's' and 'R' or 'P' or 'S') and
    prints out which player wins and the reason for the win.
    Rock, paper, scissors is a two-player game in which
    each player chooses one of three items (rock, paper,
    or scissors). If both players choose the same item, the
    game is tied. Otherwise, Rock crushes/wins over Scissors,
    Scissors cuts/wins over Paper, and Paper covers/wins
    over Rock.

    >>> better_rps()
    Welcome to Rock, Paper, Scissors!
    First player, enter 'r', 'p', or 's':P
    Second player, enter 'r', 'p', or 's':S
    s beats p - player 2 wins

    '''
    print('Welcome to Rock, Paper, Scissors!')
    firstplayer = str(input("First player, enter 'r', 'p', or 's':"))
    secondplayer = str(input("Second player, enter 'r', 'p', or 's':"))
    firstplayer = str.lower(firstplayer)
    secondplayer = str.lower(secondplayer)

    
    if firstplayer == secondplayer == 'r':
        print('The game is tied')
    elif firstplayer == secondplayer == 'p':
        print('The game is tied')
    elif firstplayer == secondplayer == 's':
        print('The game is tied')
    elif firstplayer == 'r' and secondplayer == 's':
        print('r beats s - player 1 wins')
    elif firstplayer == 's' and secondplayer == 'p':
        print('s beats p - player 1 wins')
    elif firstplayer == 'p' and secondplayer == 'r':
        print('p beats r - player 1 wins')
    elif secondplayer == 'r' and firstplayer == 's':
        print('r beats s - player 2 wins')
    elif secondplayer == 's' and firstplayer == 'p':
        print('s beats p - player 2 wins')
    elif secondplayer == 'p' and firstplayer == 'r':
        print('p beats r - player 2 wins')
    else:
        print('Please chooses one of three items (rock, paper, or scissors).')

    return #None



# Problem 4 Population Density Analysis
def density_rpt(population,land_area):
    '''(int,int) -> int

    This function has two parameters, population and land_area.
    The function should print the land density (number of people
    per unit of area). If the land density is greater than 100,
    the function should print "Densely populated" and "Sparsely
    populated" otherwise.

    # Oregon
    >>> density_rpt(3899000,98381)
    Land density is 40 per square mile.
    Area is sparsely populated
    # Washington
    >>> density_rpt(6897000,71300)
    Land density is 97 per square mile.
    Area is sparsely populated
    # Idaho
    >>> density_rpt(1596000,83570)
    Land density is 19 per square mile.
    Area is sparsely populated
    # California
    >>> density_rpt(38040000,163695)
    Land density is 232 per square mile.
    Area is densely populated    
    '''
    land_density = round(population / land_area)
    print('Land density is', land_density ,'per square mile.')
    
    if land_density > 100:
        print('Area is densely populated')
    else:
        print('Area is sparsely populated')



# Problem 5 As Time Goes By
def minstohour(mins):
    '''(int) -> float

    This function has one parameter, mins. It returns hour
    after calculation. (60 minutes per hour.)

    >>> minstohour(60)
    1.0
    >>> minstohour(120)
    2.0
    '''
    hour = round(mins / 60, 2)
    return hour

def hourtoday(hour):
    '''(int) -> float

    This function has one parameter, hour. It returns day
    after calculation. (24 hours per day)

    >>> hourtoday(24)
    1.0
    >>> hourtoday(36)
    1.5
    >>> hourtoday(48)
    2.0
    
    '''
    day = round(hour / 24,2)
    return day

def daytoyear(day):
    '''(int) -> float

    This function has one parameter, day. It returns year
    after calculation. (365 days per year)

    >>> daytoyear(365)
    1.0
    >>> daytoyear(730)
    2.0    
    '''
    year = round(day / 365,2)
    return year

def minutesToYears(minsconverted):
    '''(int) -> float

    This function has one parameter, the number of minutes to be
    converted. The function should convert the input value to the
    corresponding number of years, and return the number of years
    value. (minutes to hours, hours to days, days to years). All
    functions should return a value rounded to two decimal points. 

    >> minutesToYears(525600)
    1.0
    >>> minutesToYears(5256000)
    10.0
    >>> minutesToYears(394200)
    0.75
    >>> minutesToYears(0)
    0.0
    '''

    hour = minstohour(minsconverted)
    day = hourtoday(hour)
    year = daytoyear(day)

    return year

    

# Challenge
def make_chocolate(small,big,goal):
    '''(int,int,int) -> number

    This function has three parameters, small, big, and goal. We want
    make a package of goal kilos of chocolate, from the available small
    and big bars of chocolate. The small bars are 1 kilo each and the
    big bars are 5 kilos each. Big bars cannot be divided; they must be
    used all at once. Return the number of small bars to use, assuming
    we always use big bars before small bars. Return -1 if it can't be
    done.

    >>> make_chocolate(4,1,9)
    4
    >>> make_chocolate(4,1,10)
    -1
    >>> make_chocolate(4,1,7)
    2
    >>> make_chocolate(3,1,9)
    -1
    >>> make_chocolate(6,2,10)
    0.0

    '''
    maxBig = goal / 5
   
    if big >= maxBig:
        if small >= (goal - maxBig * 5):
            return goal - maxBig * 5
    if big < maxBig:
        if small >= (goal - big * 5):
            return goal - big * 5
    return -1
        






































































