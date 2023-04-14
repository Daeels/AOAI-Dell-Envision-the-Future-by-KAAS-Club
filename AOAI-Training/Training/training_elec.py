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


#Electrique
coord_elec = unpickled("coord_elec")
print(coord_elec[:,:10].shape)


# In[3]:


#Normalisation
Y_elec = unpickled("Y_elec")
values_elec = Y_elec.values #returns a numpy array
values_elec = values_elec.reshape(-1, 1)
min_max_scaler_elec = preprocessing.MinMaxScaler()
scaled = min_max_scaler_elec.fit_transform(values_elec)
pickled(min_max_scaler_elec,"min_max_scaler_elec")
Y_elec = pd.DataFrame(scaled)
print(Y_elec)


# In[4]:


Y_elec = np.array(Y_elec).ravel()
print(Y_elec)
encoded = Y_elec


# In[5]:


#print(coord_elec[:,:10])
coord_elec[:,:10] = coord_elec[:,:10].astype('float')
X_elec_train, X_elec_test, Y_elec_train, Y_elec_test = train_test_split(coord_elec[:,:10],encoded,test_size=0.2)
#print(type(X_elec_train),type(Y_elec_train),type(X_elec_test),type(Y_elec_test))


# In[6]:


from sklearn.ensemble import RandomForestRegressor
clf_elec = RandomForestRegressor(n_estimators=100)
clf_elec.fit(X_elec_train, np.array(Y_elec_train))  
# print("Results Using Random Forest:") 
pickled(clf_elec,"clf_elec")
y_pred_forest = clf_elec.predict(X_elec_test[0].reshape(-1, 1).T) 
print(y_pred_forest)
print(Y_elec_test[0])
# print("Confusion Matrix: ",confusion_matrix(np.array(Y_elec_test), y_pred_forest))      
# print ("Accuracy : ",accuracy_score(np.array(Y_elec_test),y_pred_forest)*100) 
# print(clf.score(X_elec_test,Y_elec_test))


# In[7]:


score_train = float("{:.2f}".format(clf_elec.score(X_elec_train, Y_elec_train)))
print(score_train)


# In[8]:


score_test = float("{:.2f}".format(clf_elec.score(X_elec_test, Y_elec_test)))
print(score_test)

