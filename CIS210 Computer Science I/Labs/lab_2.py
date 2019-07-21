import argparse

"""
    shoutLetters1 - prints all characters within a phrase separated by
    by a space

    e.g. "Go Ducks!" -> "G O  D U C K S !"
"""

def shoutLetters1(phrase):

    phrase = phrase.upper() # really shout out loud

    print("#",end="")
    for letter in phrase[:-1]:
        print(letter," ", sep="",end="")
    print(phrase[-1],end="")
    
    print("#") #new line

"""
    shoutLetters2 - prints all characters within words of a phrase
    separated by a hypen. Whitespace and punctuation are not printed
    with a hypen separator.

    e.g. "Go Ducks!" -> "G-O D-U-C-K-S!"
"""

def shoutLetters2(phrase):

    phrase = phrase.upper() # really shout out loud

    skiphypen = False
    print("#",end="")

    print(phrase[0], end="")
    for letter in phrase[1:]:
        if skiphypen:
            print(letter, end="")
            skiphypen = False
            
        elif letter.isalnum():  # returns true if all
                                # characters in the string
                                # are alphanumeric
                                # whether it is a number or a letter,
                                # it will return True
                                # but return False if it has a space.etc.
            print('-',letter, sep="",end="")
        else:
            print(letter, end="")
            skiphypen = True     #state variable
    
    print("#") #new line

    

    

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Shout Letters")
    parser.add_argument("phrase", type=str, help="Enter a phrase to shout")
    args = parser.parse_args()

    #shoutLetters1(args.phrase)
    shoutLetters2(args.phrase)

















