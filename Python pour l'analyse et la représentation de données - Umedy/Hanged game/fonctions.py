from donnees import *
from random import *

def choisi_mot():
    global liste_mots
    mot = liste_mots[randrange(0, len(liste_mots))]
    return str(mot)

def jeu(mot):
    score = 0
    global nb_coups
    coup = 0
    print("C'est bon, j'ai choisi, à vous de deviner !")
    answer = list("_" * len(mot))
    print(answer)
    solution = list(mot)
    while solution != answer and coup <= nb_coups:
        lettre = int(-1)
        while lettre == -1:
            try:
                lettre = str(input("Entrez une lettre :"))
            except NameError:
                print("Vous n'avez pas saisi une lettre.")
                lettre = -1
            except TypeError:
                print("Vous n'avez pas saisi une lettre.")
                lettre = -1
        if lettre in solution:
            print("Bien joué ! Vous avez trouvé la lettre", lettre)
            index = solution.index(lettre)
            answer[index] = lettre
            print(answer)
            coup += 1
            print("Il reste", nb_coups - coup, "coups.")
        else:
            print("La lettre", lettre, "n'est pas dans la solution.")            
            coup += 1
            print("Il reste", nb_coups - coup, "coups.")
    if coup <= nb_coups:
        score = nb_coups - coup
        print("Bien joué ! Vous avez gagné", score, "points.")
    else:
        print("Vous avez perdu...")
    return(score)
            
