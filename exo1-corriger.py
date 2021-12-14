# -*- coding : utf-8 -*-
"""
Exercice 1 : INPUT et PRINT
> Faire une discution interactif de manière suivante :
>> Demander le nom de l'utilisateur (Quel est ton nom ?)
>> Lire ça réponce et afficher un message de bienvenu (Bienvenu *NOM* !!)
>> Demander l'âge de l'utilisateur son âge (Quel âge a tu ?)
>> Afficher un message de fin (Merci pour ta participation)

Ce que ça doit afficher :
Quel est votre nom ?
Argi
Bienvenu Argi !!
Quel âge a tu ?
19
Merci pour ta participation
"""

nom = input("Quel est ton nom ?\n")
print (f"Bienvenu {nom} !!")
input ("Quel âge a tu ?\n") # \n obligatoire !!!
print ("Merci pour ta participation")

