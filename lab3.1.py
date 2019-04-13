#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

iris = datasets.load_iris()

x = iris.data
y = iris.target
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.4)


def my_iris_classifier(db):
    predictions = []
    for db_record in db:
        if db_record[3] < 1.0:
            predictions.append(0)
        elif db_record[2] < 5:
            predictions.append(1)
        else:
            predictions.append(2)
    return predictions


classifier_predictions = my_iris_classifier(x_test)
print(accuracy_score(y_test, classifier_predictions))


# In[ ]:




