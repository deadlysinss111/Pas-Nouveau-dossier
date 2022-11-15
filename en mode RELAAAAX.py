"""def concatWithComma(str1=str, str2=str):
    return (str1+", "+str2)


def fibonacci(init):
    l=[0,init]
    listSTR=''
    for i in range(10):
        l.append(l[i]+l[i+1])
    for i in range(0,10, 2):
        listSTR=(listSTR + concatWithComma(str(i),str(i+1) +', '))
    listSTR=(listSTR + '...')
    return listSTR

print(fibonacci(1))








#DEBUT  
from random import randint
#on admet l'existance d'une fonction randint qui retourne un int aléatoire entre les deux int donnés en paramètres inclus
def random(x,y):
    return randint(x,y)
#on admet l'existance d'une fonction input qui retourne une chaine de caractères mise en paramètre, demande à l'utilisateur d'écrire quelque chose et le retourne sous forme d'une chaine de caractères 

#on défini une fonction shifumi qui ne prend aucun paramètre
def shifumi():
    #on défini une liste scores de longueur 2 avec 0 et 0 comme valeurs
    scores=[0,0]
    #on défini une liste listChoices qui contien les choix possibles "caillou", "papyrus", "cisailles", "caillou" (le second caillou sera utile plus tard)
    listChoices=["caillou","papyrus","cisailles","caillou"]
    #on défini une variable choixOrdi (qui representera le caractere choisi par l'ordinateur), et lui assigne la valeur 0
    choixOrdi=0
    #on défini une variable choixJoueur (qui representera le caractere choisi par l'ordinateur), et lui assigne la valeur d'un str vide
    choixJoueur=''
    #on défini une variable isPlaying (défini si le jeu est joué ou non), et lui assigne la valeur 1
    isPlaying=1
    #tant que isPlaying est égal à 1 (tant que le jeu est joué)
    while isPlaying==1:
        #alors on assigne à l'ordi la valeur du retour d'un appel de la fonction randint avec 0 et 2 en paramètres
        choixOrdi=random(0,2)
        #on assigne à la variable choixJoueur le retour de l'execution de la fonction input avec "caillou, papyrus, cisailles ou stop" en paramètre
        choixJoueur=input("caillou, cisailles, papyrus ou stop")
        #on vérifie que choixJoueur soit bien un str qui contient uniquement "caillou", "papyrus", "cisaille" ou "stop"
        assert choixJoueur in listChoices or choixJoueur=="stop"
        #si choixJoueur est égal à "stop"
        if choixJoueur=="stop":
            #alors on affiche que la partie est terminée et la liste scores
            print("partie terminée \n",scores)
            #on stop la boucle
            break
        #si choixJoueur est égal à listChoices à l'indice choixOrdi
        if choixJoueur==listChoices[choixOrdi]:
            #alors on affiche listChoices à l'indice choixOrdi
            print(listChoices[choixOrdi])
            #on affiche "draw"
            print("draw")
        #sinon si choixJoueur est égal listChoices à l'indice (choixOrdi + 1)
        if choixJoueur==listChoices[choixOrdi]:
            #alors on affiche listChoices à l'indice choixOrdi
            print(listChoices[choixOrdi])
            #on affiche que le joueur gagne
            print("you won (gg <3)")
            #on incrémente la valeur de ls scores à l'indice 0
            scores[0]+=1
            #on affiche la liste scores
            print(scores)
        #sinon
        else:
            #alors on affiche listChoices à l'indice choixOrdi
            print(listChoices[choixOrdi])
            #on affiche que le joueur perd
            print("next time :c")
            #on incrémente la valeur de score à l'indice 1
            scores[1]+=1
            #on affiche la liste scores
            print(scores)
    #afficher l'execution de la fonction
    print(shifumi())
    #FIN
    """


from random import randint

def conway(x):
    plateau=[]
    for i in range(x):
      row=[]
      for j in range(x):
        row.append(f"{i}/{j}")
      plateau.append(row)
    return plateau


def callConway(plateau, x, y):
    return [plateau[x,y]]

def callCross(plateau,x,y):
    cross=''
    if y>0:
        cross = cross +callConway(plateau, x, y-1)
    else:
        cross = cross +"min y"
    cross = cross +"\n"
    if x>0:
        cross = cross +callConway(plateau, x-1, y)
    else:
        cross = cross +"min x"
    cross = cross +" // "
    cross = cross +callConway(plateau, x, y)
    cross = cross +" // "
    if x<len(plateau-1):
        cross = cross +callConway(plateau, x+1, y)
    else:
        cross = cross +"max x"
    cross = cross +"\n"
    if y<len(plateau-1):
        cross = cross +callConway(plateau, x, y+1)
    else:
        cross = cross +"max y"

def morpion():
    grid=conway(3)
    for k in range(3):
      print(grid[k])
    player=input("O or X ?")
    assert player=='O' or player=='X'
    if player=='O':
        pc='X'
    else:
        pc='O'
    if randint(0,1)==1:
        print("you begin")
        colonne=int(input("colonne ? (0, 1 ou 2)"))
        ligne=int(input("ligne ? (0, 1 ou 2)"))
        play(grid, player, ligne, colonne)
        currentTurn=pc
        for k in range(3):
          print(grid[k])
    else:
        print("npc starts")
        colonne=randint(0,2)
        ligne=randint(0,2)
        play(grid, pc, ligne, colonne)
        currentTurn=player
        for k in range(3):
          print(grid[k])
    listOfPlayed=[[ligne, colonne]]
    isPlaying=1
    while isPlaying==1:
        if currentTurn==player:
            colonne=int(input("colonne ? (0, 1 ou 2)"))
            ligne=int(input("ligne ? (0, 1 ou 2)"))
            if [ligne, colonne] in listOfPlayed :
                print("someone already played here :thinking:")
            elif colonne>2 or ligne>2:
              print("fin frérot... tu es cringe")
            else:
                grid=play(grid, player, ligne, colonne)
                listOfPlayed.append([ligne, colonne])
                currentTurn=pc
        else :
            colonne=randint(0,2)
            ligne=randint(0,2)
            if [ligne, colonne] not in listOfPlayed :
                grid=play(grid, pc, ligne, colonne)
                listOfPlayed.append([ligne, colonne])
                currentTurn=player
                for k in range(3):
                  print(grid[k])
        if checkWin(grid):
          if currentTurn==pc:
            print("you defeated a random bot, gg bro")
          else:
            print("man... you should ask yoourself about certains things")
          isPlaying=0

def play(grid, player, colonne, ligne):
    grid[colonne][ligne]=player
    return grid

def checkWin(grid):
  if grid[0][0]==grid[1][1]==grid[2][2] or grid[2][0]==grid[1][1]==grid[0][2]:
    return True
  for i in grid:
    if i[0]==i[1]==i[2]:
      return True
    for i in range(3):
      if grid[0][i]==grid[1][i]==grid[2][i]:
        return True
  return False

morpion()