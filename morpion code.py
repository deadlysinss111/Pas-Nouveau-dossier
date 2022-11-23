from random import randint


#classe de couleurs imortées
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


#génère un tableau de taille x avec chaque cellule un str de ses coordonnées
def conway(x):
  plateau = []
  for i in range(x):
    row = []
    for j in range(x):
      row.append(f"{i}/{j}")
    plateau.append(row)
  return plateau


#la fonction qui lance le morpion contre le bot
def pve():
  grid = conway(3)
  visuel(grid, "nothing")
  #on demande au joueur si il veux jouer X ou O
  player = input(bcolors.HEADER + ' O ' + bcolors.ENDC + 'or' +
                 bcolors.OKBLUE + ' X ' + bcolors.ENDC + '?')
  assert player == 'O' or player == 'X'
  #on assigne a joueur son signe et on change la couleur des textes en fonction
  if player == 'O':
    pc = 'X'
    textColor=bcolors.HEADER
  else:
    pc = 'O'
    textColor=bcolors.OKBLUE
  #on décide au hasard qui commence
  if randint(0, 1) == 1:
    print(bcolors.ENDC + bcolors.BOLD + "You begin")
    column = int(input(textColor + "column ? (0, 1 ou 2)"))
    row = int(input(textColor + "row ? (0, 1 ou 2)"))
    play(grid, player, row, column)
    currentTurn = pc
  else:
    print("npc starts")
    column = 1
    row = 1
    play(grid, pc, row, column)
    currentTurn = player
    visuel(grid, player)
  listOfPlayed = [[row, column]]
  isPlaying = 1
  
  #une fois le premier tour passé, on lance une boucle qui se stop dès qu'un joueur gagne ou que la grille est pleine
  while isPlaying == 1:
    if currentTurn == player:
      fullGrid = 0
      for i in grid:
        for j in i:
          if j == 'X' or j == 'O':
            fullGrid += 1
      if fullGrid == 9:
        print("draw, ggwp")
        endThisWhile = 1
        isPlaying = 0
        break
      column = int(input(textColor + "column ? (0, 1 ou 2)"))
      row = int(input(textColor + "row ? (0, 1 ou 2)"))
      if [row, column] in listOfPlayed:
        print("someone already played here :thinking:")
      elif not(0 <= column <= 2) or not (0 <= row <= 2):
        print("fin frérot... tu es cringe")
      else:
        grid = play(grid, player, row, column)
        listOfPlayed.append([row, column])
        currentTurn = pc
    else:
      endThisWhile = 0
      if [1,1] not in listOfPlayed:
        play(grid, pc, 1, 1)
        listOfPlayed.append([1,1])
        endThisWhile=1
        visuel(grid, player)
        currentTurn=player
      emergency = checkGrid(grid)
      
      #si le pc est sur le point de gagner
      #on va localiser où grâce à des conditions et des appels de la fonction checkGrid et jouer en fonction
      if emergency[0] == pc:
        if emergency[1] == "row":
          for i in grid[emergency[2]]:
            if i != pc:
              grid = play(grid, pc, emergency[2], grid[emergency[2]].index(i))
              listOfPlayed.append([emergency[2], grid[emergency[2]].index(i)])
              currentTurn = player
        if emergency[1] == "column":
          for i in range(3):
            if grid[i][emergency[2]] != pc:
              grid = play(grid, pc, i, emergency[2])
        if emergency[1] == "diagonale":
          if emergency[2] == 1:
            for i in range(3):
              if grid[i][i] != pc:
                grid = play(grid, pc, i, i)
          if emergency[2] == 2:
            for i in range(3):
              if grid[i][2 - i] != pc:
                grid = play(grid, pc, i, 2 - i)
                
      #si le joueur est sur le point de gagner
      #on va localiser où grâce à des conditions et des appels de la fonction checkGrid et jouer en fonction
      if emergency[0] == player:
        if emergency[1] == "row":
          for i in grid[emergency[2]]:
            if i != player:
              grid = play(grid, pc, emergency[2], grid[emergency[2]].index(i))
              currentTurn = player
              endThisWhile = 1
              visuel(grid, player)
        if emergency[1] == "column":
          for i in range(3):
            if grid[i][emergency[2]] != player:
              grid = play(grid, pc, i, emergency[2])
              currentTurn = player
              endThisWhile = 1
              visuel(grid, player)
        if emergency[1] == "diagonale":
          if emergency[2] == 1:
            for i in range(3):
              if grid[i][i] != player:
                grid = play(grid, pc, i, i)
                listOfPlayed.append([i, i])
                currentTurn = player
                endThisWhile = 1
                visuel(grid, player)
          if emergency[2] == 2:
            for i in range(3):
              if grid[i][2 - i] != player:
                grid = play(grid, pc, i, 2 - i)
                listOfPlayed.append([i, 2 - i])
                currentTurn = player
                endThisWhile = 1
                visuel(grid, player)
      randomPlayPref = [[0, 0], [0, 2], [2, 0], [2, 2]]
      randomPlay = [[1, 0], [0, 1], [2, 1], [1, 2], [1, 1]]
      
      #si aucun joueur n'est sur le point de gagner
      while endThisWhile == 0:
        #on essaie des coups au hasard et on priorise les coins
        if len(randomPlayPref) != 0:
          randomNb = randint(0, len(randomPlayPref) - 1)
          row = randomPlayPref[randomNb][0]
          column = randomPlayPref[randomNb][1]
          del randomPlayPref[randomNb]
        elif len(randomPlay) != 0:
          randomNb = randint(0, len(randomPlay) - 1)
          row = randomPlay[randomNb][0]
          column = randomPlay[randomNb][1]
          del randomPlay[randomNb]
        #si il n'y a plus de case disponible, la grille est pleine, il y a égalité
        else:
          print("draw, ggwp")
          endThisWhile = 1
          isPlaying = 0
          break
        #le coup au hasard est joué si rien n'est déja joué sur la case, sinon on relance la boucle jusqu'à avoir un coup sur une case vide
        if [row, column] not in listOfPlayed:
          grid = play(grid, pc, row, column)
          listOfPlayed.append([row, column])
          currentTurn = player
          visuel(grid, player)
          endThisWhile = 1
    #on vérifie si un joueur gagne
    if checkWin(grid):
      if currentTurn == pc:
        print("well done, the programm is bugged")
      else:
        print("man... you should ask yoourself about certains things")
      isPlaying = 0


