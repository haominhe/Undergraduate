"""
Tactics and checks for Sudoku.

Authors: Haomin He
Consulted with: Office Hour, Rickie Kerndt, Daniel Bach. 

A tactic is a rule that can be used to determine and/or constrain the
possible choices for a Sudoku tile.

A check determines whether a given Sudoku board
(whether complete or incomplete) is legal.  A board is
legal if it contains only digits and open spaces, and
if all of the digits are unique in each row, column,
and 3x3 block.
"""
import sdkboard

# The following variables are private but global to the module
global groups
global progress

def prepare(board):
    """ 
    Prepare for checking and solving a sudoku board.
    Args:
       board:  An sdkboard.Board object
    Returns:
       nothing
    Effects:
       prepared for check(board) and solve(board)
    """
    global groups  # rows, columns, and blocks

    groups = [ ]

    # Rows  (we can reuse them from the board)
    for row in range(9):
        groups.append(board.tiles[row])
    
    for column in range(9): #9 groups for the 9 columns,column loop should not be nested inside row loop
        new_empty_list = []
        for row in range(9):
            new_empty_list.append(board.tiles[row][column])
        groups.append(new_empty_list)
        
    for start_row in [0, 3, 6]:
        for start_col in [0, 3, 6]:
            sq_tiles = [ ] 
            for row in range(3):
                for col in range(3): 
                    t = board.tiles[start_row + row][start_col+col]
                    sq_tiles.append(t)
            groups.append(sq_tiles)

    # We need to know when we are making progress 
    for row in board.tiles:
        for tile in row:
            tile.register(progress_listener)


 
def progress_listener(tile, event):
    """
    An event listener, used to determine whether we have made
    some progress in solving a Sudoku puzzle.  This listener
    will be attached to Sudoku Tile objects, and informed when
    "determined" and "constrained" events occur.
    Args:
       tile:  The tile on which an event occurred
       event: What happened.  The events we listen for are "determined"
         and "constrained"
    Returns:  nothing
    Effects: module-global variable progress may be set to True
    """
    global progress 
    if event == "determined" or event == "constrained":
       progress = True
       # print("Notified of progress!")

def good_board(): 
        """Check that every group (row, column, and block)
        contains unique elements (no duplicate digits).
        Args:
           none  (implicit through prepare_board)
        Returns:
           Boolean True iff all groups contain unique elements
        Effects:
           Will announce "duplicate" event on tiles that are
           not unique in a group.
        Requires:
           prepare(board) must be called before good_board
        """
        Flag = True # whether the board is "ok so far" here
        for everyelement in groups:
            dups = set()     # reset every time
            available = set(sdkboard.SYMBOLS) # SYMBOLS = frozenset('.123456789')
            for tile in everyelement:
                if (tile.symbol in available):
                    if tile.symbol != sdkboard.OPEN:
                        available.remove(tile.symbol)
                else:                         # (tile.symbol not in available)
                    dups.add(tile.symbol)
                    Flag = False
            for tile in everyelement:
                for dup in dups:
                    if tile.symbol == dup:
                        tile.announce("duplicate")              
        return Flag
def solve():
    """
    Keep applying naked_single and hidden_single tactics to every
    group (row, column, and block) as long as there is progress.
    Args: 
        none
    Requires:
        prepare(board) must be called once before solve()
        use only if good_board() returns True
    Effects: 
        May modify tiles in the board passed to prepare(board), 
        setting symbols in open tiles, and reducing the possible
        sets in some tiles. 
    """
    global progress
    progress = True
    while(progress):
        # print("***Starting solution round***")
        progress = False
        # Note that naked_single and hidden_single may indirectly
        # set the progress flag by causing the progress listener to be
        # triggered.  
        for group in groups:
            naked_single(group)
            hidden_single(group)

def naked_single(group):
        """Constrain each tile to not contain any of the digits 
        that have already been used in the group.
        Args: 
            group: a list of 9 tiles in a row, column, or block
        Returns:
            nothing
        Effects:
            For each tile in the group, eliminates "possible" elements
            that match a digit used by another tile in the group.  If 
            this reduces it to one possibility, the selection will be 
            made (Tile.remove_choices does this), and progress may be 
            signaled.
        """
        chosen_num = set()
        for tile in group:
            if (tile.symbol != sdkboard.OPEN):
                chosen_num.add(tile.symbol)
        for tile in group: 
            if tile.symbol == sdkboard.OPEN:
                tile.remove_choices(chosen_num) # remove used symbols from "possible"
        return
        
        
def hidden_single(group):
        """Each digit has to go somewhere.  For each digit, 
        see if there is only one place that digit should 
        go.  If there is, put it there. 
        Args: 
           group:  a list of 9 tiles in a row, column, or block
        Returns: 
           nothing
        Effects: 
           For each tile, if it is the only tile that can accept a 
           particular digit (according to its "possible" set), 
           
        """ 
        used = set(sdkboard.DIGITS)
        for tile in group:
            if tile.symbol in used:
                used.remove(tile.symbol) # left available digits
        for symbol in used:
            last_tile = None
            counter = 0
            for tile in group: # count how many tiles can take it
                if tile.symbol == sdkboard.OPEN:
                    if symbol in tile.possible:
                        counter += 1
                        last_tile = tile # remembering the last tile that can take it
            if counter == 1:
                last_tile.determine(symbol)
        return
'''
solve(board):
   """Returns True if the board is solvable, 
      False if the board is not solvable. 
      If it returns True, it also leaves the 
      completed board in global variable Solution.
   """
   if board is already complete and consistent: 
        save board to Solution
        return True
   elif board is inconsistent (that is, good_board() returns False):
        return False
   else:
        # The guess-and-check step
        pick some tile that is OPEN
        prior = current state of board
        for digit in DIGITS:
            tile.symbol = digit
            if solve(board):
               return True
        board = prior
        return False'''
        
