# Hänga Gubbe

import random
 
# Lista Av Sporter
Sporter = ["fotboll", "golf", "basket", "handboll", "cricket", "rugby", "badminton", "bowling", "tennis", "boxning", "dart", "hockey", "squash", "volleyboll", "taekwondo"]

ord = random.choice(Sporter)
hemligt_ord = []
for bokstav in ord:
    hemligt_ord.append("_ ")
print(hemligt_ord)
print()
# print _ _ _ _ _


omgångar = 6

# Början av spelet
while omgångar > 0 and "_ " in hemligt_ord:
    gissa = input("Gissa en bokstav :")
    # När man gissar rätt bokstav
    if gissa in ord:
        print ("Rätt")
        for index, bokstav in enumerate(ord):
            if bokstav == gissa:
                hemligt_ord[index] = (gissa)
        print(hemligt_ord)
    # När man gissar fel bokstav
    if gissa not in ord:
        for bokstav in ord:
            print('_ ', end='')
        omgångar = omgångar - 1
        print (f"Fel, Du har {omgångar} gissningar kvar")

# När man förlorar
if omgångar == 0:
    print(f"Du förlora. Ordet va '{ord}'")
else:
    print("Korrekt! Du vann!")