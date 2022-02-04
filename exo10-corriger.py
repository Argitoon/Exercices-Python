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


def game_init() : #Initialise le jeu (que des cases vide)
  cases = [" "," "," ", " "," "," ", " "," "," "]
  return cases

def game_print(cases) : # Affiche le jeu (print)
  print(f" {cases[0]} | {cases[1]} | {cases[2]} ")
  print(f" ― + ― + ― ")
  print(f" {cases[3]} | {cases[4]} | {cases[5]} ")
  print(f" ― + ― + ― ")
  print(f" {cases[6]} | {cases[7]} | {cases[8]} ")
  return

def check_move(cases, i, j) : # Regarde si la case est vide (si on a le droit de poser qqch dessus)
  if cases[i*3 + j] == " " :
    return True
  print("Action impossible !")
  return False

def game_play(cases, synbole, i, j) : # Joue le jeu (place soit X soit 0)
  if check_move(cases, i, j) :
    cases[i*3 + j] = synbole

def game_is_over(cases) : # Vérifie si le jeu est terminé
  test = True

  for i in cases :
    if i == " " :
      test = False 
      # Si il n'y a pas de cases vide alors True -> Le jeu est fini

  if test :
    print("Egalité !")
    # Si il n'y a pas de cases vide alors True -> Le jeu est fini -> EGALITE
  
  if (cases[0] == "X" and  cases[1] == "X" and cases[2] == "X") or (cases[3] == "X" and  cases[4] == "X" and cases[5] == "X") or (cases[6] == "X" and  cases[7] == "X" and cases[8] == "X") or (cases[2] == "X" and  cases[4] == "X" and cases[6] == "X") or (cases[0] == "X" and  cases[4] == "X" and cases[8] == "X") or (cases[0] == "X" and  cases[3] == "X" and cases[6] == "X") or (cases[1] == "X" and  cases[4] == "X" and cases[7] == "X") or (cases[2] == "X" and  cases[5] == "X" and cases[8] == "X") :
    print(" BRAVO !!! X a gagné !")
    test = True
    # Si trois X sont alligné alors True -> X à gagner
  
  if (cases[0] == "0" and  cases[1] == "0" and cases[2] == "0") or (cases[3] == "0" and  cases[4] == "0" and cases[5] == "0") or (cases[6] == "0" and  cases[7] == "0" and cases[8] == "0") or (cases[2] == "0" and  cases[4] == "0" and cases[6] == "0") or (cases[0] == "0" and  cases[4] == "0" and cases[8] == "0") or (cases[0] == "0" and  cases[3] == "0" and cases[6] == "0") or (cases[1] == "0" and  cases[4] == "0" and cases[7] == "0") or (cases[2] == "0" and  cases[5] == "0" and cases[8] == "0") :
    print(" BRAVO !!! 0 a gagné !")
    test = True
    # Si trois 0 sont alligné alors True -> 0 à gagner

  return test

def game_rules() : #Affiche les regles du jeu (incomplet)
  pass



while True :
  var = input()
  if var == "Start" or var == "start" :
    cases = game_init()
    while not game_is_over(cases) :
      game_print(cases)
      game_rules()
      synbole = input()
      
      if synbole == "Close" or synbole == "close" : # "Close" -> Ferme le jeu
        break

      if synbole == "q" or synbole == "quit" or synbole == "Quit": # "q" -> Ferme le jeu
        break

      if synbole == "r" or synbole == "restart" or synbole == "Restart": # "r" -> Réinitialise le jeu
        cases = game_init()

      if synbole == "h" or synbole == "help" or synbole == "Help": # "h" -> montre les règles du jeu
        game_rules()
      
      if synbole[0] == "X" : # "X 1 1" -> Place X dans la case 1 1
        # le mieux serait de vérifié que synbole[2] et [4] sont numeric et entre 0 et 3
        row = int(synbole[2])
        col = int(synbole[4])
        game_play(cases,"X", row, col)

      if synbole[0] == "0" or synbole[0] == "O" :  # "0 1 1" ou "O 1 1" -> Place X dans la case 1 1
        # le mieux serait de vérifié que synbole[2] et [4] sont numeric et entre 0 et 3
        row = int(synbole[2])
        col = int(synbole[4])
        game_play(cases, "0", row, col)
      
      #Suite de la boucle
        
  break

      

