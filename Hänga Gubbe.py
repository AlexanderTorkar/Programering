# Hänga Gubbe

import random
 
# Lista Av Sporter
Sporter = ["fotboll", "golf", "basket", "handboll", "cricket", "rugby", "badminton", "bowling", "tennis", "boxning", "dart", "hockey", "squash", "volleyboll", "taekwondo"]

ord = random.choice(Sporter)

omgångar = 6

while omgångar > 0:
    gissa = input("Gissa en bokstav")
    if gissa not in ord:
        print ("Fel")
        omgångar -=1 