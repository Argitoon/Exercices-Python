"""
Exercice 9 : BACK A SABLE | CRYPTAGE
> Faire deux fonction :
>> la première crypter() prend comme paramettre une chaine de caractère et va retourner
une autre chaine de caractère "crypter" (modifier)
>> la première décrypter() prend comme paramettre une chaine de caractère crypter et va 
retourner une autre chaine de caractère "decrypter" (le mot d'origine)

Vous avez le choix entre plusieurs type de cryptage, vous pouvez exemple faire en sorte que
a --> b
b --> c
...
z --> a

mais vous pouvez aussi faire en sorte que chaque caractère correspond à un chiffre ou 
symbole
a --> 0
b --> 1
...
g --> .
h --> (
...
z --> ?

>> ATTENTION AUX ERREURS, en effet la fonction crypte ne peut peut être pas transformer
certain caractère comme les majuscule et il faudras gerer ces erreur

Voici un exemple qui pourrais s'afficher :
crypte hello world


"""
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def crypter(word) :
    new = ""
    for char in word :
        if char != " " :
            ind = alphabet.index(char)
            new = new + "".join(alphabet[(ind + 3)%(len(alphabet))])
        else :
            new = new + "."
    return new

def decrypter(word) :
    new = ""
    for char in word :
        if char != " " :
            ind = alphabet.index(char)
            new = new + "".join(alphabet[(ind - 3)%(len(alphabet))])
        else :
            new = new + "."
    return new

def verif(word) :
    for char in word :
        if not char in alphabet and char != " ":
            return False
    return True
while True :
    fonc = input()

    if fonc[0:7] == "crypter" :
        fonc = fonc[8:]
        fonc = fonc.lower()
        if verif(fonc) :
            print(crypter(fonc))
        else :
            print("ERROR")
    elif fonc[0:9] == "decrypter" :
        fonc = fonc[10:]
        fonc = fonc.lower()
        if verif(fonc) :
            print(decrypter(fonc))
        else :
            print("ERROR")
    elif fonc[0:5] == "close" :
        break
    else :
        print("probleme")


