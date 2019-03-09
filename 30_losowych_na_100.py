
import random

numbers = []
for x in range(0, 29):
    randomNumber = random.randrange(100)
    numbers.append(randomNumber)
for x in range(0, 29):
    print(numbers[x])