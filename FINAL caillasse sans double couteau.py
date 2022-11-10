#on admet l'existance d'une fonction randint qui retourne un int aléatoire entre les deux int donnés en paramètres inclus
#on admet l'existance d'une fonction input qui retourne une chaine de caractères mise en paramètre et demande à l'utilisateur d'écrire quelque chose et le retourne sous forme d'une chaine de caractères 
#on défini une fonction shifumi qui ne prend aucun paramètre
    #on défini une liste scores de longueur 2 avec 0 et 0 comme valeurs
    #on défini une liste listChoices qui contien les choix possibles "caillou", "papyrus", "cisailles", "caillou" (le second caillou sera utile plus tard)
    #on défini une variable choixOrdi (qui representera le caractere choisi par l'ordinateur), et lui assigne la valeur 0
    #on défini une variable choixJoueur (qui representera le caractere choisi par l'ordinateur), et lui assigne la valeur d'un str vide
    #on défini une variable isPlaying (défini si le jeu est joué ou non), et lui assigne la valeur 1
    #tant que isPlaying est égal à 1 (tant que le jeu est joué)
        #alors on assigne à l'ordi la valeur du retour d'un appel de la fonction randint avec 0 et 2 en paramètres
        #on assigne à la variable choixJoueur le retour de l'execution de la fonction input avec "caillou, papyrus, cisaille ou stop" en paramètre
        #on vérifie que choixJoueur soit bien un str qui contient uniquement "caillou", "papyrus", "cisaille" ou "stop"
        #si choixJoueur est égal à "stop"
            #alors on affiche que la partie est terminée et la liste scores
            #on stop la boucle
        #si choixJoueur est égal à listChoices à l'indice choixOrdi
            #alors on affiche listChoices à l'indice choixOrdi
            #on affiche "draw"
        #sinon si choixJoueur est égal listChoices à l'indice (choixOrdi + 1)
            #alors on affiche listChoices à l'indice choixOrdi
            #on affiche que le joueur gagne
            #on incrémente la valeur de ls scores à l'indice 0
            #on affiche la liste scores
        #sinon
            #alors on affiche listChoices à l'indice choixOrdi
            #on affiche que le joueur perd
            #on incrémente la valeur de score à l'indice 1
            #on affiche la liste scores