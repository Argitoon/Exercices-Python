# -*- coding : utf-8 -*-
"""
Exercice 2 : CALCULER ET DEFINIR UNE FONCTION
> Creer plusieurs fonction
>> Creer une fonction plus() qui prend deux parametre a et b et qui renvoie leurs somme
La fonction pourra être appeler en écrivant "plus 3 4" (pour la somme de 3 et 4) ou "3 + 4" 
sur la console 
>> Creer une fonction moins() qui prend deux parametre a et b et qui renvoie a moins b
La fonction pourra être appeler en écrivant "moins 3 4" (pour sustraction de 4 à 3) ou "3 - 4" 
sur la console 
>> Creer une fonction mult() qui prend deux parametre a et b et qui renvoie a multiplier par b
La fonction pourra être appeler en écrivant "mult 3 4" ou "3 * 4" 
>> Creer une fonction div_s() qui prend deux parametre a et b et qui renvoie la division de a par b
La fonction pourra être appeler en écrivant "div_s 3 4" ou "3 : 4" 
>> Creer une fonction div_int() qui prend deux parametre a et b et qui renvoie la division entiere (sans virgule) de a par b
La fonction pourra être appeler en écrivant "div_int 3 4" ou "3 // 4" 
>> Creer une fonction div_rest() qui prend deux parametre a et b et qui renvoie le rest de la division entiere de a par b (ou autrement dit le modulo de a par b)
La fonction pourra être appeler en écrivant "div_rest 3 4" ou "3 % 4" 
>> Creer une fonction moyenne() qui prend deux parametre a et b et qui renvoie la myenne des deux
La fonction pourra être appeler en écrivant "moyenne 3 4" 

Ce que ça doit afficher :
mult 2 2
4
div_s 3 2
1.5
div_int 3 2
1
div_rest 3 2
1
moyenne 0 10
5
"""

def plus(a,b) :
    pass

def moins(a,b) :
    pass

def mult(a,b) :
    pass

def div_s(a,b) :
    pass

def div_int(a,b) :
    pass

def div_rest(a,b) :
    pass

def moyenne(a,b) :
    pass




#================================================================================================
#========================== IGNORER CE QU'IL Y AS PLUS BAS ======================================
#================================================================================================



def print_error():
    print ("❌ Error ❌")
    print ("Not enougth argument !")
    pass

while True :
    fonction = input()

    if fonction == "close" : 
        break

    elif "plus" in fonction or "+" in fonction : 
        fonction = fonction.replace(f"+",'$')
        fonction = fonction.replace(f"plus ",'')
        if "$" in fonction :
            fonction = fonction.replace(f" ",'')
            a , b = fonction.split("$")
        else :
            a , b = fonction.split(" ")
       
        if a.isnumeric() :
            a = int(a)
        else :
            print_error()
        if b.isnumeric :
            b = int(b)
        else :
            print_error()
           
        test = (plus (a, b))
        if test == (a+b) :
            print ("✔️  Sucess ✔️")
        else : 
            print ("❌ Failure ❌")
            print ("Wrong answer !")
        print (test) 

    elif "moins" in fonction or "-" in fonction : 
        fonction = fonction.replace(f"-",'&')
        fonction = fonction.replace(f"moins ",'')
        if "$" in fonction :
            fonction = fonction.replace(f" ",'')
            a , b = fonction.split("$")
        else :
            a , b = fonction.split(" ")
       
        if a.isnumeric() :
            a = int(a)
        else :
            print_error()
        if b.isnumeric :
            b = int(b)
        else :
            print_error()
           
        test = (moins (a, b))
        if test == (a-b) :
            print ("✔️  Sucess ✔️")
        else : 
            print ("❌ Failure ❌")
            print ("Wrong answer !")
        print (test)

    elif "mult" in fonction or "*" in fonction : 
        fonction = fonction.replace(f"*",'$')
        fonction = fonction.replace(f"mult ",'')
        cmp = 0
        if "$" in fonction :
            fonction = fonction.replace(f" ",'')
            a , b = fonction.split("$")
        else :
            a , b = fonction.split(" ")
       
        if a.isnumeric() :
            a = int(a)
        else :
            print_error()
        if b.isnumeric :
            b = int(b)
        else :
            print_error()
           
        test = (mult(a, b))
        if test == (a*b) :
            print ("✔️  Sucess ✔️")
        else : 
            print ("❌ Failure ❌")
            print ("Wrong answer !")
        print (test)

    elif "div_int" in fonction or "//" in fonction : 
        fonction = fonction.replace(f"//",'$')
        fonction = fonction.replace(f"div_int ",'')
        if "$" in fonction :
            fonction = fonction.replace(f" ",'')
            a , b = fonction.split("$")
        else :
            a , b = fonction.split(" ")
       
        if a.isnumeric() :
            a = int(a)
        else :
            print_error()
        if b.isnumeric :
            b = int(b)
        else :
            print_error()
           
        test = (div_int(a, b))
        if test == (a//b) :
           print ("✔️  Sucess ✔️")
        else : 
            print ("❌ Failure ❌")
            print ("Wrong answer !")
        print (test)
    
    elif "div_rest" in fonction or "%" in fonction : 
        fonction = fonction.replace(f"%",'$')
        fonction = fonction.replace(f"div_rest ",'')
        if "$" in fonction :
            fonction = fonction.replace(f" ",'')
            a , b = fonction.split("$")
        else :
            a , b = fonction.split(" ")
       
        if a.isnumeric() :
            a = int(a)
        else :
            print_error()
        if b.isnumeric :
            b = int(b)
        else :
            print_error()
           
        test = (div_rest(a, b))
        if test == (a%b) :
           print ("✔️  Sucess ✔️")
        else : 
            print ("❌ Failure ❌")
            print ("Wrong answer !")
        print (test)
    
    elif "div_s" in fonction or ":" in fonction : 
        fonction = fonction.replace(f":",'$')
        fonction = fonction.replace(f"div_s ",'')
        if "$" in fonction :
            fonction = fonction.replace(f" ",'')
            a , b = fonction.split("$")
        else :
            a , b = fonction.split(" ")
       
        if a.isnumeric() :
            a = int(a)
        else :
            print_error()
        if b.isnumeric :
            b = int(b)
        else :
            print_error()
           
        test = (div_s(a, b))
        if test == (a/b) :
            print ("✔️  Sucess ✔️")
        else : 
            print ("❌ Failure ❌")
            print ("Wrong answer !")
        print (test) 

    elif "moyenne" in fonction :
        fonction = fonction.replace(f"moyenne ",'')
        if "$" in fonction :
            fonction = fonction.replace(f" ",'')
            a , b = fonction.split("$")
        else :
            a , b = fonction.split(" ")
       
        if a.isnumeric() :
            a = int(a)
        else :
            print_error()
        if b.isnumeric :
            b = int(b)
        else :
            print_error()
           
        test = (moyenne(a, b))
        if test == (a+b)/2 :
            print ("✔️  Sucess ✔️")
        else : 
            print ("❌ Failure ❌")
            print ("Wrong answer !")
        print (test) 

    else :
        print ("❌ Error ❌")
        print ("Unidentified function !")
        

