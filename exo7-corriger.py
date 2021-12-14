"""
Exercice 7 : CHAINE DE CARACTERE
> Prenons la chaine de caractère suivant :
msg = "Hello World !"

(attention il ne faut en aucun cas modifier le msg !!!)

>> Afficher la position de la lettre "d" dans le msg
>> Afficher la position du mot "yolo" dans le msg
>> Afficher la nombre de "l" dans le msg
>> Afficher le msg en MAJUSCULE puis en minuscule
>> Afficher le msg mais remplacer le mot "Hello" par "Pizza"
>> Afficher le msg suivi par "No !"
>> En utilisant le msg afficher "Hell"
>> Afficher la longueur du msg
>> Afficher le msg à l'envers
>> Afficher si msg est un nombre ou pas
>> Afficher le message suivant (sans oublier les retour à la ligne, les tabulation et les "):
Voici un programme qui envoie
    "Hello World !"

Ce que ça doit afficher :
10
-1
3
HELLO WORLD !
hello world !
Pizza World !
Hello World !No !
Hell
13
! dlroW olleH
False
Voici un programme qui envoie
        "Hello World !"
"""
msg = "Hello World !"

print(msg.find("d"))
print(msg.find("yolo"))
print(msg.count("l"))
print(msg.upper())
print(msg.lower())
print(msg.replace("Hello", "Pizza"))
print(msg + "No !")
print(msg[0:4])
print(len(msg))
print("".join(reversed(msg)))
print(msg.isnumeric())
print("Voici un programme qui envoie\n\t\"Hello World !\"")
