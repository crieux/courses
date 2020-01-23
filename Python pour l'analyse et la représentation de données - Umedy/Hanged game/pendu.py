import os
from fonctions import *

fichier_scores = open("scores", 'r')
scores = dict(fichier_scores.read())
fichier_scores.close()
nom = -1

while nom == -1:
    try:
        nom = str(input("Quel est votre nom ?"))
    except NameEroor:
        print("Vous n'avez pas saisi un nom.")
        name = -1
    except TypeError:
        print("Vous n'avez pas saisi un nom.")
        name = -1    

noms = scores.keys()
if nom in noms:
    score = scores[nom]
    print("Rebonjour", nom, "vous avez un score de", score, ", je choisi un mot...")
    mot = choisi_mot()
    score = jeu(mot)
    if score > 0:
        scores[nom] = scores[nom] + score
        fichier_scores = open("scores", 'w')
        fichier_scores.write(scores)
        fichier_scores.close()    
else:
    print("Bienvenue", nom, ", je choisi un mot...")
    mot = choisi_mot()
    score = jeu(mot)
    if score > 0:
        fichier_scores = open("scores", 'w')
        imprime = (str(nom) + str(" ") + str(score))
        fichier_scores.write(imprime)
        fichier_scores.close()
    
print("A bientôt !")
