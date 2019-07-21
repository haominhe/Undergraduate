from turtle import *

# Problem 0
#(0a)
def square(length):
    '''(number) -> [drawing of a square]

    This function is to draw a square, using turtle movement
    commands. Function square have one parameter, length,
    which is the length of the sides of the square.
    Square will not return any value.

    >>> square(100)
    >>> square(200)

    '''
    fd(length)
    lt(90)

    fd(length)
    lt(90)

    fd(length)
    lt(90)

    fd(length)
    lt(90)

    return #None


#(0b)
def square(length,scolor):
    '''(number,string) -> [drawing of an scolored-colored square]

    This function is to draw an scolored-colored square,
    using turtle movement commands. Function square have two
    parameter, length, which is the length of the sides of
    the square, and scolor, which is the color of the square.
    Square will not return any value.

    >>> square(100,"red")
    >>> square(200,"cyan")

    '''
    color(scolor)
    begin_fill()
    penup()
    
    fd(length)
    lt(90)

    fd(length)
    lt(90)

    fd(length)
    lt(90)

    fd(length)
    lt(90)
    
    pendown()
    end_fill()

    return #None


#(0c)
def triangle(length,tcolor):
    '''(number,string) -> [drawing of a tcolor-colored triangle]

    This function has two parameters, length and tcolor,
    which will draw a tcolor-colored triangle when called.
    Triangle will not return any value.

    >>> triangle(100, “orange”)
    >>> triangle(150, “purple”)

    '''
    color(tcolor)
    begin_fill()
    penup()
    
    fd(length)
    lt(120)

    fd(length)
    lt(120)

    fd(length)
    lt(120)
    
    end_fill()

    return #None


#(0d)
def house():
    '''() -> [drawing of a square house with a door and a roof]

    The house body, door, and roof should be drawn by calling functions
    you have already defined. The house function definition will not
    have any parameters and will not return a value.

    >>> house()

    '''
    title("House")
    
    square(200,"cyan")
    square(100,"pink")

    setpos(0,200)
    triangle(200,"purple")
    
    return #None


# Problem 1
def art_show():
    '''() -> [drawing of beautiful houses and a red sun]

    This function will not have any parameters and
    art_show does not return a value.

    >>> art_show()

    '''

    title("Three Colorful Houses and a Red Sun")
    
    square(200,"yellow")
    square(100,"magenta")

    setpos(0,200)
    triangle(200,"maroon")

    setpos(300,0)
    
    square(200,"violet")
    square(100,"brown")

    setpos(300,200)
    triangle(200,"purple")

    setpos(-300,0)
    
    square(200,"blue")
    square(100,"green")

    setpos(-300,200)
    triangle(200,"orange")

    setpos(-400,265)

    color('yellow', 'red')
    begin_fill()
    circle(127)
    end_fill()
    
    return #None


# Problem 2
from random import randint

def mars_explore_main():
    '''() -> None
    
    main function for mars_explore:
    set up print and graphical output
    then call mars_explore repeatedly
    data is printed; no value is returned

    >>> mars_explore_main()
    xpos 	 ypos 	 water 	 temp
    92 275 152 -54
    140 28 31 -172
    142 -263 234 -124
    170 154 264 -42
    227 218 111 -97
    '''

    #  label  for  print  output
    print("xpos",  "\t",
          "ypos",  "\t",
          "water",  "\t",
          "temp")                      
    #  set  up  graphical  output
    reset()
    title("Mars  Rover")
    display_color  =  "blue"
    color(display_color)
    square(10,display_color) #draw the rover

    #  explore  five places  on  Mars

    mars_explore()
    mars_explore()
    mars_explore()
    mars_explore()
    mars_explore()

    return  #None

#(2a)
def rover_loc():
    '''() -> int

    The rover_loc function returns a
    random integer between -275 and 275,
    for rover location.

    >>> rover_loc()
    22
    >>> rover_loc()
    -144
    >>> rover_loc()
    99

    '''
    return randint(-275,275)



def water_content():
    '''() -> int

    There are no parameters.
    The water_content function should return
    a random integer between 1 and 290 (ppm).

    >>> water_content()
    277
    >>> water_content()
    77
    >>> water_content()
    174

    '''
    return randint(1,290)


def temp():
    '''() -> int

    There are no parameters.
    The temp function should return a random
    integer between -178 and 1 (degrees Fahrenheit).

    >>> temp()
    -106
    >>> temp()
    -42
    >>> temp()
    -8

    '''
    return randint(-178,1)

#(2b)
def mars_explore():
    '''() -> [print the x and y coordinates of the
              rover, and the data for the water content
              and temperature at this location.]

    Function mars_explore has no parameters
    and does not return a value.

    >>> mars_explore()
    -30 -122 163 -9
    >>> mars_explore()
    174 -79 93 -110

    '''
    #Determine the next location for exploration.
    x = rover_loc()
    y = rover_loc()
    
    #Move the rover to the new location and mark thez
    #position. Show the rover's path.
    goto(x,y)
    stamp()
    dot()

    #Collect data at this location. 
    water = water_content()
    temperature = temp()

    #Dispaly the data.
    print(x,y,water,temperature)

    return #None


# Challenge
def mars_explore_write():
    '''() -> [print the x and y coordinates of the
              rover, and the data for the water content
              and temperature at this location.]

    This funciton has no parameters and does not return
    a value.

    >>> mars_explore_write()
    (-22, -118, 69, -88)
    (-30, 120, 113, -55)
    (126, 146, 37, -94)
    (211, -12, 134, -45)
    (67, 47, 213, -54)

    '''
    reset()
    title("Mars  Rover with Data")
    
    stamp()
    dot()
    water1 = water_content()
    temperature1 = temp()
    a = rover_loc()
    b = rover_loc()
    goto(a,b)
    position1 = (a,b,water1,temperature1)
    write(position1, font=('Arial', 18, 'normal'))

    stamp()
    dot()
    water2 = water_content()
    temperature2 = temp()
    c = rover_loc()
    d = rover_loc()
    goto(c,d)
    position2 = (c,d,water2,temperature2)
    write(position2, font=('Arial', 18, 'normal'))

    stamp()
    dot()
    water3 = water_content()
    temperature3 = temp()
    e = rover_loc()
    f = rover_loc()
    goto(e,f)
    position3 = (e,f,water3,temperature3)
    write(position3, font=('Arial', 18, 'normal'))

    stamp()
    dot()
    water4 = water_content()
    temperature4 = temp()
    g = rover_loc()
    h = rover_loc()
    goto(g,h)
    position4 = (g,h,water4,temperature4)
    write(position4, font=('Arial', 18, 'normal'))

    stamp()
    dot()
    water5 = water_content()
    temperature5 = temp()
    i = rover_loc()
    j = rover_loc()
    goto(i,j)
    position5 = (i,j,water5,temperature5)
    write(position5, font=('Arial', 18, 'normal'))

    print(position1)
    print(position2)
    print(position3)
    print(position4)
    print(position5)

    return #None


































