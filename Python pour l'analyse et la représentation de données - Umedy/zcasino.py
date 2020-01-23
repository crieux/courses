from math import *
from random import *

argent = -1
while argent <= 0:
    try:
        argent = int(input("Combien d'argent avez-vous ?"))
    except ValueError:
        print("Vous n'avez pas saisi un nombre")
    if argent <= 0:
        print("Vous devez saisir un nombre supérieur à 0")

while argent > 0:
    choix = -1
    while choix < 0 or choix >= 50:
        try:
            choix = int(input("Quelle case choisissez-vous ?"))
        except ValueError:
            print("Vous n'avez pas saisi un nombre.")
            choix = -1
        if choix < 0 or choix >= 50:
            print("Vous devez saisir un nombre compris entre 0 et 59 inclus.")
    mise = 0
    while mise == 0:
        try:
            mise = int(input("Combien misez-vous ?"))
        except ValueError:
            print("Vous n'avez pas saisi une nombre.")
            mise = 0
        if mise > argent:
            mise = 0
            print("Vous n'avez pas assez d'argent.")
    case = randrange(0, 50)
    argent = argent - mise
    if mise == case:
        print("* La bille tombe sur la case", case, "*")
        print("Bravo ! Vous remportez la mise !")
        argent = argent + (mise * 3)
    else:
        print("* La bille tombe sur la case", case, "*")
        modulo_choix = choix % 2
        modulo_case = case % 2
        if modulo_choix == modulo_case:
            print("Vous remportez la moitié de votre mise, arrondie au supérieur.")
            gain = mise/2
            if isinstance(gain, float):
                gain = ceil(gain) + 1
            argent = argent + gain
        else:
            print("Vous perdez votre mise.")
    print("Il vous reste", argent, "$")
