"""
Exercice 5 : LISTE ET TABLEAU
> Definissons les liste suivante :
L1 = [1,2,3,2,1]
L2 = [100,54,3,6,8,34]

>> Afficher le premier élément de la liste L1[]
>> Creer une nouvelle liste vide L3[]
>> Ajouter 6 à la liste L1[]
>> Changer le 3e élément de la liste L1[] en 9
>> Creer une nouvelle list qui sappel L4[] en utilisant L2[] qui n'inclu 
pas le chiffre 3
>> Ajouter à L3[] le nombre de 1 qu'il y as dans L1[]
>> Creer une list L5[] qui est la fusion de L1[] et L2[]
>> Ajouter la longuer de la list L5[] dans L3[]

Ce que ça doit afficher :
2
L1 =  [1, 2, 9, 2, 1, 6]
L2 =  [100, 54, 3, 6, 8, 34]
L3 =  [2, 12]
L4 =  [100, 54, 6, 8, 34]
L5 =  [1, 2, 9, 2, 1, 6, 100, 54, 3, 6, 8, 34]
"""
#====== LISTE PRE-DEFINI ======

L1 = [1,2,3,2,1]
L2 = [100,54,3,6,8,34]

#====== LISTE A DEFINIR ======

print(L1[1])
L3 = []
L1 = L1 + [6]
L1[2] = 9
L4 = L2[:]
ind = L4.index(3)
del L4[ind]
count = L1.count(1)
L3 = L3 + [count]
L5 = L1 + L2
long = len(L5)
L3 = L3 + [long]


#================================================================================================
#========================== IGNORER CE QU'IL Y AS PLUS BAS ======================================
#================================================================================================

print("L1 = ", L1)
print("L2 = ", L2)
print("L3 = ", L3)
print("L4 = ", L4)
print("L5 = ", L5)
