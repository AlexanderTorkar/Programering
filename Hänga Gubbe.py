# Hänga Gubbe

import random
 
# Lista Av Sporter
Sporter = ["fotboll", "golf", "basket", "handboll", "cricket", "rugby", "badminton", "bowling", "tennis", "boxning", "dart", "hockey", "squash", "volleyboll", "taekwondo"]

ord = random.choice(Sporter)
for bokstav in ord:
    print('_ ', end='')
print()
# print _ _ _ _ _



omgångar = 6

# Början av spelet
while omgångar > 0:
    gissa = input("Gissa en bokstav")
    # När man gissar rätt bokstav
    if gissa in ord:
        print (bokstav)
        print ("Rätt")
    # När man gissar fel bokstav
    if gissa not in ord:
        print ("Fel")
        omgångar = omgångar - 1
# När man förlorar
if omgångar == 0:
    print("Du förlora")