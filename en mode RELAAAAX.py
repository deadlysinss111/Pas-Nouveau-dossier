from random import randint

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def conway(x):
    plateau=[]
    for i in range(x):
      row=[]
      for j in range(x):
        row.append(f"{i}/{j}")
      plateau.append(row)
    return plateau

#definir la fonction morpion
def morpion():
  #Assigne à une variable grid le retour de la fonction conway(3)
  grid=conway(3)
  #Pour k allant de 0 à 2
  for k in range(3):
    #Écrire l'élément à l'index k de grid
    print(grid[k])
  #Assigne à une variable player le retour de la fonction input("O or X ?")
  player=input("O or X ?")
  #Effectuer une assertion qui vérifie si player est égal soit à 'O' soit à 'X'
  assert player=='O' or player=='X'
  #Si player est égal à 'O'
  if player=='O':
    #alors pc est égal à 'X'
    pc='X'
  #Sinon
  else:
    #pc est égal à 'O'
    pc='O'
  #Si la fonction randint renvoie 1
  if randint(0,1)==1:
    #alors écris "You begin"
    print("You begin")
    #Assigne à colonne le retour de la fonction integer input demandant au joueur s'il veut la colonne numéro 0, 1 ou 2 
    colonne=int(input("colonne ? (0, 1 ou 2)"))
    #Assigne à ligne le retour de la fonction integer input demandant au joueur s'il veut la ligne numéro 0, 1 ou 2 
    ligne=int(input("ligne ? (0, 1 ou 2)"))
    #Execute la fonction play avec les paramètres grid, player, ligne et colonne
    play(grid, player, ligne, colonne)
    #Assigne à la variable currentTurn la valeur pc
    currentTurn=pc
    #Pour k de allant 0 à 2
    for k in range(3):
      #Écrire l'élément à l'index k de grid 
      print(grid[k])
  #Sinon
  else:
    #Écrire "npc starts"
    print("npc starts")
    #Assigne à la variable colonne la valeur 1
    colonne=1
    #Assigne à la variable ligne la valeur 1
    ligne=1
    #Execute la fonction play avec les paramètres grid, player, ligne et colonne
    play(grid, pc, ligne, colonne)
    #Assigne à la variable currentTurn la valeur player
    currentTurn=player
    #Pour k allant de 0 à 2
    for k in range(3):
      #Écrire l'élément à l'index k de grid 
      print(grid[k])
  #Assigne à la variable listOfPlayed une liste dans une liste qui contient les termes ligne colonne
  listOfPlayed=[[ligne, colonne]]
  #Assigne à la variable isPlaying la valeur 1
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
      #cpu----------------------
      endThisWhile=0
      #2 pions pc sur une ligne
      emergency=checkGrid(grid)
      if emergency[0]==pc:
        if emergency[1]=="ligne":
          for i in grid[emergency[2]]:
            if i!=pc:
              i=pc
        if emergency[1]=="colonne":
          for i in range(3):
            if grid[i][emergency[2]]!=pc:
              grid[i][emergency[2]]=pc
        if emergency[1]=="diagonale":
          if emergency[1]==1:
            for i in range(3):
              if grid[i][i]!=pc:
                grid[i][i]=pc
          if emergency[1]==2:
            for i in range(3):
              if grid[i][2-i]!=pc:
                grid[i][2-i]=pc
      #2 pions player sur une ligne
      if emergency[0]==player:
        if emergency[1]=="ligne":
          for i in grid[emergency[2]]:
            if i!=player:
              i=pc #play
              currentTurn=player
              endThisWhile=1
        if emergency[1]=="colonne":
          for i in range(3):
            if grid[i][emergency[2]]!=player:
              grid=play(grid, pc, i, emergency[2])
              currentTurn=player
              endThisWhile=1
        if emergency[1]=="diagonale":
          if emergency[1]==1:
            for i in range(3):
              if grid[i][i]!=player:
                grid=play(grid, pc, i, i)
                currentTurn=player
                endThisWhile=1
          if emergency[1]==2:
            for i in range(3):
              if grid[i][2-i]!=player:
                grid=play[grid, pc, i, 2-1]
                currentTurn=player
                endThisWhile=1
      #aucun joueur n'est sur le point de gagner
      randomPlayPref=[[0,0],[0,2],[2,0],[2,2]]
      randomPlay=[[1,0],[0,1],[2,1],[1,2],[1,1]]
      while endThisWhile==0:
        if len(randomPlayPref)!=0:
          randomNb=randint(0,len(randomPlayPref)-1)
          ligne=randomPlayPref[randomNb][0]
          colonne=randomPlayPref[randomNb][1]
          del randomPlayPref[randomNb]
        else:
          randomNb=randint(0,len(randomPlay-1))
          ligne=randomPlay[randomNb][0]
          colonne=randomPlay[randomNb][1]
          del randomPlayPref[randomNb]
        if [ligne, colonne] not in listOfPlayed :
          grid=play(grid, pc, ligne, colonne)
          listOfPlayed.append([ligne, colonne])
          currentTurn=player
          for k in range(3):
            print(grid[k])
          endThisWhile=1
        if len(randomPlay)==0:
          print("draw, ggwp")
          endThisWhile=1
          isPlaying=0
  #cpu-------------------
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

def checkGrid(grid):
  #check horizontal
  for i in grid:
    nbX=0
    nbO=0
    for j in i:
      if j=='X':
        nbX+=1
      if j=='O':
        nbO+=1
      if nbX==2 and nbO!=1:
        return ['X', "ligne", i]
      if nbO==2 and nbX!=1:
        return ['O', "ligne", i]
  #check vertical
  for i in range(3):
    nbX=0
    nbO=0
    for j in range(3):
      if grid[j][i]=='X':
        nbX+=1
      if grid[j][i]=='O':
        nbO+=1
      if nbX==2 and nbO!=1:
        return ['X', "colonne", j]
      if nbO==2 and nbX!=1:
        return ['O', "colonne", j]
  #check diagonal
  for i in range(3):
    if grid[i][i]=='X':
      nbX+=1
    if grid[i][i]=='O':
      nbO+=1
    if nbX==2 and nbO!=1:
      return ['X', "diagonale 1", i]
    if nbO==2 and nbX!=1:
      return ['O', "diagonale 1", i]
  for i in range(3):
    if grid[i][2-i]=='X':
      nbX+=1
    if grid[i][2-i]=='O':
      nbO+=1
    if nbX==2 and nbO!=1:
      return ['X', "diagonale", 1]
    if nbO==2 and nbX!=1:
      return ['O', "diagonale", 2]
  return ['','',0]

morpion()

liste = [["-","-","-","-","-"], \
        ["-",1,1,2,"-"], \
        ["-",2,1,1,"-"], \
        ["-",1,2,0,"-"], \
        ["-","-","-","-","-"]]
      
def visuel(tableau):
  ''' affichage d'une grille : les 1 sont représentés par 
  des "X" , les 2 par un "O" et les 0 un "." '''
  for ligne in tableau:
    for col in ligne:
      if col == 1:
        print(bcolors.OKBLUE+"  X  ",end=""+bcolors.ENDC)
      elif col == 2:
        print(bcolors.HEADER+"  O  ",end=""+bcolors.ENDC)
      elif col == 0:
        print(bcolors.BOLD+"  .  ",end=""+bcolors.ENDC)
      else:
        print(bcolors.FAIL+"  -  ",end="")
    print()

visuel(liste)