# -*-coding:utf-8 -*

import os

def TestDico():
    fruits = {"pommes":21, "melons":12, "bananes":53, "poires":112, "avocats":54}

    print(fruits)

    for cle in fruits.keys():
        print(cle)

    for values in fruits.values():
        print(values)

    for cle, values in fruits.items():
        print("La clé {} contient la valeur {}.".format(cle, values))

    def testFonctionParametresInconnusNommes(**param):
        print("La fonction a reçu les paramètres suivants : {}".format(param))

    testFonctionParametresInconnusNommes()
    testFonctionParametresInconnusNommes(fruits = 6, legumes = 8)
    testFonctionParametresInconnusNommes(epicerie = fruits)