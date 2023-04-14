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


#Industriel
coord_indus = unpickled("coord_indus")
print(coord_indus[:,:10].shape)


# In[3]:


#Normalisation
Y_indus = unpickled("Y_indus")
values_indus = Y_indus.values #returns a numpy array
values_indus = values_indus.reshape(-1, 1)
min_max_scaler_indus = preprocessing.MinMaxScaler()
scaled = min_max_scaler_indus.fit_transform(values_indus)
pickled(min_max_scaler_indus,"min_max_scaler_indus")
Y_indus = pd.DataFrame(scaled)
print(Y_indus)


# In[4]:


# Y_indus = np.array(Y_indus).ravel()
# enc = preprocessing.LabelEncoder()
# encoded = enc.fit_transform(Y_indus)
# print(encoded)


# In[5]:


Y_indus = np.array(Y_indus).ravel()
print(Y_indus)
encoded = Y_indus


# In[6]:


#print(coord_indus[:,:10])
coord_indus[:,:10] = coord_indus[:,:10].astype('float')
X_indus_train, X_indus_test, Y_indus_train, Y_indus_test = train_test_split(coord_indus[:,:10],encoded,test_size=0.2)
#print(type(X_indus_train),type(Y_indus_train),type(X_indus_test),type(Y_indus_test))


# In[7]:


#X_indus_test[0].reshape(-1, 1).T


# In[8]:


from sklearn.ensemble import RandomForestRegressor
clf_indus = RandomForestRegressor(n_estimators=100)
clf_indus.fit(X_indus_train, np.array(Y_indus_train))  
# print("Results Using Random Forest:") 
pickled(clf_indus,"clf_indus")
y_pred_forest = clf_indus.predict(X_indus_test[0].reshape(-1, 1).T) 
print(y_pred_forest)
print(Y_indus_test[0])
# print("Confusion Matrix: ",confusion_matrix(np.array(Y_indus_test), y_pred_forest))      
# print ("Accuracy : ",accuracy_score(np.array(Y_indus_test),y_pred_forest)*100) 
# print(clf.score(X_indus_test,Y_indus_test))


# In[9]:


score_train = float("{:.2f}".format(clf_indus.score(X_indus_train, Y_indus_train)))
print(score_train)


# In[10]:


score_test = float("{:.2f}".format(clf_indus.score(X_indus_test, Y_indus_test)))
print(score_test)

