#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import neighbors, tree
from sklearn.naive_bayes import GaussianNB
from sklearn.neural_network import MLPClassifier

iris = datasets.load_iris()
x = iris.data
y = iris.target
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.4)

classifier_decisionTree = tree.DecisionTreeClassifier()
classifier_decisionTree.fit(x_train, y_train)
print('DecisionTree ', accuracy_score(y_test, classifier_decisionTree.predict(x_test)))

classifier_kNeighbors = neighbors.KNeighborsClassifier(15)
classifier_kNeighbors.fit(x_train, y_train)
print('KNeighbors ', accuracy_score(y_test, classifier_kNeighbors.predict(x_test)))

classifier_NaiveBayes = GaussianNB()
classifier_NaiveBayes.fit(x_train, y_train)
print('Gaussian Naive Bayes ', accuracy_score(y_test, classifier_NaiveBayes.predict(x_test)))

classifier_MLP = MLPClassifier(solver='lbfgs', alpha=1e-5)
classifier_MLP.fit(x_train, y_train)
print('MLP ', accuracy_score(y_test, classifier_MLP.predict(x_test)))


# In[ ]:





# In[ ]:




