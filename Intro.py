#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Hello tout le monde")


# ## Titre
# 
# #### Sous titre
# 
# Paragraphe d'introduction
# 
# * Premier
# * Deuxieme

# In[3]:


print(a)


# In[2]:


a = 2


# In[8]:


ma_variable = 2
print(ma_variable)
print(type(ma_variable))

# ma_variable = "bonjour"

# print(ma_variable)
# print(type(ma_variable))


# In[11]:


2 + "bonjour"


# In[10]:


print(b)


# In[12]:


a = 2
b = 2.04
c = (1 + 1j)**2
print(c)
d = True 
e = False
print(type(d))
f = None


# In[15]:


print( 8 / 5) # Sur python 3 donne un float. Sur python 2 donne un entier


# In[16]:


print( 8 // 5)


# In[19]:


print( True or False )
print( True and False )
print(d or e)


# In[20]:


# Nom de classe en CamelCase ex: UneClasse
# Nom des variables snake_case ex: ma_varaibel, ma_fonction
# PEP8 pour les conventions de coding stlye

A = 4
a = 2 
a == A


# In[21]:


2 | 4


# In[23]:


2 & 6


# In[38]:


import numpy as np
# numpy est la librairie de calcul matriciel

matrice_a = np.ones((4,4))
matrice_a[2,2]


# In[30]:


ma_chaine = "Bonjour tout le monde"

print(ma_chaine)
print(ma_chaine[0])
print(ma_chaine[1])
print(ma_chaine[-1])


# In[31]:


a = "bonjour"
print("a")
print(a)


# In[34]:


# Existe uniquement dans python 3

nom = "Dupont"
prenom = "Xavier"

print("Bonjour " + nom + " " + prenom)
print(f"Bonjour {nom} {prenom}")


# In[44]:


ma_liste = [2, True, "Bonjour", 10, [15, 4]]
ma_liste[-1][-1]
print(2 in ma_liste)
print(11 in ma_liste)


# In[46]:


nom = "prenom"
mon_dico = {"nom": "Dupont", "prenom": "Laurent"}
print(mon_dico["nom"])
print(mon_dico[nom])
print("dupont" in mon_dico)
print("nom" in mon_dico)


# In[48]:


len(ma_liste)

1 == True


# In[60]:


print(ma_liste)
print(ma_liste[0:-1])
print(ma_liste[0:len(ma_liste)])
print(ma_liste[:-1])
print(ma_liste[:])
print(ma_liste[2:])
print(ma_liste[::2])
print(ma_liste[1::2])
print(ma_liste[::-2])
nouvelle_liste = ma_liste[1::2]


# In[63]:


a = [ 1 , 4 , 8 , [2, 3]]
b = a
b[0] = 6
print(a)

a = [ 1 , 4 , 8 , [2, 3]]
b = list(a)
b[0] = 6
b[-1][0] = 6
print(a)


# In[65]:


a = 2.4
b = int(a)
print(b)
c = float(b)
print(c)
# str() list() dict() set()
print(set([2,4,8,2,2,2,16]))
len(set([2,4,8,2,2,2,16]))


# In[ ]:


a = [ 1 , 4 , 8, 16, 18 , [2, 3]]
# du deuxième au dernier
# du premier à l'avant avant dernier
# un élément sur deux à partir du 3e élément
# un élément sur deux en sens inverse
# de l'avant dernier au 2e


# In[73]:


age = 30

if age > 18:
    print("majeur")
elif age < 18:
    print("mineur")
else:
    print("tu as 18 ans")
    print("autre ligne")
    
print("Affiché quoiqu'il en soit")


# In[74]:


age = 24
while age > 18:
    print(age)
    age -= 1


# In[75]:


for i in [4,2,3,10]:
    print(i)


# In[76]:


for i in range(100):
    print(i)


# In[85]:


list(range(15,100))


# # Fizz Buzz
# 
# Pour tous les entiers de 0 à 100:
# - afficher fizz s'il est divisible par 3
# - afficher buzz s'il est divisible par 5
# - afficher bazz s'il est divisible par 3 et 5
# - sinon on affiche l'entier

# In[86]:


for i in range(101):
    if i % 15 == 0:
        print("bazz")
    elif i % 5 == 0:
        print("buzz")
    elif i % 3 == 0:
        print("fizz")
    else:
        print(i)


# In[ ]:





# In[81]:


# help(np.ones)


# In[82]:


# dir(a)


# In[88]:


nom = raw_input("Quel est votre nom ?") # input pour la version 2
print(nom)


# In[89]:


liste_noms = []
liste_noms.append("Mathieu")

liste_obj = []
liste_obj = liste_obj + [{"nom": "Barney"}]


# In[90]:


students = []
continuer = True

while continuer:
    nom = input("Quel est votre nom ?")
    prenom = input("Quel est votre prenom ?")
    age = int(input("Quel est votre age ?"))
    students.append({
        "nom": nom,
        "prenom": prenom,
        "age": age
    })
    continuer = input("Voulez-vous continuer ? Y/N") == "Y"


# In[93]:


students


# In[94]:


liste_noms = []
for s in students:
    liste_noms.append(s["nom"])


# In[96]:


liste_noms = [s["nom"] for s in students]


# In[97]:


liste_noms


# In[ ]:




