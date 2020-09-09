# -*-coding:utf-8 -*

import os

def mult():

    def tableMultiplication(nbAMultiplier, nbMult):

        i = 0

        while i < nbMult + 1 :
            print(i , "*", nbAMultiplier, "= ", i * nbAMultiplier)
            i += 1


    nbAMultiplier = int(input("Quelle est la table de multiplication désirée ? "))
    nbMult = int(input("Entrez la limite du nombre de résultats désirés ? "))

    tableMultiplication(nbAMultiplier, nbMult)
