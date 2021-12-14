"""
Exercice 3 : LE TYPE BOOL
> Creer plusieurs fonctions
>> Creer une focntion all_true() qui renvoie toujours True
>> Creer une focntion all_false() qui renvoie toujours False
>> Creer une fonction is_even() qui prend comme paramettre un nombre et qui 
renvoie si il est pair ou non
>> Creer une fonction is_more_than_10() qui prend comme paramettre un nombre et qui 
renvoie si il est plus grand ou égal à 10
>> Creer une foction is_odd_and_more_than_10() en utilisant les fonction précédente et qui 
revoie si le nombre est impair (non pair) et plus grand ou égal à 10
>> Creer une foction is_odd_or_less_than_10() en utilisant les fonction précédente et qui 
revoie si le nombre est impair (non pair) ou (non inclusif) plus petit que 10


Ce que ça doit afficher :
11
all_true --> True
all_false --> False
is_even --> False
is_more_than_10 --> True
is_odd_and_more_than_10 --> True
is_odd_or_less_than_10 --> True

8
all_true --> True
all_false --> Talse
is_even --> True
is_more_than_10 --> True
is_odd_and_more_than_10 --> Talse
is_odd_or_less_than_10 --> True
"""

def all_true():
    pass

def all_false():
    pass

def is_even(n):
    pass

def is_more_than_10(n):
    pass

def is_odd_and_more_than_10(n):
    pass

def is_odd_or_less_than_10(n):
    pass





#================================================================================================
#========================== IGNORER CE QU'IL Y AS PLUS BAS ======================================
#================================================================================================

def print_error():
    print ("❌ Error ❌")
    print ("Not enougth argument !")
    pass

while True :
    nombre = input()
    if not nombre.isnumeric() :
        if nombre == "close" :
            break
        print ("❌ Error ❌")
        print ("Not a valid argument !")
    else :
        nombre = int(nombre)
        print(f"all_true --> {all_true()}")
        print(f"all_false --> {all_false()}")
        print(f"is_even --> {is_even(nombre)}")
        print(f"is_more_than_10 --> {is_more_than_10(nombre)}")
        print(f"is_odd_and_more_than_10 --> {is_odd_and_more_than_10(nombre)}")
        print(f"is_odd_or_less_than_10 --> {is_odd_or_less_than_10(nombre)}\n")
   