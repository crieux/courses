from fonctions import *

choix = 0

print("Labyrinthes existants :")
print("   1 - facile.")
print("   2 - prison.\n")

while choix == 0:
    try :
        choix = int(input("Entrez un numéro de labyrinthe pour commencer à jouer : "))
    except NameError:
        print("Vous n'avez pas saisi un choix valide.")
        choix = 0
    except ValueError:
        print("Vous n'avez pas saisi un choix valide.")
        choix = 0

print("")
carte = load(choix)
solution = 
print(carte)

