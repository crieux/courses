import os
import re

def load(choix):
    if choix == 1:
        fichier = open("Cartes/facile.txt", "r")
    elif choix == 2:
        fichier = open("Cartes/prison.txt", "r")
    return (fichier.read())

def trouver_objet(carte, objet):
    x = 0
    while re.search(r".*"+objet+".*", data_split[x]) == None:
        x += 1
    y = data_split[i].index(objet)
    return (x, y)

