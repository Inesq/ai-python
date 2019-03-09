import datetime
import random
import math
import statistics

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
srednia = suma/30
print("srednia wektora: ", srednia)
#odchylenie standard
odchylenieStandardowe = statistics.stdev(numbers)
# wektor znormalizowany
wektorZnormalizowany = []
for x in range(0, 29):
    wZ = (numbers[x]-najmniejsza)/(najwieksza-najmniejsza)
    wektorZnormalizowany.append(wZ)
for x in range(0, 29):
    print(wektorZnormalizowany[x])
#wektor standaryzowany
wektorStandaryzowany = []
for x in range(0, 29):
    wS = (numbers[x]-srednia)/odchylenieStandardowe
    wektorStandaryzowany.append(wS)
for x in range(0, 29):
    print(wektorStandaryzowany[x])