#la fonction du morpien en 1 contre 1
def pvp():
  grid = conway(3)
  listOfPlayed=[]
  visuel(grid, "nothing")
  #on demande au joueur si il veux jouer X ou O
  player = input("player 1 : " + bcolors.HEADER + ' O ' + bcolors.ENDC + 'or' + bcolors.OKBLUE + ' X ' + bcolors.ENDC + '?')
  assert player == 'O' or player == 'X'
  if player == 'O':
    playerTwo = 'X'
    textColorOne=bcolors.HEADER
    textColorTwo=bcolors.OKBLUE
  else:
    playerTwo = 'O'
    textColorOne=bcolors.OKBLUE
    textColorTwo=bcolors.HEADER
  #on décide au hasard qui commence
  if randint(0, 1) == 1:
    print(bcolors.ENDC + bcolors.BOLD + "player 1 begins")
    currentTurn = player
  else:
    print(bcolors.ENDC + bcolors.BOLD + "player 2 begins")
    currentTurn = playerTwo
  isPlaying = 1
  
  #on lance le jeu
  while isPlaying == 1:
    fullGrid = 0
    for i in grid:
      for j in i:
        if j == 'X' or j == 'O':
          fullGrid += 1
    if fullGrid == 9:
      print("draw, ggwp")
      isPlaying = 0
      break
    if currentTurn == player:
      column = int(input(textColorOne + "column ? (0, 1 ou 2)"))
      row = int(input(textColorOne +"row ? (0, 1 ou 2)"))
      if [row, column] in listOfPlayed:
        print("someone already played here :thinking:")
      elif 0 > column or 0 > row or column >2 or row >2 or type(column) != int or type(row) != int:
        print("fin frérot... tu es cringe")
      else:
        grid = play(grid, player, row, column)
        listOfPlayed.append([row, column])
        currentTurn = playerTwo
    else:
      column = int(input(textColorTwo +"column ? (0, 1 ou 2)"))
      row = int(input(textColorTwo + "row ? (0, 1 ou 2)"))
      if [row, column] in listOfPlayed:
        print("someone already played here :thinking:")
      elif 0>column or 0> row or column > 2 or row > 2 or type(column) != int or type(row) != int:
        print("fin frérot... tu es cringe")
      else:
        grid = play(grid, playerTwo, row, column)
        listOfPlayed.append([row, column])
        currentTurn = player
    visuel(grid, "nothing")
    
    #on vérifie si un joueur gagne
    if checkWin(grid):
      if currentTurn == player:
        print("player 2 won")
      else:
        print("player 1 won")
      isPlaying = 0

      
