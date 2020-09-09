# -*-coding:utf-8 -*

import os
import Packages.Bissextile as Bissextile
import Packages.TableMultiplication as Mult
import Packages.Casino as Casino
import Packages.TestDictionnaire as Dico

stop = False

while stop == False :

    print("Liste des choix : ")
    print("1 : Test des années bissextiles ")
    print("2 : Table de multiplication ")
    print("3 : Jeu de Roulette ")
    print("4 : Test des dictionnaires Python")
    print("5 : Arréter le programme ")

    choice = int(input("Choisissez ce que vous voulez exécuter : "))

    if choice == 1:
        Bissextile.AnneeBissextile()

    if choice == 2:
        Mult.mult()

    if choice == 3:
        Casino.Roulette()

    if choice == 4:
        Dico.TestDico()

    if choice == 5:
        stop = True

