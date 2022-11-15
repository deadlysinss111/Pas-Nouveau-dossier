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