#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pyeasyga import pyeasyga

data = [1, 4, 6, 11, 13, 20, 35]

ga = pyeasyga.GeneticAlgorithm(data, maximise_fitness=False)

def fitness(individual, data):
    sum1 = 0
    sum2 = 0
    for i in range(len(individual)):
        if individual[i] == 0:
            sum1 += data[i]
        else:
            sum2 += data[i]
    return abs(sum1 - sum2)

ga.fitness_function = fitness
ga.run()
print(ga.best_individual())


# In[ ]:




