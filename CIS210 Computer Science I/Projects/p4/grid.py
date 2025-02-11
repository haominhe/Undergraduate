"""
Grid display for class projects.

Author: Michal Young (michal@uoregon.edu) for CIS 210

Displays a rectangular grid of cells, organized in rows and columns
with row 0 at the top and growing down, column 0 at the left and 
growing to the right.  A sequence of unique colors for cells can 
be chosen from a color wheel, in addition to colors 'black' and 'white'
which do not appear in the color wheel. 

Uses the simple graphics module provided by Zelle, which in turn 
is built on the Tk graphics package (and which should therefore be 
available on all major Python platforms, including Linux, Mac, and 
all flavors of Windows at least back to XP). 
"""

from graphics import *    # Zelle's simple OO graphics

global win  # The window we are drawing the grid in
global cell_width, cell_height  # The size of a cell in the grid

global color_wheel
color_wheel = [  color_rgb(255,0,0), color_rgb(0,255,0), color_rgb(0,0,255),
                        color_rgb(255,255,0), color_rgb(255,0,255), color_rgb(0,255,255),
                        color_rgb(127,255,0), color_rgb(0,127,255), color_rgb(127,0,255),
                        color_rgb(255,127,0), color_rgb(0,255,127), color_rgb(255,0,127),
                        color_rgb(127,127,0), color_rgb(127,0,127), color_rgb(0,127,127),
                        color_rgb(255,255,127), color_rgb(255,127,255), color_rgb(127,255,255) ]
global cur_color
cur_color = 0
global black
black = color_rgb(0,0,0)
global white
white = color_rgb(255,255,255)
global nrows
nrows = 1

def make( rows, cols, width, height ) :
    """Create the grid display, initially all white.
    rows, cols are the grid size in rows and columns.
    width, height are the window size in pixels.
    
    Args: 
        rows:  number of rows of cells in the grid (vertical divisions)
        cols:  number of columns of cells in the grid (horizontal divisions)
        width:  horizontal width of window in pixels
        height: vertical height of window in pixels
    Returns:  nothing
    """
    global win, cell_width, cell_height, nrows
    win = GraphWin("Grid", width, height )
    win.setCoords(0, 0, cols, rows)
    bkgrnd = Rectangle( Point(0,0), Point(width,height) )
    bkgrnd.setFill( color_rgb(255,255,255) ) # White background
    cell_width = width / cols
    cell_height = height / rows
    nrows = rows 

def get_cur_color():
    """Return the currently chosen color in the color wheel.  
    
    The color wheel is a list of colors selected to be contrast with each other. 
    The first few entries are bright primary colors; as we cycle through the color
    wheel, contrast becomes less, but colors should remain distinct to those with 
    normal color vision until the color wheel cycles all the way around in 18 
    choices and starts recycling previously used colors.   The color wheel starts
    out in position 0, so get_cur_color() may be called before get_next_color() has 
    been called. 
    
    Args:  none
    Returns:  
        a 'color' that can be passed to fill_cell
        
    FIXME: The color wheel should produce colors of contrasting brightness
    as well as hue, to maximize distinctness for dichromats (people with 
    "color blindness".  Maybe generating a good color wheel can be part of a 
    project later in CIS 210.   (This is not a required or expected change 
    for the week 4 project.) 
    """
    return color_wheel[cur_color]

def get_next_color():
    """Advance the color wheel, returning the next available color. 
    
    The color wheel is a list of colors selected to be contrast with each other. 
    The first few entries are bright primary colors; as we cycle through the color
    wheel, contrast becomes less, but colors should remain distinct to those with 
    normal color vision until the color wheel cycles all the way around in 18 
    choices and starts recycling previously used colors. 
    
    Args:  none
    Returns:  
        a 'color' that can be passed to fill_cell    
    """
    global cur_color
    cur_color += 1
    if cur_color >= len(color_wheel) :
        cur_color = 0
    return color_wheel[cur_color]

def fill_cell(row, col, color):
    """Fill cell[row,col] with color.
    
    Args: 
        row:  which row the selected cell is in.  Row 0 is the top row, 
           row 1 is the next row down, etc.  Row should be between 0 
           and one less than the number of rows in the grid. 
        col:  which column the selected cell is in.  Column 0 is 
           the leftmost row, column 1 is the next row to the right, etc. 
           Col should be between 0 and one less than the number of columns
           in the grid. 
        color: What color to fill fill the selecte cell with.  Valid colors
           include grid.white, grid.black, and values returned by 
           grid.get_next_color() and grid.get_cur_color()

    """
    global nrows, win
    left = col
    right = col + 1
    top = nrows - (row + 1)
    bottom = nrows - row
    mark = Rectangle( Point(left,bottom), Point(right,top) )
    mark.setFill(color)
    mark.draw(win)

    

