"""CIS 211 Winter 2015
   Haomin He 
   Project 4: Building GUIs with Tk

   3. Write a program that will display three playing card images and a button
   labeled "flip". Each time the user clicks the button one of the card images
   should be updated.

   When the window is first opened the user should see the backs of three cards.
   The first button click should turn over the first card, and the next two
   clicks should turn over the other two cards. 

   When you display the front of a card you can pick any card at random.
    
   The fourth click should appear to remove a card, but in fact your program
   should change the image to a white square the size of a card. The next two
   clicks will remove the other two cards.

   The next three clicks should appear to “deal” three new cards face down.
   Your program just needs to replace the blank images with the image for the
   back side of a card.
   
"""

from tkinter import *
from random import randint
from CardLabel import *

root = Tk()
CardLabel.load_images()
sides = ['back', 'front', 'blank']# values that can be passed to display method
n = 0           # index into list of sides

a = [CardLabel(root), CardLabel(root), CardLabel(root)]
for i in range(3):
    a[i].grid(row = 0, column = i)
    

def flip():
    global n
    x = (n+3) // 3
    if x == 3:
        x = 0
    a[n%3].display(sides[x], randint(0,51))
    print(n, n%3, (n+3)//3)
    n = (n+1) % 9 #9 events
            
root.rowconfigure(0, minsize=115)
root.columnconfigure(0, minsize=85)

button = Button(root, text='Flip', width = 10, command = flip)
button.grid(row = 1, column = 1, pady = 10, rowspan = 1)

if __name__ == '__main__':
    root.mainloop()




















    
