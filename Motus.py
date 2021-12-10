import random

from colorama import Fore, Back, Style

import time

ListeDeMots = ["montre", "maison", "raison", "manger", "saumon", "cinema", "ragout", "prison", "proche", "breton"]

MotAuHasard = random.choice(ListeDeMots)
MotStock = ""

for i in range(len(MotAuHasard)):
    if MotAuHasard[i] == MotAuHasard[0]:
        MotStock = MotStock + MotAuHasard[i]
        print(Back.RED + MotStock[0]+ Style.RESET_ALL, end=" ")
        time.sleep(0.5)
    else:
        MotStock = MotStock + " _"
        print(" _", end=" ")
        time.sleep(0.5)



tentatives = 8
while MotStock != MotAuHasard :
    if tentatives == 0:
        print("Vous avez perdu...")
        quit()
    MotJoueur = input("à quel mot pensez vous?")
    MotStock = MotJoueur
    
    for i in range(len(MotAuHasard)):
        
        if MotJoueur[i] == MotAuHasard[i]:
            print(Back.RED + MotJoueur[i]+ Style.RESET_ALL, end=" ")
            time.sleep(0.5)
        elif MotJoueur[i] != MotAuHasard[i]:
            print(Back.BLUE + MotJoueur[i]+ Style.RESET_ALL, end=" ")
            time.sleep(0.5)
        if MotJoueur != MotAuHasard:
            tentatives = tentatives-1
if MotStock == MotAuHasard:
    print ("Bien joué, vous avez gagné!")

