#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pickle 
import os
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.neighbors import KernelDensity
import matplotlib.pyplot as plt
from scipy.stats import norm
import random as r
import math
import pickle 
from sklearn import preprocessing
from sklearn.tree import DecisionTreeClassifier 
from sklearn.metrics import * 
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from pickled.pickled import *


# In[3]:


def ACP_indus(ANALYSE1,ANALYSE2,ALGEBRE2,PROCEFABRICDESSINTECHN,ANALYSEDESCIRCUIOPTIQ,ALGEBRE1,CHIMIE,ELECTRICITE,THERMODYNAMIQUE,LANGUES,TECHNIDEXPRESSCOMMU1,Mecaniquedupoint,ELECTROMAGNETISME,ELECTRONIQUE,ANALYSNUMERPROBSTAT,ALGORITHMIQUEPROGRAMMA,BASEDELACONCEPTION,TECHNOMETALLETTHERMO,TECHNIDOCPRODDOCENTR,DAOETOUTILSDEMATLAB,ALGEBRE3,MECANIQUEDUSOLIDE,TECHNDEXPREETDECOMM,MOYENNE) :
    X_indus = unpickled("X_indus")
    X_indus.loc[X_indus.index[-1] + 1] = ([ANALYSE1,ANALYSE2,ALGEBRE2,PROCEFABRICDESSINTECHN,ANALYSEDESCIRCUIOPTIQ,ALGEBRE1,CHIMIE,ELECTRICITE,THERMODYNAMIQUE,LANGUES,TECHNIDEXPRESSCOMMU1,Mecaniquedupoint,ELECTROMAGNETISME,ELECTRONIQUE,ANALYSNUMERPROBSTAT,ALGORITHMIQUEPROGRAMMA,BASEDELACONCEPTION,TECHNOMETALLETTHERMO,TECHNIDOCPRODDOCENTR,DAOETOUTILSDEMATLAB,ALGEBRE3,MECANIQUEDUSOLIDE,TECHNDEXPREETDECOMM,MOYENNE])
    #Matrice de Correlation
    R_indus = np.corrcoef(X_indus.values,rowvar=False)
    #Moyennes
    moyennes_indus = np.mean(X_indus.values,axis=0)
    #vecteur écart-type
    s_indus=np.std(X_indus.values,axis=0)
    #centrage et réduction 
    Z_indus=(X_indus.values-moyennes_indus)/s_indus
    #calcul des valeurs propres
    acp = PCA()
    #coordonnées factorielles
    coord_indus = acp.fit_transform(Z_indus)
    X = coord_indus[-1,:10]
    return X   


# In[4]:


def train_indus(X) :
    #Industriel
    coord_indus = unpickled("coord_indus")
    #Normalisation
    min_max_scaler_indus = unpickled("min_max_scaler_indus")
    clf_indus = unpickled("clf_indus")
    y_pred = clf_indus.predict(X.reshape(-1, 1).T) 
    y_pred = str(float("{:.2f}".format(y_pred[0]*100))) + "%"
    return y_pred


# In[5]:


X = ACP_indus(10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10) 
print(X)


# In[14]:


y_pred = train_indus(X)
print(y_pred[0]*100)
y_pred = str(float("{:.2f}".format(y_pred[0]*100))) + "%"
print(y_pred)

