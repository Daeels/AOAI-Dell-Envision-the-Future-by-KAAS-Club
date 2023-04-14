#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn.neighbors import KernelDensity
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.stats import norm
import random as r
import math
import pickle 
import os.path
from sklearn import preprocessing
from sklearn.tree import DecisionTreeClassifier 
from sklearn.metrics import * 
from sklearn.model_selection import train_test_split
from pickled.pickled import *


# In[2]:


#Mecanique
coord_meca = unpickled("coord_meca")
print(coord_meca[:,:10].shape)


# In[3]:


#Normalisation
Y_meca = unpickled("Y_meca")
values_meca = Y_meca.values #returns a numpy array
values_meca = values_meca.reshape(-1, 1)
min_max_scaler_meca = preprocessing.MinMaxScaler()
scaled = min_max_scaler_meca.fit_transform(values_meca)
pickled(min_max_scaler_meca,"min_max_scaler_meca")
Y_meca = pd.DataFrame(scaled)
print(Y_meca)


# In[4]:


Y_meca = np.array(Y_meca).ravel()
print(Y_meca)
encoded = Y_meca


# In[5]:


#print(coord_meca[:,:10])
coord_meca[:,:10] = coord_meca[:,:10].astype('float')
X_meca_train, X_meca_test, Y_meca_train, Y_meca_test = train_test_split(coord_meca[:,:10],encoded,test_size=0.2)
#print(type(X_meca_train),type(Y_meca_train),type(X_meca_test),type(Y_meca_test))


# In[6]:


#X_indus_test[0].reshape(-1, 1).T


# In[7]:


from sklearn.ensemble import RandomForestRegressor
clf_meca = RandomForestRegressor(n_estimators=100)
clf_meca.fit(X_meca_train, np.array(Y_meca_train))  
# print("Results Using Random Forest:") 
pickled(clf_meca,"clf_meca")
y_pred_forest = clf_meca.predict(X_meca_test[0].reshape(-1, 1).T) 
print(y_pred_forest)
print(Y_meca_test[0])
# print("Confusion Matrix: ",confusion_matrix(np.array(Y_meca_test), y_pred_forest))      
# print ("Accuracy : ",accuracy_score(np.array(Y_meca_test),y_pred_forest)*100) 
# print(clf.score(X_meca_test,Y_meca_test))


# In[8]:


score_train = float("{:.2f}".format(clf_meca.score(X_meca_train, Y_meca_train)))
print(score_train)


# In[9]:


score_test = float("{:.2f}".format(clf_meca.score(X_meca_test, Y_meca_test)))
print(score_test)

