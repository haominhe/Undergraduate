"""
Boggle solver finds words on a boggle board. 
Authors:  Haomin He
Credits:  Office Hour 

Usage:  python3 boggler.py  "board" dict.txt
    where "board" is 16 characters of board, in left-to-right reading order
    and dict.txt can be any file containing a list of words in alphabetical order
    
"""

from boggle_board import BoggleBoard   
import argparse   # Command line processing
import game_dict  # Dictionary of legal game words

def main():
    """
    Main program: 
    Find all words of length 3 or greater on a boggle 
    board. 
    Args:
        none (but expect two arguments on command line)
    Returns: 
        Nothing (but prints found words in alphabetical
        order, without duplicates, one word per line)
    """
    dict_file, board_text = getargs()
    game_dict.read( dict_file )
    board = BoggleBoard(board_text)
    results = [ ]
    
    for row in range(4):
        for col in range(4):
            find_words(board, row, col, "", results)
    #Search for words starting from each position on the board.
    
    final = dedup(results)
    counter = 0
    for i in final:
        print(i, score(i))  # Print each word and its score
        counter += score(i)
    print("Total score: ", counter) # Print total score    
    
def dedup(resultslist):  # Remove duplicates
    """
    This function is for putting a results list into
    sorted order, without duplicate words.
    Args:
       resultslist: a list with duplicate words
    Returns:
       a sorted list without duplicate words
    """
    s = set(resultslist)
    l = list(s)
    l.sort()      # sort alphabetically
    return l 
    
def getargs():
    """
    Get command line arguments.
    Args:
       none (but expects two arguments on program command line)
    Returns:
       pair (dictfile, text)
         where dictfile is a file containing dictionary words (the words boggler will look for)
         and   text is 16 characters of text that form a board
    Effects:
       also prints meaningful error messages when the command line does not have the right arguments
   """
    parser = argparse.ArgumentParser(description="Find boggle words")
    parser.add_argument('board', type=str, help="A 16 character string to represent 4 rows of 4 letters. Q represents QU.")
    parser.add_argument('dict', type=argparse.FileType('r'),
                        help="A text file containing dictionary words, one word per line.")
    args = parser.parse_args()  # will get arguments from command line and validate them
    text = args.board
    dictfile = args.dict
    if len(text) != 16 :
        print("Board text must be exactly 16 alphabetic characters")
        exit(1)
    return dictfile, text

def find_words(board, row, col, prefix, results):
    """Find all words starting with prefix that
    can be completed from row,col of board.
    Args:
        row:  row of position to continue from (need not be on board)
        col:  col of position to continue from (need not be on board)
        prefix: looking for words that start with this prefix
        results: list of words found so far
    Returns: nothing
        (side effect is filling results list)
    Effects:
        inserts found words (not necessarily unique) into results
    """
    if not board.available(row, col):
        return       # check row, col availability, off the board or currently in use
    singlechar = board.get_char(row,col)
    prefix = prefix + singlechar  # new prefix
    
    match = game_dict.search(prefix)
    if match == game_dict.NO_MATCH:
        return  # no word can start with the current prefix, no use searching further on that path
	
    if match == game_dict.WORD:
        results.append(prefix) # a complete word might also be part of a longer word
        
    board.mark_taken(row, col) # mark possible prefix as currently in use
    find_words(board, row + 1, col, prefix, results) # search in all 8 directions around the mark
    find_words(board, row - 1, col, prefix, results)
    find_words(board, row + 1, col + 1, prefix, results)
    find_words(board, row - 1, col + 1, prefix, results)
    find_words(board, row, col + 1, prefix, results)
    find_words(board, row, col - 1, prefix, results)
    find_words(board, row + 1, col - 1, prefix, results)
    find_words(board, row - 1, col - 1, prefix, results)
    board.unmark_taken(row, col) # unmark: no longer in use
    
    return
   
def score(word):
    """
    Compute the Boggle score for a word, based on the scoring table
    at http://en.wikipedia.org/wiki/Boggle. 
    Args:
        word: a word read from boggle
    Returns:
        according to the word length to determine the score
        Word    Points
        Length
        3,4	1
        5	2
        6	3
        7	5
        8+      11
     """
    if len(word) >= 8:
        return 11
    if len(word) == 7:
        return 5
    if len(word) == 6:
        return 3
    if len(word) == 5:
        return 2   
    return 1

####
# Run if invoked from command line
####

if __name__ == "__main__":
    main()
    input("Press enter to end")

