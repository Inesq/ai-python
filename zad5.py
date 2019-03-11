import random
import numpy as np
import math


def vec_scal(x, y):
    return np.dot(x, y)


def vec_len(x):
    x_len = 0
    for i in range(0, 10):
        x_len += x[i]**2
    return math.sqrt(x_len)

def vec_cos(x, y):
    return vec_scal(x, y)/(vec_len(x)*vec_len(y))


def vec_ang_rad(x, y):
    return math.acos(vec_cos(x, y))


def vec_ang_deg(x, y):
    return math.degrees(vec_ang_rad(x, y))


vector_one = []
vector_two = []

for i in range(0, 10):
    random_number = random.randrange(20)
    vector_one.append(random_number)

for i in range(0, 10):
    random_number = random.randrange(20)
    vector_two.append(random_number)

print('Wektor pierwszy: %s' % vector_one)
print('Wektor drugi: %s' % vector_two)

print('Iloczyn skalarny: %s' % vec_scal(vector_one, vector_two))
print('Długość wektora pierwszego: %s' % vec_len(vector_one))
print('Długość wektora drugiego: %s' % vec_len(vector_two))
print('Cosinus kąta między wektorami: %s' % vec_cos(vector_one, vector_two))
print('Kąt w radianach: %s' % vec_ang_rad(vector_one, vector_two))
print('Kąt w stopniach: %s' % vec_ang_deg(vector_one, vector_two))