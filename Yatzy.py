import random

tärningar = []

for i in range(5):
    # lägg till slumptal, 1 till 6, i listan tärningar
    tärningar.append(random.randint(1,6))

print("välj: ")
print("1 ettor")
print("2 tvåor")
print("3 treor")
print("4 fryror")
print("5 femmor")
print("6 sexor")
print("7 par")
print("8 tvåpar")
print("9 tretal")
print("10 fyrtal")
print("11 kåk")
print("12 liten stege")
print("13 stor stege")
print("15 chans")
print("16 yatzy")

print(tärningar)
print("summa", sum(tärningar))



# fungerar inte om vi vill ändra på värden i listan
for tärning in tärningar:
    tärning = 5 - tärning

print(tärningar)