# -*-coding:utf-8 -*

import os
from math import ceil
from random import randrange

def Roulette():

    gameOver = False
    money = 100

    while gameOver == False:

        print("Vous avez ", money, " euros")

        enoughMoney = False

        bouleNumber = int(input("Veuillez entrer le numéro que vous désirez jouer (entre 0 et 49) : "))



        while enoughMoney == False:
            mise = int(input("Veuillez entrer la somme que vous désirez miser : "))
            
            if money >= mise:
                enoughMoney = True
            else:
                print("Vous n'avez pas assez d'argent!!!")


        result = randrange(50)


        money = ceil(money - mise)

        if bouleNumber == result:
            money = ceil(money + mise*3)
            print("Vous avez trouvé! Vous gagnez" , (mise*3) , " euros. Votre solde est de " , money , " euros.")
        else:
            print("Vous avez perdu. Le bon numéro était le ", result)

            if money <= 0:
                print("Game Over")
                gameOver = True

        os.system("pause")
           
