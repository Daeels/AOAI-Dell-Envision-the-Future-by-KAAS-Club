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
def pickled(variable,string) :
    directory = os.path.join("pickled",string+".pickle")
    pickle_out = open(directory,"wb")
    pickle.dump(variable,pickle_out)
    pickle_out.close()
def unpickled(string) :
    directory = os.path.join("pickled",string+".pickle")
    pickle_in = open(directory,"rb")
    variable = pickle.load(pickle_in)
    return variable


# In[2]:


def ACP_elec(ANALYSE1,ANALYSE2,ALGEBRE2,PROCEFABRICDESSINTECHN,ANALYSEDESCIRCUIOPTIQ,ALGEBRE1,CHIMIE,ELECTRICITE,THERMODYNAMIQUE,LANGUES,TECHNIDEXPRESSCOMMU1,Mecaniquedupoint,ELECTROMAGNETISME,ELECTRONIQUE,ANALYSNUMERPROBSTAT,ALGORITHMIQUEPROGRAMMA,BASEDELACONCEPTION,TECHNOMETALLETTHERMO,TECHNIDOCPRODDOCENTR,DAOETOUTILSDEMATLAB,ALGEBRE3,MECANIQUEDUSOLIDE,TECHNDEXPREETDECOMM,MOYENNE) :
    X_elec = unpickled("X_elec")
    X_elec.loc[X_elec.index[-1] + 1] = ([ANALYSE1,ANALYSE2,ALGEBRE2,PROCEFABRICDESSINTECHN,ANALYSEDESCIRCUIOPTIQ,ALGEBRE1,CHIMIE,ELECTRICITE,THERMODYNAMIQUE,LANGUES,TECHNIDEXPRESSCOMMU1,Mecaniquedupoint,ELECTROMAGNETISME,ELECTRONIQUE,ANALYSNUMERPROBSTAT,ALGORITHMIQUEPROGRAMMA,BASEDELACONCEPTION,TECHNOMETALLETTHERMO,TECHNIDOCPRODDOCENTR,DAOETOUTILSDEMATLAB,ALGEBRE3,MECANIQUEDUSOLIDE,TECHNDEXPREETDECOMM,MOYENNE])
    #Matrice de Correlation
    R_elec = np.corrcoef(X_elec.values,rowvar=False)
    #Moyennes
    moyennes_elec = np.mean(X_elec.values,axis=0)
    #vecteur écart-type
    s_elec=np.std(X_elec.values,axis=0)
    #centrage et réduction 
    Z_elec=(X_elec.values-moyennes_elec)/s_elec
    #calcul des valeurs propres
    acp = PCA()
    #coordonnées factorielles
    coord_elec = acp.fit_transform(Z_elec)
    X = coord_elec[-1,:10]
    return X   


# In[3]:


def train_elec(X) :
    #Mecanique
    coord_elec = unpickled("coord_elec")
    #Normalisation
    min_max_scaler_elec = unpickled("min_max_scaler_elec")
    clf_elec = unpickled("clf_elec")
    y_pred = clf_elec.predict(X.reshape(-1, 1).T) 
    y_pred = str(float("{:.2f}".format(y_pred[0]*100))) + "%"
    return y_pred


# In[4]:


X = ACP_elec(10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10) 
print(X)


# In[5]:


y_pred = train_elec(X)
print(y_pred)

