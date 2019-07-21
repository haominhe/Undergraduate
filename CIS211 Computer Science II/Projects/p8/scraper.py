"""CIS 211 Winter 2015
Project 8: Scanning HTML Documents

Part 2:
This program extracts final scores from an HTML file containing the results
of basketball games. It will use the HTMLParser class.

Define a class named Scraper that inherits from HTMLParser. The parser should
create a list of games, where each game is a list that will eventually have
two team names and two scores.
"""

from sys import argv
from html.parser import HTMLParser
from urllib.request import urlopen

text = urlopen(argv[1]).read().decode()

class Scraper(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self._grab_this = False
        self._lsgames = []    # constructor should initialize the game list
                              # to be an empty list
        self.game = None # instance variable, initialize to None
                              

    def handle_starttag(self, tag, attrs):
        """This method adds a new empty list to the end of the game list
           whenever it sees a table tag that has the attribute class=”linescore”.
           If a tag is 'a' with '/schools/' in attribute or a td with attribute
           class=”final score” raise a flag so the next data item is appended to
           the current game (a “flag” is just a boolean variable that is True
           with the flag is up and False when the flag is down).

           In handle_starttag, set self.game to the empty list when the the tag is
           'table' and the attributes are "class='linescore'", also in handle_starttag,
           raise the flag only if self.game is not None
        """
        if tag == 'table' and attrs == [('class','linescore')]:
            self.game = [] 
            
        if (tag == 'a' and '/schools/' in attrs[0][1]) and self.game != None:
            self._grab_this = True
            
        elif (tag == 'td' and attrs == [('class','final score')]) and self.game != None:
            self._grab_this = True

        
    def handle_data(self, text):
        """This method checks to see if the flag is up. If so, it should append
           the data to the current game (because it will be either a team name
           or a score) and lower the flag.
           Append the text to self.game if self.game is not None and the flag is up.
        """
        if self._grab_this and self.game != None:
            self.game.append(text.strip())
            self._grab_this = False


    def handle_endtag(self, tag):
        """If the tag is 'table' and self.game is not None the contents of
           self.game (which should now be a list with 4 items) is appended to
           the game list, and set self.game to None again.
        """
        if tag == 'table' and self.game != None:
            self._lsgames.append(self.game)
            self.game = None
            



if __name__ == "__main__":
    parser = Scraper()
    parser.feed(text)
    for each in parser._lsgames:
        print("{} {}, {} {}".format(each[0], each[1], each[2], each[3]))

    
    
















        
