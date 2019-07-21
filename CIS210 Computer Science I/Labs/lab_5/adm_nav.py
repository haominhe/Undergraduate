#
# adm_nav.py
#
# Program to generate an ADM route file based on a floor plan, starting coordinates, and
# ending coordinates

import sys

# Markers used for the initial map
WALL='#'
OPEN='.'

# A number bigger than the longest possible path; effectively infinity
MAXI=2**24

def readMap(filename):
    """Returns a 2D list representing the floor plan in the file named filename"""
    map=list()
    mapfile=open(filename)
    for line in mapfile:
        line=line.strip()
        map.append(list(line))
    return map

def readLoc(map,x,y):
    """Returns the symbol to location x,y in the 2D list map
       Locations outside of the map are reported as walls
    """
    if y<0 or y>=len(map) or x<0 or x>=len(map[0]):
    	return WALL
    return map[y][x]

def setLoc(map,x,y,sym):
    """Sets the symbol at location x,y in the 2D list map to sym
       Locations outside of the map are not recorded
    """
    if y<0 or y>=len(map) or x<0 or x>=len(map[0]):
    	return
    map[y][x]=sym

def printMap(map):
    """Prints the map to the terminal"""
    for y in range(len(map)):
        for x in range(len(map[0])):
            print(readLoc(map,x,y),end='')
        print('')

def printRoute(map,adm_x,adm_y,route):
    """Marks a map with the given route and then prints the map"""
    for item in route:
        setLoc(map,adm_x,adm_y,'@')
        if item=='N':
            adm_y=adm_y-1
        if item=='S':
            adm_y=adm_y+1
        if item=='W':
            adm_x=adm_x-1
        if item=='E':
            adm_x=adm_x+1
    setLoc(map,adm_x,adm_y,'@')
    printMap(map)

def writeRoute(outfile,route):
    """Takes a list of steps in route and writes them to the file named outfile, one
       step per line
    """
    out=open(outfile,"w")
    out.write('\n'.join(route))

def lenPath(path):
    """Returns the length of path

       If there is not a path, the path length is infinite
       Otherwise, the length of the paths is returned
    """
    if path is None:
        return MAXI
    return len(path)

def minPath(a,b,c,d):
	"""Returns the shortest path from the set a, b, c, d"""

	r=a
	if lenPath(b)<lenPath(r):
	    r=b
	if lenPath(c)<lenPath(r):
	    r=c
	if lenPath(d)<lenPath(r):
	    r=d
	return r


def getRoute(map,step,adm_x,adm_y,alien_x,alien_y):
    """Returns a list of moves to reach alien_x,alien_y from adm_x,adm_y or None if there
       isn't a viable path.

       map - a two dimensional array representing a floor plan
       step - number of steps from the starting square
       adm_x,adm_y - the ADM coordinates
       alien_x,alien_y - the alien coordinates

       Returns a minimum path, represented by a list/string of steps, or None
    """

    # read the marker for the current location
    sym=readLoc(map,adm_x,adm_y)

    # Can't ever move through walls
    if sym==WALL:
        return None

    # If the ADM is at the alien's coordinates, then no moves are needed
    if adm_x==alien_x and adm_y==alien_y:
        return ''
    
    if sym != OPEN:
        if step > int(sym):  # step > already taken
            return None
        
    setLoc(map,adm_x,adm_y,step)  # Store the number of steps taken in map
        
    # increment the step counter before taking the next step
    step=step+1
    
    up_path = getRoute(map,step + 1, adm_x, adm_y-1,alien_x,alien_y)
    down_path = getRoute(map,step + 1, adm_x, adm_y+1,alien_x,alien_y)
    left_path = getRoute(map,step + 1, adm_x-1, adm_y,alien_x,alien_y)
    right_path = getRoute(map,step + 1, adm_x+1, adm_y,alien_x,alien_y) # if zpos is open
    
    if up_path is not None:
        up_path = 'N' + up_path
    if down_path is not None:
        down_path = 'S' + down_path
    if left_path is not None:
        left_path = 'W' + left_path
    if right_path is not None:
        right_path = 'E' + right_path
    return minPath(up_path,down_path,left_path,right_path)


def main():
    """Reads a map file and prints a message when there is a way to get from the start
       coordinates to the target coordinates.

       You don't need to make any changes to the main function this week."""

    #check the args, abort if their aren't enough
    if len(sys.argv) != 7:
        print("Usage: python3 "+sys.argv[0]+" <filename.map> <ADM x> <ADM y> <alien x> <alien y> <out.route>")
        exit(1)

    # covert from sys.argv list to easier names
    mapfile=sys.argv[1]
    admx=int(sys.argv[2])
    admy=int(sys.argv[3])
    alnx=int(sys.argv[4])
    alny=int(sys.argv[5])
    outfile=sys.argv[6]

    # Read the map file
    map=readMap(mapfile)

    # Use the recursive function to complete the search
    route=getRoute(map,0,admx,admy,alnx,alny)

    map=readMap(mapfile)
    setLoc(map,alnx,alny,'T')
    printRoute(map,admx,admy,route)

    # Print the correct message to the user based on the search results
    if route==None:
        print("***************************************************")
        print("* !!! DANGER - ADM can't reach alien - DANGER !!! *")
        print("***************************************************")
    else:
        writeRoute(outfile,route)
        print("Route has been saved in: "+sys.argv[6])

if __name__=="__main__":
    main()
