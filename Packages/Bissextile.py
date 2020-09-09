
# -*-coding:utf-8 -*

import os

def AnneeBissextile():


    annee = int(input("Veuillez entrer votre année :"))



    if annee % 4 != 0 or annee % 100 != 0 :
        bissextile = False

    else :
        if annee % 400 != 0 :
            bissextile = False
        else :
            bissextile = True

    if bissextile :
        print("L'année " + str(annee) + " est bissextile.")
    else :
        print("L'année " + str(annee) + " n'est pas bissextile.")