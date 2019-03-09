import  random
import math
vector1 = []
vector2 = []
for x in range(0, 9):
    randomNumber = random.randrange(20)
    vector1.append(randomNumber)
    randomNumber = random.randrange(20)
    vector2.append(randomNumber)
iloczynSkalarny=0
for x in range(0, 9):
    iloczynSkalarny = iloczynSkalarny + (vector1[x]*vector2[x])
print(iloczynSkalarny)
#dlugosci wektorow
dlugoscWektora1 = 0
dlugoscWektora2 = 0
for x in range(0, 9):
    dlugoscWektora1 = dlugoscWektora1 + (vector1[x]*vector1[x])
    dlugoscWektora2 = dlugoscWektora2 + (vector2[x] *vector2[x])
print("dlugosc wektora pierwszego: ", math.sqrt(dlugoscWektora1),  "drugiego: ", math.sqrt(dlugoscWektora2))
#cos
cos = iloczynSkalarny/(math.sqrt(dlugoscWektora1)*math.sqrt(dlugoscWektora2))
print("cos: ",cos)
stopnie = cos * 180 / math.pi
print(stopnie)
radiany = stopnie * math.pi / 180
print(radiany)
