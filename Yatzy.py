import random

tärningar = []

for i in range(5):
    # lägg till slumptal, 1 till 6, i listan tärningar
    tärningar.append(random.randint(1,6))

print(tärningar)
print("min", min(tärningar))
print("max", max(tärningar))
print("summa", sum(tärningar))

# fungerar inte om vi vill ändra på värden i listan
for tärning in tärningar:
    tärning = 5 - tärning

print(tärningar)