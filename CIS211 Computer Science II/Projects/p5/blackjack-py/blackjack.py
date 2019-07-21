"""CIS 211
   Project 5: Blackjack    Winter 2015
   Haomin He

   This program will play a game of Blackjack. The top level window should have
   room for two rows of cards, with six cards in each row. Below the cards
   display three buttons, named "deal", "hit", and "pass".

   I have also tried Extra Credit Ideas.
"""

from tkinter import *
from CardLabel import *
from Card import *
from Deck import *
from tkinter.messagebox import showinfo
import time

    

class BlackjackGame(BlackjackCard):
    def __init__(self):
        """This init contains two rows of cards, with six cards in each row.
           Below the cards display three buttons, named "deal", "hit", and "pass".
        """
        
        self.root = Tk()

        self.deal = Button(self.root, text='Deal', width = 10, command = self.dealf)
        self.deal.grid(row = 2, column = 0, pady = 10, rowspan = 2)

        self.hit = Button(self.root, text='Hit', width = 10, command = self.hitf)
        self.hit.grid(row = 2, column = 2, pady = 10, rowspan = 2, columnspan = 2)

        self.gamepass = Button(self.root, text='Pass', width = 10, command = self.gamepassf)
        self.gamepass.grid(row = 2, column = 5, pady = 10, rowspan = 2)

        CardLabel.load_images()     # call after creating top level application
        self.house = [CardLabel(self.root) for i in range(6)]
        self.player = [CardLabel(self.root) for i in range(6)]

        housecol = 0
        for each in self.house:
            each.grid(row = 0, column = housecol)
            each.display(side = 'blank')
            housecol += 1

        playercol = 0
        for every in self.player:
            every.grid(row = 1, column = playercol)
            every.display(side = 'blank')
            playercol += 1
  
        self.trackwins = Label(self.root, text = "Player Wins: {}".format(BlackjackGame.pwins))
        self.trackwins.grid(row = 4, column = 0)
        
        self.trackloses = Label(self.root, text = "Player Loses: {}".format(BlackjackGame.ploses))
        self.trackloses.grid(row = 4, column = 3)

        """Allow the player to specify an account balance and an amount they want to bet,
           and update the balance after every game."""
        Label(self.root, text = "Account Balance: ").grid(row = 5, column = 0)
        self.amt = Entry(self.root, text = "100")
        self.amt.grid(row = 5, column = 1)

        Label(self.root, text = "Bet Amount: ").grid(row = 5, column = 3)
        self.betamt = Entry(self.root)
        self.betamt.grid(row = 5, column = 4)
        
        self.root.rowconfigure(0, minsize=115)
        self.root.columnconfigure(0, minsize=85)
        self.root.mainloop()

    pwins = 0
    ploses = 0
    

    def dealf(self):
        """The deal button should start a new game. Shuffle a deck of cards, then
           display two cards for the dealer in the top row, with one card face down,
           and display two cards for the player, both face up, in the bottom row. The
           remaining four places in each row should be blank cards.
        """
        
        self.hit.configure(state = "normal")
        self.gamepass.configure(state = "normal")
               
        self.gamedeck = Deck()
        self.gamedeck.shuffle()
        
        self.housedeal = self.gamedeck.deal(2)
        self.playerdeal = self.gamedeck.deal(2)

        self.house[0].display('back', self.housedeal[0]._id)
        self.house[1].display('front', self.housedeal[1]._id)

        self.player[0].display('front', self.playerdeal[0]._id)
        self.player[1].display('front', self.playerdeal[1]._id)

        for i in range(2, 6):
            self.player[i].display('blank', 0)
            self.house[i].display('blank', 0)
        
        BlackjackGame.counter1 = 1
        BlackjackGame.counter2 = 1

        """ Check to see if either player has “blackjack” (a total of 21 using
         only two cards), and if so, display the game results right away,
         without waiting for the hit or pass button (a blackjack always beats
         any other kind of hand)."""
        BlackjackGame.total(self)
        if self.playerpoints == 21:
            self.house[0].display('front', self.housedeal[0]._id)
            showinfo("Game Over!", "Player has the blackjack!")
            BlackjackGame.pwins += 1

            self.Amt = int(self.amt.get())
            self.Bet = int(self.betamt.get())
            self.Amt += self.Bet * 2
            self.amt.delete(0, END)
            self.amt.insert(0, self.Amt)
            
            self.gamepass.configure(state = "disable")
            self.hit.configure(state = "disable")
            self.restartprogram()

        if self.dealerpoints == 21:
            self.house[0].display('front', self.housedeal[0]._id)
            showinfo('Game Over!', "Dealer has the blackjack!")
            BlackjackGame.ploses += 1

            self.Amt = int(self.amt.get())
            self.Bet = int(self.betamt.get())
            self.Amt -= self.Bet
            self.amt.delete(0, END)
            self.amt.insert(0, self.Amt)

            self.gamepass.configure(state = "disable")
            self.hit.configure(state = "disable")
            self.restartprogram()
            
        

    counter1 = 1
    def hitf(self):
        """The hit button should turn over the next card in the bottom row, and it
           should update the player’s score using a function named total (described
           below). If the score is over 21 the player loses the game, and your program
           should display an alert box with a consoling message.
        """
        
        BlackjackGame.total(self)
        
        if self.playerpoints > 21:
            self.house[0].display('front', self.housedeal[0]._id)
            showinfo("Game Over!", "Player loses the game!")
            BlackjackGame.ploses += 1

            self.Amt = int(self.amt.get())
            self.Bet = int(self.betamt.get())
            self.Amt -= self.Bet
            self.amt.delete(0, END)
            self.amt.insert(0, self.Amt)
            
            self.gamepass.configure(state = "disable")
            self.hit.configure(state = "disable")
            self.restartprogram()
            
        elif len(self.playerdeal) < 6:
            self.playerdeal += self.gamedeck.deal(1)
            self.player[BlackjackGame.counter1 + 1].display('front', self.playerdeal[BlackjackGame.counter1 + 1]._id)
            BlackjackGame.counter1 += 1
        

            """In some casinos, the dealer or the player wins if they have 5 cards that total 21 or
            less, no matter what the other player’s total is (unless the other person has a
            blackjack)."""
        elif len(self.playerdeal) == 5 and self.playerpoints <= 21:
            self.house[0].display('front', self.housedeal[0]._id)
            showinfo("Game Over!", "Player wins!")
            BlackjackGame.pwins += 1

            self.Amt = int(self.amt.get())
            self.Bet = int(self.betamt.get())
            self.Amt += self.Bet * 2
            self.amt.delete(0, END)
            self.amt.insert(0, self.Amt)

            self.gamepass.configure(state = "disable")
            self.hit.configure(state = "disable")
            self.restartprogram()
               
        else:
            self.hit.configure(state = "disabled")
            

    counter2 = 1
    def gamepassf(self):
        """If the user clicks the pass button, turn over the dealer’s hidden card
           and compute the total points for the cards in the dealer’s row. Then while
           the dealer’s total score is less than 17 turn over a the next card in the
           dealer’s hand and add the points for that card to the dealer’s total. When
           the dealer’s total is 17 or higher compare the dealer’t total with the
           player’s total and display a message that shows the result of the game
           (dealer wins, player wins, or tie game).
        """
        
        BlackjackGame.total(self)
        time.sleep(0.5)
        self.house[0].display('front', self.housedeal[0]._id)

        while self.dealerpoints < 17:
            self.housedeal += self.gamedeck.deal(1)
            """ When showing the dealer’s cards have the program pause for
             ½ second between each card."""
            time.sleep(0.5)
            self.house[BlackjackGame.counter2 + 1].display('front', self.housedeal[BlackjackGame.counter2 + 1]._id)
            BlackjackGame.counter2 += 1
            BlackjackGame.total(self)

            if len(self.housedeal) == 5 and self.dealerpoints <= 21:
                self.house[0].display('front', self.housedeal[0]._id)
                showinfo("Game Over!", "Dealer wins!")
                BlackjackGame.pwins += 1

                self.Amt = int(self.amt.get())
                self.Bet = int(self.betamt.get())
                self.Amt -= self.Bet
                self.amt.delete(0, END)
                self.amt.insert(0, self.Amt)

                self.gamepass.configure(state = "disable")
                self.hit.configure(state = "disable")
                self.restartprogram()

        if (self.dealerpoints > self.playerpoints and self.dealerpoints <= 21) or self.playerpoints > 21:
            showinfo('Game Over!', "Dealer wins!")
            BlackjackGame.ploses += 1

            self.Amt = int(self.amt.get())
            self.Bet = int(self.betamt.get())
            self.Amt -= self.Bet
            self.amt.delete(0, END)
            self.amt.insert(0, self.Amt)
            
        elif self.dealerpoints < self.playerpoints or self.dealerpoints > 21:
            showinfo("Game Over!", "Player wins!")
            BlackjackGame.pwins += 1

            self.Amt = int(self.amt.get())
            self.Bet = int(self.betamt.get())
            self.Amt += self.Bet * 2
            self.amt.delete(0, END)
            self.amt.insert(0, self.Amt)
            
        else:
            showinfo("Game Over!", "Its a tie game!")
            
        self.gamepass.configure(state = "disable")
        self.hit.configure(state = "disable")
        self.restartprogram()


    def total(self):
        """The idea is to use a loop that computes an initial total, using 11
           points for each ace and counting the number of aces in the hand. Then
           a second loop changes aces to 1 point if necessary: while the number
           of aces is greater than 0 and the total is greater than 21 subtract 10
           from the total and subtract one from the ace counter.
        """
        self.playerpoints = 0 
        Ace = 0
        
        for each in self.playerdeal:
                self.playerpoints += BlackjackCard(each._id).points()
                if BlackjackCard(each._id).rank() == 12:
                    Ace += 1
        while self.playerpoints > 21 and Ace > 0:
                self.playerpoints -= 10
                Ace -= 1
                
        self.dealerpoints = 0
        Ace = 0
        for every in self.housedeal:
                self.dealerpoints += BlackjackCard(every._id).points()
                if BlackjackCard(every._id).rank() == 12:
                        Ace += 1
        while self.dealerpoints > 21 and Ace > 0:
                self.dealerpoints -= 10
                Ace -= 1


    def restartprogram(self):
        """Restarts the current game.
           This program keeps track of the number of games the player wins
           and loses, and display the current total in the window.
        """
        for i in range(0, 6):
            self.player[i].display('blank', 0)
            self.house[i].display('blank', 0)
            
        BlackjackGame.counter1=1
        BlackjackGame.counter2=1

        self.trackwins.config(text = "Player Wins: {}".format(BlackjackGame.pwins))
        self.trackloses.config(text = "Player Loses: {}".format(BlackjackGame.ploses))


def histogram():
    """Create a histogram with 10 bins, labeled 1 through 10, all initially set to 0. Then
        deal a series of hands, keeping track of how many cards you need to deal before
        the total is 22 or higher. For each hand update the bin that corresponds to the
        number of cards dealt; for example, if a hand reaches 25 on the 3rd card add one to
        the count in bin 3. If you repeat this process several million times you will start to
        get a pretty good idea of the shape of the probability distribution."""
    
    tenbins = { x:0 for x in range(10)}

    for i in range(1000):
        bindeck = Deck()
        bindeck.shuffle()
        hand = []
        handpoints = 0
        Ace = 0

        while handpoints < 21:
            hand += bindeck.deal(1)
            handpoints += BlackjackCard(hand[-1]._id).points()
            if BlackjackCard(hand[-1]._id).rank() == 12:
                Ace += 1
                
            
        while handpoints > 21 and Ace > 0:
            handpoints -= 10
            Ace -= 1
            
        tenbins[len(hand)] += 1
        
    print(tenbins)
        


if __name__ == '__main__':
    BlackjackGame()
    histogram()

















    
