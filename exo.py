from random import randint
#on defini une liste qui contien les chiox possibles
choixPossibles=["pierre","papier","ciseaux","pierre"]
#on defini une variable choixOrdi qui represente le caractere choisi par l'ordinateur
choixOrdi=''
#on defini une variable choixJoueur qui est un str vide
choixJoueur=''
#on défini isPlaying, variable qui défini si le jeu est joué ou non
isPlaying=1
#on met en place une boucle qui tourne tant que le jeu est joué
while isPlaying==1:
    #l'ordi fait son choix dans la variable choixOrdi
    choixOrdi=randint(0, 2)
    #on demande le choix du joueur
    choixJoueur=input("pierre, papier ou ciseaux pour jouer, stop pour arreter le jeu")
    #si le joueur souhaite stopper le jeu
    if choixJoueur=='stop':
        #on met fin a la boucle
        isPlaying=0
        break
    #on compare les deux choix et effectue une scripte différent selon le résultat
    #si égalité
    if choixJoueur==choixPossibles[choixOrdi]:
        #on affiche l'égalité
        print("l'ordi a choisi ", choixPossibles[choixOrdi],", égalité")
    #sinon si le joueur gagne
    elif choixJoueur==choixPossibles[choixOrdi+1]:
        #on affiche que le joueur gagne
        print("l'ordi a choisi ", choixPossibles[choixOrdi],", gagné")
    #sinon
    else:
        #on affiche que le joueur perd
        print("l'ordi a choisi ", choixPossibles[choixOrdi],", perdu")
    



tableau=[0,1,1,1,0,1,1,0,1]

def concatWithComma(str1=str, str2=str):
    return (str1+", "+str2)




#definir une fonction fibonacci qui prend en paramètre un nombre et qui retourne les 10 occurences la suite de fabinacci a partir de ce nombre
    #definir i un index de depart
    #definir chaineRetour telle qu'une chaine de caractere vide
    #je defini un booleen tel que firstTurn est true
    #tant que i
        #alors j'attribue a une variable la valeur de tableau a l'indexe i
        #si selected est egal a x et firstTurn est true
            #alors on assigne a chaine retour la valeur de str(i)
            #changer la valeur de firstTurn a false
        #sinon si selected est egal a x
            #alors j'assigne le retour de concatWithComma tel que : concatWithComma(chaineRetour, i) à chaineRetour
        #j'increment i de 1
    #retourner la chaine retour