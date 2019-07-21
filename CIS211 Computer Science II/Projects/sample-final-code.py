"""
CIS 211 Winter 2015
Sample Final Code
Haomin He
"""


from tkinter import *


class Element:
    def __init__(self, n, atom_wt=None):
        "Initialization: n is an element number from the periodic table"
        self._id = n
        self._wt = atom_wt

    names = ['Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron', 'Ununoctium']
    symbols = ['H', 'He', 'Li', 'Be', 'B', 'Uuo']

    def __repr__(self):
        return Element.symbols[self._id-1]

    def symbol(self):
        return Element.symbols[self._id-1]

    def id(self):
        return self._id

    def name(self):
        return Element.names[self._id - 1]

    def weight(self):
        if self._wt != None:
            return self._wt
        else:
            return "Not Given."

    last = 118



class NobleGas(Element):
    def __init__(self, n, wt = None):
        if n in [2,10,18,36,54,86,118]:
            Element.__init__(self, n, wt)
        else:
            raise Exception("not a noble gas")


class ElementFrame(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.pack()


        self._name = Label(self, text="")
        self._name.grid(row=0, column=1)
        self._symbol = Label(self, text="")
        self._symbol.grid(row=1, column=1)

        
        self._next = Button(self, text='next', command=self.next_element)
        self._next.grid(row=2, column=1, pady=20)

        self.set_element(Element(1))

        self.reset = Button(self, text = 'Reset', command=self.reset_cb)
        self.reset.grid(row=2, column=2, pady=20)

    def set_element(self, e):
        self._element = e
        print(self._element)
        self._name.configure(text = e.name())
        self._symbol.configure(text = e.symbol())
        
    
    def next_element(self):
        if self._element.id() < Element.last:
            self.set_element(Element(self._element.id() + 1))

    def reset_cb(self):
        self.set_element(Element(1))






if __name__ == "__main__":
    h = Element(1)
    e = [ Element(i) for i in [1,3,5] ]
    #print(e)
    h.name()

    g = NobleGas(2)
    #print(g)
    #c = NobleGas(6)
    #print(c)

##    root = Tk()
##    a = ElementFrame(root)
##    root.mainloop()

    from functools import reduce
    from operator import mul, add

    x = ['zucchini', 'onion', 'garlic', 'tomato', 'olive oil']
    def first(s): return s[0]
    def compound(s): return s.find(' ') != -1

##    print(list(map(len, x)))
##    print(".".join(list(map(first, x))))
##    print(list(filter(compound, x)))
##    print(reduce(mul, range(1,6)))
    
    line = ['less', 'than', '100', 'calories', 'and', '10', 'grams', 'of', 'fat', '??']







