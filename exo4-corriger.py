"""
Exercice 4 : IF, ELIF ET ELSE
> Demander un nombre à l'utilisateur et 
>> afficher "Ce nombre est 0" si le nombre est 0
>> afficher "Ce nombre est pair" si le nombre est pair 
>> afficher "Ce nombre est impair" si le nombre est impair

Ce que ça doit afficher :
Donner moi nombre :
1
Ce nombre est impair
"""

nombre = input("Donner moi nombre :\n")
if int(nombre) == 0 :
    print("Ce nombre est 0")
elif int(nombre) % 2 == 0 :
    print("Ce nombre est pair")
else :
    print ("Ce nombre est impair")