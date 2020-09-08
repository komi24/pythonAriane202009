#!/usr/bin/env python
# coding: utf-8

# ## Dichotomie
# 
# * Ecrire un programme qui vous permet de deviner un nombre
# mystère qu'il génère aléatoirement
# 
# * Ecrire un programme qui trouve un nombre 
# mystère (entre 0 et 100) que vous avez en tête
# 
# 

# In[1]:


from random import randint

nb_mystere = randint(0,100)
proposition = -1

while proposition != nb_mystere:
    proposition = int(input("Devinez le nombre mystère :"))
    if proposition < nb_mystere:
        print("Proposition trop petite")
    elif proposition > nb_mystere:
        print("Propostion trop grande")
    else:
        print("Vous avez gagné !!")


# In[1]:


borne_min = 0
borne_max = 101

proposition = (borne_min + borne_max ) // 2
reponse = None

while reponse != "=":
    reponse = input(f"Est-ce que le nombre est {proposition} ? +/-/=")
    if reponse == "+":
        borne_min = proposition
    elif reponse == "-":
        borne_max = proposition
    
    proposition = (borne_min + borne_max ) // 2
    
print("Gagné !!")


# In[1]:


i = 10
while i > 0:
    print(i)
    if i % 2 == 0:
        print("pair")
        i -= 1
        continue
    print("fin du bloc")
    i -= 1
    


# In[2]:


i = 10
while i > 0:
    print(i)
    if i % 2 == 0:
        print("pair")
        i -= 1
        break
    print("fin du bloc")
    i -= 1
    


# In[3]:


a = [ 1,2,3,4,[5,6]]
b = a
b[0] = 6
print(a)


# In[4]:


a = [ 1,2,3,4,[5,6]]
b = list(a)
b[0] = 6
print(a)


# In[5]:


a = [ 1,2,3,4,[5,6]]
b = list(a)
b[-1][0] = 16
print(a)


# In[8]:


def print_values(liste):
    for i in liste:
        print(i)

print_values(a)


# In[11]:


def print_values_and_change_it(liste):
    for i in liste:
        print(i)
    liste[0] *= 2

print_values_and_change_it(a)
print(a)


# In[16]:


def print_values(liste):
    assert type(liste) == list, "First argument must be a list"
    print("bonjour")
    for i in liste:
        print(i)

try:
    print_values(4)
except:
    print("Il y a eu une erreur")
finally:
    print("execute")
print("fin")


# ## Tri bulle
# 
# 

# In[ ]:


def tri_bulle(a):
    

