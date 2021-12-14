"""
Exercice 10 : MORPION
> Faire le jeu du morpion en text

Rappel :
>> 9 case au morpion : On va le représenter dans une list appeler cases[]
 0 | 1 | 2
 ― + ― + ―
 3 | 4 | 5
 ― + ― + ―
 6 | 7 | 8

[0,1,2,3,4,5,6,7,8]

>> Trois valeur pour chaque case : ' ' '0' 'X'
exemple de jeu :

   | 0 |  
 ― + ― + ―
   | 0 | X
 ― + ― + ―
 X | 0 | X

[' ','0',' ',' ','0','X','X','0','X']

>> Pour jouer au jeu :
Au debut le jeu s'affichera 
   |   |  
 ― + ― + ―
   |   |  
 ― + ― + ―
   |   |  

Puis l'utilisateur tapera une commande 
X 1 1 (ajouter X à la ligne 1 colonne 1)

Puis le jeu se met à jour
   |   |  
 ― + ― + ―
   | X |  
 ― + ― + ―
   |   |  

>> Normalement le jeu se termine une fois qu'il y as un allignement mais pour simplifier 
(au début) on considérera que c'est le joueur qui decide de terminer la partie
en écrivant 'exit' ou 'quit' par exemple

>> Quelque fonction sont déjà entamer pour aider !!
"""


def game_print(cases) : # Fonction d'affichage du jeu
    pass

def game_play(synbole, i, j) : # Fonction de modification du jeu (jouer X ou 0)
    pass

def check_move(synbole, i, j) : # Foction qui vérifie si la case est libre pour jouer
    pass