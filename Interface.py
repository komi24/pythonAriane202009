#!/usr/bin/env python
# coding: utf-8

# In[9]:


from tkinter import *

fen = Tk()

label = Label(fen, text="Salut")
label.pack()

button1 = Button(fen, text="Bouton 1")
button1.pack(side=RIGHT)

button2 = Button(fen, text="Bouton 2")
button2.pack(side=BOTTOM)

button3 = Button(fen, text="Bouton 3")
button3.pack(side=BOTTOM)

fen.mainloop()


# In[12]:


from tkinter import *

fen = Tk()

button1 = Button(fen, text="Bouton 1")
button1.grid(row=0, column=0)

button2 = Button(fen, text="Bouton 2")
button2.grid(row=1, column=0)

button3 = Button(fen, text="Bouton 3")
button3.grid(row=0, column=1)

fen.mainloop()


# In[14]:


from tkinter import *

fen = Tk()

label = Label(fen, text="Salut")
label.pack()

frame_button = Frame(fen)
frame_button.pack()


button1 = Button(frame_button, text="Bouton 1")
button1.grid(row=0, column=0)

button2 = Button(frame_button, text="Bouton 2")
button2.grid(row=1, column=0)

button3 = Button(frame_button, text="Bouton 3")
button3.grid(row=0, column=1)

fen.mainloop()


# In[40]:


from tkinter import *
from itertools import product

class MonBouton(Button):
    def __init__(self, root, value, width=8, height=4):
        Button.__init__(self, root, text=str(value), width=width, height=height)
        self.value = value

fen = Tk()

chaine = StringVar()
chaine.set("0")

def print_hello(evt):
    chaine.set("1")
    print(evt.widget.value)


label = Label(fen, textvariable=chaine, height=4)
label.pack()

frame_ops = Frame(fen)
frame_ops.pack(side=RIGHT)

frame_button = Frame(fen)
frame_button.pack()

for (i,j) in product(range(3), range(3)):
    button1 = MonBouton(frame_button, value=3*(2-i)+j+1, width=8, height=4)
    button1.bind("<Button-1>", print_hello)
    button1.grid(row=i, column=j)

for op in ["+","-","*","/"]:
    button1 = Button(frame_ops, text=op, width=8, height=4)
    button1.pack()

button1 = MonBouton(fen, value=0, width=8, height=4)
button1.pack(side=BOTTOM, fill=BOTH)

fen.mainloop()


# In[47]:


from tkinter import *
from itertools import product

class MonBouton(Button):
    def __init__(self, root, value, width=8, height=4):
        Button.__init__(self, root, text=str(value), width=width, height=height)
        self.value = value

class CalculatriceUI:
    def __init__(self):
        self.fen = Tk()
        self.displayed_value = StringVar()

        self.label = Label(self.fen,
                           textvariable=self.displayed_value,
                           height=4)
        self.label.pack()

        self.frame_ops = Frame(self.fen)
        self.frame_ops.pack(side=RIGHT)

        self.frame_button = Frame(self.fen)
        self.frame_button.pack()

        for (i,j) in product(range(3), range(3)):
            button1 = MonBouton(self.frame_button, value=3*(2-i)+j+1)
            button1.bind("<Button-1>", self.num_button_pressed)
            button1.grid(row=i, column=j)

        for op in ["+","-","*","/"]:
            button1 = Button(self.frame_ops, text=op, width=8, height=4)
            button1.pack()

        button1 = MonBouton(self.fen, value=0)
        button1.pack(side=BOTTOM, fill=BOTH)

    def start(self):
        self.fen.mainloop()
        
    def op_button_pressed(self, evt):
        pass
    def num_button_pressed(self, evt):
        pass
    def process(self, evt):
        pass


# In[48]:


calc = CalculatriceUI()


# In[49]:


calc.start()


# In[50]:


class Calculatrice(CalculatriceUI):
    def __init__(self):
        """
        Initialize Calc UI
        """
        CalculatriceUI.__init__(self)
        self.total = 0
        self.value = 0
    
    def op_button_pressed(self, evt):
        pass
    
    def num_button_pressed(self, evt):
        print(evt.widget.value)
    
    def process(self, evt):
        pass
    
calc = Calculatrice()
calc.start()
# class OpButton(Button):
#     pass


# class NumButton(Button):
#     pass


# In[ ]:




