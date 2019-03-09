
import random

numbers = []
for x in range(0, 29):
    randomNumber = random.randrange(100)
    numbers.append(randomNumber)
najwieksza =0
najmniejsza = 100
for x in range(0, 29):
    if(numbers[x]>najwieksza):
        najwieksza=numbers[x]
    if(numbers[x]< najmniejsza):
            najmniejsza=numbers[x]
print("najmniejsza = ",najmniejsza," najwieksza = ", najwieksza)
numbers.sort()
suma = 0
for x in range(0, 29):
    suma = suma + numbers[x]
print("srednia wektora: ", suma/30)
wektorZnormalizowany = []
for x in range(0, 29):
    wZ = (numbers[x]-najmniejsza)/(najwieksza-najmniejsza)
    wektorZnormalizowany.append(wZ)
for x in range(0, 29):
    print(wektorZnormalizowany[x])
    


