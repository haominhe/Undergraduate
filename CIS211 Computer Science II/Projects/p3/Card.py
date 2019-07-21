
# Card.py, the second programming project for CIS 211 (WQ 2015)

# [Haomin He]

# [overview of the project：]
"""This program has three definitions: a class named Card,
   a class named BlackjackCard, a function named total,
   and a function named new_deck. At the end of the file
   include the 'magic incantation.

   I also tried Extra Credit Ideas.
"""

from sys import argv

class Card:
    """
    [description: Card object. Each instance of the class
     will be a single playing card.]
    """

    def __init__(self, *args):
        """This constructor takes an integer id between
        0 and 51 to specify which card to make.
        Card 0 to 12 are clubs, 13 to 25 diamonds,
        26 to 38 hearts, and 39 to 51 spades
        """
        self._singlestr = None
        self._twostr = None
        self._rank = None
        if len(args) == 1 and isinstance(args[0], int):
            if not (0 <= args[0] <= 51):
                raise Exception("The integer should between 0 and 51")
            self._id = args[0]
            self._suit, self._rank = divmod(self._id, 13)
            
        elif len(args) == 1 and isinstance(args[0], str):
            self._singlestr = args[0] # allow users to pass a single string

        else:
            self._twostr = args[0] + args[1]
        # Users can pass a specified rank and suit to the Card constructor
        

    syms = {0: '\u2663', 1: '\u2666', 2: '\u2665', 3:  '\u2660'}
         # Clubs, Diamonds, Hearts, Spades

    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J',
             'Q', 'K', 'A']
        
    def __repr__(self):
        """the representation of a card is a 2-letter string
        """
        if self._rank != None:
            ranknum = Card.ranks[self.rank()]
            suitnum = Card.syms[self.suit()]
            return ranknum + suitnum
        if self._singlestr != None:
            return self._singlestr
        if self._twostr != None:
            return self._twostr
        
    def __lt__(self, other):
        """cards are compared according to their ids
        """
        return self._id < other._id

    def rank(self):
        """This function returns a number between 0 and 12, where
           2s have rank 0 and aces have rank 12.
        """
        return self._rank

    def suit(self):
        """This function should return the suit number, with
           clubs = 0, diamonds = 1, hearts = 2, and spades = 3
        """
        return self._suit

    def points(self):
        """This function should return 4 if the card is an ace,
           3 if it’s a king, 2 if it’s a queen, 1 if it’s a jack,
           and 0 otherwise
        """
        if self._rank != None:
            if Card.ranks[self._rank] == 'A':
                return 4
            elif Card.ranks[self._rank] == 'K':
                return 3
            elif Card.ranks[self._rank] == 'Q':
                return 2
            elif Card.ranks[self._rank] == 'J':
                return 1
            else:
                return 0
        elif self._singlestr != None:
            if self._singlestr[0] == 'A':
                return 4
            elif self._singlestr[0] == 'K':
                return 3
            elif self._singlestr[0] == 'Q':
                return 2
            elif self._singlestr[0] == 'J':
                return 1
            else:
                return 0
        elif self._twostr != None:
            if self._twostr[0] == 'A':
                return 4
            elif self._twostr[0] == 'K':
                return 3
            elif self._twostr[0] == 'Q':
                return 2
            elif self._twostr[0] == 'J':
                return 1
            else:
                return 0
                
        
class BlackjackCard(Card):
    """
    [description: BlackjackCard object. This class uses Card
     as its base class. Overload the points method]
    """
    
    def points(self):
        """Aces have 11 points, face cards (J, Q, K) have 10
           points, and other cards have their natural value
           (10, 9, 8, etc down to 2).
        """
        if self._rank != None:
            if Card.ranks[self._rank] == 'A':
                return 11
            elif (Card.ranks[self._rank] == 'J' or
                  Card.ranks[self._rank] == 'Q' or
                  Card.ranks[self._rank] == 'K'):
                return 10
            else:
                return int(Card.ranks[self._rank])
            
        elif self._singlestr != None:
            if self._singlestr[0] == 'A':
                return 11
            elif (self._singlestr[0] == 'J' or
                  self._singlestr[0] == 'Q' or
                  self._singlestr[0] == 'K'):
                return 10
            else:
                return int(self._singlestr[0])
            
        elif self._twostr != None:
            if self._twostr[0] == 'A':
                return 11
            elif (self._twostr[0] == 'J' or
                  self._twostr[0] == 'Q' or
                  self._twostr[0] == 'K'):
                return 10
            else:
                return int(self._twostr[0])

    def __lt__(self, other):
        """cards are compared according to their points
        """
        return self.points() < other.points()
              
        
def total(h):
    """
    [description: This is a top-level function named total that
     will take a list of cards and return the sum of the point
     values of the cards.]
    """
    sumpt = 0
    for each in h:
        sumpt += each.points()
    return sumpt


def new_deck(cardtype = None):
    """This function will create a list of cards of a specified type.
       The argument should be the name of the class that specifies
       which type of card to make (if no argument is passed make a
       list of standard cards)
    """
    deck = [ Card(i) for i in range(52) ]
    blackjack_deck = [ BlackjackCard(i) for i in range(52) ]
    
    if cardtype == Card:
        return deck
    elif cardtype == BlackjackCard:
        return blackjack_deck
    else:
        return deck
    
    
        

if __name__ == '__main__':
    x = Card(35)
    print(x)
    print(x.suit())
    print(x.rank())
    print(x.points())

    y = BlackjackCard(38)
    print(y)
    print(y.points())

    z = BlackjackCard(39)
    print(z)
    print(z.points())
    print(y < z)

    deck = [ Card(i) for i in range(52) ]
    blackjack_deck = [ BlackjackCard(i) for i in range(52) ]
    from random import sample
    hand = sample(deck, 5)
    print(hand)
    print(total(hand))

    bj_hand = sample(blackjack_deck,3)
    print(bj_hand)
    print(total(bj_hand))

    print(new_deck(Card))
    print(new_deck(BlackjackCard))
    print(new_deck())

    print(Card('A','\u2660'))
    print(Card('A♠'))
    
    print(Card(56))