#fonction qui joue un pion sur la grille aux paramètres indiqués
def play(grid, player, column, row):
  grid[column][row] = player
  return grid


#fonction qui vérifie si un joueur a gagné
def checkWin(grid):
  if grid[0][0] == grid[1][1] == grid[2][2] or grid[2][0] == grid[1][
      1] == grid[0][2]:
    return True
  for i in grid:
    if i[0] == i[1] == i[2]:
      return True
    for i in range(3):
      if grid[0][i] == grid[1][i] == grid[2][i]:
        return True
  return False


#fonction qui regardxe l'état d'une grille et renvoie une liste contenant des informationssi un joueur est sur le point de gagner (joueur qui est sur le point de gagner, row / column / diagonale, indice)
def checkGrid(grid):
  #check horizontal
  for i in range(3):
    nbX = 0
    nbO = 0
    for j in range(3):
      if grid[i][j] == 'X':
        nbX += 1
      if grid[i][j] == 'O':
        nbO += 1
      if nbX == 2 and nbO != 1 and j == 2:
        return ['X', "row", i]
      if nbO == 2 and nbX != 1 and j == 2:
        return ['O', "row", i]
  #check vertical
  for i in range(3):
    nbX = 0
    nbO = 0
    for j in range(3):
      if grid[j][i] == 'X':
        nbX += 1
      if grid[j][i] == 'O':
        nbO += 1
      if nbX == 2 and nbO != 1 and j == 2:
        return ['X', "column", i]
      if nbO == 2 and nbX != 1 and j == 2:
        return ['O', "column", i]
  #chack diagonal
  nbX = 0
  nbO = 0
  for i in range(3):
    if grid[i][i] == 'X':
      nbX += 1
    if grid[i][i] == 'O':
      nbO += 1
    if nbX == 2 and nbO != 1 and i == 2:
      return ['X', "diagonale", 1]
    if nbO == 2 and nbX != 1 and i == 2:
      return ['O', "diagonale", 1]
  nbX = 0
  nbO = 0
  for i in range(3):
    if grid[i][2 - i] == 'X':
      nbX += 1
    if grid[i][2 - i] == 'O':
      nbO += 1
    if nbX == 2 and nbO != 1 and i == 2:
      return ['X', "diagonale", 2]
    if nbO == 2 and nbX != 1 and i == 2:
      return ['O', "diagonale", 2]
  return ['', '', 0]


#fonction qui rend la grille plus lisible et change les couleurs du texte
def visuel(tableau, choix):
  ''' affichage d'une grille : les 'X' sont représentés par 
  des 'X' , les 'O' par un 'O' et les cases vides par un "-" '''
  print(bcolors.FAIL + "------------------------")
  for row in tableau:
    for col in row:
      if col == 'X':
        print(bcolors.OKBLUE + bcolors.BOLD + "| X |", end="" + bcolors.ENDC)
      elif col == 'O':
        print(bcolors.HEADER + bcolors.BOLD + "| O |", end="" + bcolors.ENDC)
      else:
        print(bcolors.FAIL + "| - |", end="")
    print()
  print(bcolors.FAIL + "------------------------")


def start():
  choice = input(bcolors.BOLD+"solo or 1v1 ?")
  if choice == "solo":
    pve()
  elif choice == "1v1":
    pvp()
  else:
    print("fin frérot, tu es cringe")





start()
