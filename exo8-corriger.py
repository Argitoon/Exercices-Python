"""
Exercice 8 : RANDOM ET LE WHILE INFINI
> Definir trois fonction
>> La première (spell_until_vowel), la fonction epelera (print) le mot JUSQU'A 
une voyelle (a,e,i,o,u,y) (pour faire simple on considère que les lettre miniscule sans accent)
>> La seconde (random_number), la fonction renvera un nombre random entre 1 et 
le nombre écris par l'utilisateur
>> La seconde (repeat) sera appeler si l'utilisateur ecris un nombre puis un mot,
repetera le mot nombre de fois

>> Faire un boucle WHILE infini pour que le programe continu à s'executé même après avoir
efectué une foction. 
>> Faire en sorte que la foction random_number() ne soit appeler QUE lorsque l'utilisateur
ecris un nombre
>> Faire en sorte que la fonction repeat() ne soit appeler QUE lorsque l'utilisateur
ecris un nombre PUIS un mot (ou une phrase)
>> Faire en sorte que le mot "close" arrête le programe
>> Faire en sorte que la foction spell_until_vowel() fonction dans tout les autre cas

Ce que ça doit afficher :
5
3
4 bonjour Jojo !
bonjour Jojo !
bonjour Jojo !
bonjour Jojo !
bonjour Jojo !
stratosphere
s
t
r
"""
import random

def spell_until_vowel (word) :
    vowel = ['a','e','i','o','u','y']
    ind = 0
    while (not (word[ind] in vowel)) and (ind < len(word)-1) :
        print(word[ind])
        ind = ind + 1

def random_number (n) :
    res = random.randrange(1,n+1)
    print(res)


def repeat(n, word) :
    for i in range (n) :
        print(word)

while True :
    fonct = input()

    if fonct.isnumeric() : 
        random_number(int(fonct))
    elif fonct[0].isnumeric() : 
        n = int(fonct[0])
        word = fonct.replace(f"{fonct[0]} ",'')
        repeat(n, word)
    elif fonct == "close" :
        break
    else :
        spell_until_vowel(fonct)
        