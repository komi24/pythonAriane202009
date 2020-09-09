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


# In[30]:


from tkinter import *
from itertools import product


fen = Tk()

label = Label(fen, text="Salut")
label.pack()

frame_ops = Frame(fen)
frame_ops.pack(side=RIGHT)

frame_button = Frame(fen)
frame_button.pack()

for (i,j) in product(range(3), range(3)):
    button1 = Button(frame_button, text=str(3*(2-i)+j+1), width=8, height=4)
    button1.grid(row=i, column=j)

for op in ["+","-","*","/"]:
    button1 = Button(frame_ops, text=op, width=8, height=4)
    button1.pack()

button1 = Button(fen, text="0", width=8, height=4)
button1.pack(side=BOTTOM, fill=BOTH)

fen.mainloop()


# In[ ]:




