"""CIS 211 Winter 2015
   Haomin He 
   Project 4: Building GUIs with Tk

   1. Write a simple "hello, world" program that displays a text message in a
   window. The program will terminate when the user closes the window.

   I also tried Extra Credit Ideas.

   Play around with different sizes, shapes, colors, and fonts in your “hello,
   world” program. Add a quit button. Add buttons with the names of different
   languages so that when the user clicks a button the message changes to
   “hello” in that language. This might be a good chance to play with Unicode,
   both in the message text and in the string displayed on a button.
"""
from tkinter import *

root = Tk()

def quitbutton():
    root.destroy()
    print("Have a wonderful day\u0021")

def english():
    hello.config(text = "Hello, world\u26BD")

def french():
    hello.config(text = "Bonjour tout le monde\u2600")

def chinese():
    hello.config(text = "你好,世界\u263A")

def dutch():
    hello.config(text = "Hallo, wereld\u2665")

def russian():
    hello.config(text = "Привет, мир\u2614")

hello = Label(master = root,
              height = 5,
              width = 20,
              fg = "pink",
              bg = "teal",
              font = ("Helvetica", 18),
              anchor = CENTER,
              justify = CENTER,
              relief = RAISED,
              underline = 0,
              compound = CENTER,
              padx = 16,
              pady = 6,
              text = "hello, world")
hello.grid(row = 0, columnspan = 6)


quitB = Button(root, text = "Quit\u26C5", width = 20, command = quitbutton)
quitB.grid(row = 3, columnspan = 6)

helloE = Button(root, text = "English\u26F3", command = english)
helloE.grid(row = 2, column = 0)

helloF = Button(root, text = "French\u26EA", command = french)
helloF.grid(row = 2, column = 1)

helloC = Button(root, text = "Chinese\u26F2", command = chinese)
helloC.grid(row = 2, column = 3)

helloD = Button(root, text = "Dutch\u264F", command = dutch)
helloD.grid(row = 2, column = 4)

helloR = Button(root, text = "Russian\u26F5", command = russian)
helloR.grid(row = 2, column = 5)

if __name__ == "__main__":
    root.mainloop()















    
