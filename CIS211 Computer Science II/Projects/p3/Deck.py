"""Project 3: Decks   CIS 211  2015 Winter
   Haomin He

   This project defines a new class that extends one of Python’s
   built-in types, we also explore random number generators.

   This code has two definitions: a class named Deck and a class
   named PinochleDeck.

   I also have tried the Extra Credit Ideas.
"""

from sys import argv
from Card import *
import random

class Deck(list):
    """This class should be derived from Python’s list class. An
       instance of this class will be a list of 52 Card objects
       (which are defined in Card.py).
    """

    def __init__(self):
        """When the constructor is called it should return a list of all
           52 cards in order from 2♣ up through A♠.
        """
        list.__init__(self, [Card(i) for i in range(52)])


    def shuffle(self):
        """This function should rearrange the cards into a new
           random permutation
           Write my own version of a method that makes a random
           permutation instead of using random.shuffle
        """
        _shuffledlist = []
        for every in range(len(self)):
            pick = random.choice(self)
            self.remove(pick)
            _shuffledlist.append(pick)

        self.extend(_shuffledlist)
            
        return None


    def deal(self, n, optionalPlayer = None):
        """This function should remove the first n cards from the deck
           and return them in a list
           Add a second (optional) argument to the deal method that specifies
           the number of hands to create. For example, deal(5,2) will make 2
           hands with 5 cards each, where the cards are dealt in the traditional
           fashion, i.e. alternate cards to each hand.
        """
        if optionalPlayer == None:
            self._firstNcards = self[0:n]
            del self[0:n]
            return self._firstNcards
        elif optionalPlayer != None:
            total_cardsnum = n * optionalPlayer
            self._firstNcards = self[0:total_cardsnum]
            del self[0:total_cardsnum]

            hands = [[] for player in range(optionalPlayer)]
            i = -1
            for eachcard in range(n):
                for h in hands:
                    i += 1
                    h.append(self._firstNcards[i])
            return hands
            


    def restore(self, a):
        """This function should add the cards in list a to the end
           of the deck
           This function verify its argument is a list of Card objects
        """
        flag = True
        for i in range(len(a)):
            if type(a[i]) != Card:
                flag = False

        if flag == True:
            self.extend(a)
        else:
            Deck.not_implemented()

    
    @staticmethod
    def not_implemented():
        """This function prevents users from altering the decks with 
	   list methods like append.
	"""
        raise Exception("operation not implemented") 

    def append(self, val):  Deck.not_implemented()
    def insert(self, loc, val):  Deck.not_implemented()



class PinochleDeck(Deck):
    """This class has Deck as its base class. An instance of this class
       should be a list of 48 cards. The game of Pinochle uses only 9s
       and above, and there are two copies of each card. A new deck should
       be sorted.
    """

    def __init__(self):
        """When the constructor is called it should return a list of 
           48 cards.
        """
        Deck.__init__(self)
        _PDlist = []
        for each in self:
            if (each._rank >= 7):
                _PDlist.append(each)
                _PDlist.append(each)
        _PDlist.sort()
        list.__init__(self, _PDlist)
    
    


if __name__ == "__main__":
    d = Deck()
    print("should be 52 ----> {}".format(len(d)))
    print("should be <class 'Card.Card'> ----> {}".format(type(d[0])))
    print("should be [2♣, 3♣, 4♣, ... Q♠, K♠, A♠] ----> {}".format(d))
    d.shuffle()
    print("should be random 52 cards ----> {}".format(d))
    h = d.deal(5)
    print("should be first 5 cards ----> {}".format(h))
    print("should be random 47 cards ----> {}".format(d))
    print("should be 47 ----> {}".format(len(d)))
    d.restore(h)
    print("cards should be added at the end ----> {}".format(d))
    print("should be 52 ----> {}".format(len(d)))
    d.sort()
    print("should be [2♣, 3♣, 4♣, ... Q♠, K♠, A♠] ----> {}".format(d))

    print("=================================================================")
    
    d = PinochleDeck()
    print("should be [9♣, 9♣, 10♣, 10♣, ... Q♠, Q♠, K♠, K♠, A♠, A♠] ----> {}".format(d))
    d.shuffle()
    h = d.deal(12)
    h.sort()
    print("12 random cards should be in ordered: ♣, ♦, ♥, ♠ ----> {}".format(h))

    print("=================================================================")
    
    d = Deck()
    print("should be [2♣, 3♣, 4♣, ... Q♠, K♠, A♠] ----> {}".format(d))

    try:
        d.append('howdy')
        print("after appending 'howdy' to the Deck:", d)
    except Exception as e:
        print("should have error message ----> {}".format(e))
    
    print("should be 52 ----> {}".format(len(d)))
    d.shuffle()
    print("should have no appended string in it ----> {}".format(d))

    

















