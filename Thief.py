#!/usr/bin/env python
# coding: utf-8

# In[2]:


from pyeasyga import pyeasyga
import matplotlib.pyplot as plt
import time
import random2 as random

data1 = {
    "items": [[19, 39, 30, 40, 23, 16, 14, 38, 11, 37],
              [18, 46, 15, 41, 31, 30, 32, 42, 32, 11]],
    "limit": 120,
    "min": 140
}
data2 = {
    "items": [[42, 50, 34, 44, 18, 27, 21, 12, 31, 25, 34, 50, 32, 29, 36, 6, 11, 40, 36, 25],
              [50, 46, 30, 21, 34, 41, 43, 35, 7, 29, 41, 2, 14, 10, 12, 34, 45, 6, 47, 6]],
    "limit": 240,
    "min": 400
}
data3 = {
    "items": [[88, 18, 86, 89, 90, 58, 93, 32, 89, 90, 75, 75, 24, 85, 35, 25, 97, 71, 15, 82, 87, 33, 3, 3, 98, 87, 81,
               49, 14, 70],
              [55, 68, 73, 3, 27, 26, 24, 57, 43, 89, 43, 40, 3, 1, 54, 29, 99, 66, 53, 41, 34, 72, 14, 21, 75, 44, 87,
               56, 7, 69]],
    "limit": 350,
    "min": 800
}
data4 = {
    "items": [[72, 6, 83, 78, 39, 11, 57, 5, 17, 24, 34, 95, 43, 33, 79, 46, 56, 6, 86, 81, 60, 2, 74, 44, 81, 18, 47,
               15, 72, 84, 4, 34, 40, 94, 15, 82, 17, 55, 96, 70],
              [29, 71, 53, 73, 32, 66, 26, 90, 60, 53, 15, 28, 5, 60, 11, 67, 35, 83, 25, 93, 40, 24, 81, 96, 100, 76,
               60, 15, 38, 61, 38, 26, 92, 31, 42, 57, 66, 92, 97, 86]],
    "limit": 450,
    "min": 850
}
data5 = {
    "items": [[177, 120, 33, 167, 122, 29, 26, 46, 148, 85, 98, 139, 28, 5, 37, 46, 63, 26, 132, 184, 145, 200, 190, 41,
               93, 66, 12, 146, 170, 41, 43, 162, 62, 170, 60, 42, 154, 151, 90, 169, 160, 147, 26, 39, 70, 71, 169, 47,
               110, 111, 15, 121, 169, 153, 47, 130, 59, 10, 169, 163],
              [174, 28, 181, 116, 39, 78, 22, 86, 110, 48, 4, 142, 36, 173, 105, 121, 145, 131, 4, 45, 9, 97, 114, 98,
               164, 14, 135, 166, 200, 69, 193, 172, 107, 122, 10, 75, 83, 162, 27, 185, 62, 112, 154, 192, 139, 147, 9,
               10, 152, 108, 105, 27, 85, 57, 168, 46, 73, 18, 82, 57]],
    "limit": 1000,
    "min": 2000
}

def mapData(data):
    output = []
    for i in range(len(data["items"][0])):
        output.append(
            {"value": data["items"][0][i], "weight": data["items"][1][i], "limit": data["limit"]})
    return output

def fitness(individual, data):
    fitness = 0
    value = 0
    weight = 0
    limit = data[0]["limit"]
    for (selected, item) in zip(individual, data):
        if selected:
            value += item["value"]
            weight += item["weight"]
    if weight <= limit:
        fitness = value
    return fitness

def create_individual(data):
    return [low_weight_random() for _ in range(len(data))]

def low_weight_random():
    randint = random.randint(0, 5)
    if randint < 4:
        return 0
    else:
        return 1

start = time.time()
ga1 = pyeasyga.GeneticAlgorithm(mapData(data1), population_size=50,
                                generations=50,
                                crossover_probability=0.9,
                                mutation_probability=0.1,
                                elitism=True,
                                maximise_fitness=True)
ga1.create_individual = create_individual
ga1.fitness_function = fitness
ga1.run()
print(ga1.best_individual())
end = time.time()
time1 = end - start
print(time1)

start = time.time()
ga2 = pyeasyga.GeneticAlgorithm(mapData(data2), population_size=100,
                                generations=100,
                                crossover_probability=0.9,
                                mutation_probability=0.1,
                                elitism=True,
                                maximise_fitness=True)
ga2.create_individual = create_individual
ga2.fitness_function = fitness
ga2.run()
print(ga2.best_individual())
end = time.time()
time2 = end - start
print(time2)

start = time.time()
ga3 = pyeasyga.GeneticAlgorithm(mapData(data3), population_size=500,
                                generations=100,
                                crossover_probability=0.9,
                                mutation_probability=0.1,
                                elitism=True,
                                maximise_fitness=True)
ga3.create_individual = create_individual
ga3.fitness_function = fitness
ga3.run()
print(ga3.best_individual())
end = time.time()
time3 = end - start
print(time3)

start = time.time()
ga4 = pyeasyga.GeneticAlgorithm(mapData(data4), population_size=500,
                                generations=100,
                                crossover_probability=0.9,
                                mutation_probability=0.1,
                                elitism=True,
                                maximise_fitness=True)
ga4.create_individual = create_individual
ga4.fitness_function = fitness
ga4.run()
print(ga4.best_individual())
end = time.time()
time4 = end - start
print(time4)

start = time.time()
ga5 = pyeasyga.GeneticAlgorithm(mapData(data5), population_size=500,
                                generations=200,
                                crossover_probability=0.9,
                                mutation_probability=0.1,
                                elitism=True,
                                maximise_fitness=True)
ga5.create_individual = create_individual
ga5.fitness_function = fitness
ga5.run()
print(ga5.best_individual())
end = time.time()
time5 = end - start
print(time5)

len1 = len(data1["items"][0])
len2 = len(data2["items"][0])
len3 = len(data3["items"][0])
len4 = len(data4["items"][0])
len5 = len(data5["items"][0])
x = [len1, len2, len3, len4, len5]
y = [time1, time2, time3, time4, time5]

plt.plot(x, y, color="blue", linewidth=1.0, linestyle="-")

plt.xlabel('liczba przedmiotów')
plt.ylabel('czas')
plt.title('Wykres ilosci do czasu')
plt.grid(True)

plt.show()


# In[ ]:




