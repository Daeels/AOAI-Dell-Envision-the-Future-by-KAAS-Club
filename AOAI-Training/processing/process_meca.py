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


def ACP_meca(ANALYSE1,ANALYSE2,ALGEBRE2,PROCEFABRICDESSINTECHN,ANALYSEDESCIRCUIOPTIQ,ALGEBRE1,CHIMIE,ELECTRICITE,THERMODYNAMIQUE,LANGUES,TECHNIDEXPRESSCOMMU1,Mecaniquedupoint,ELECTROMAGNETISME,ELECTRONIQUE,ANALYSNUMERPROBSTAT,ALGORITHMIQUEPROGRAMMA,BASEDELACONCEPTION,TECHNOMETALLETTHERMO,TECHNIDOCPRODDOCENTR,DAOETOUTILSDEMATLAB,ALGEBRE3,MECANIQUEDUSOLIDE,TECHNDEXPREETDECOMM,MOYENNE) :
    X_meca = unpickled("X_meca")
    X_meca.loc[X_meca.index[-1] + 1] = ([ANALYSE1,ANALYSE2,ALGEBRE2,PROCEFABRICDESSINTECHN,ANALYSEDESCIRCUIOPTIQ,ALGEBRE1,CHIMIE,ELECTRICITE,THERMODYNAMIQUE,LANGUES,TECHNIDEXPRESSCOMMU1,Mecaniquedupoint,ELECTROMAGNETISME,ELECTRONIQUE,ANALYSNUMERPROBSTAT,ALGORITHMIQUEPROGRAMMA,BASEDELACONCEPTION,TECHNOMETALLETTHERMO,TECHNIDOCPRODDOCENTR,DAOETOUTILSDEMATLAB,ALGEBRE3,MECANIQUEDUSOLIDE,TECHNDEXPREETDECOMM,MOYENNE])
    #Matrice de Correlation
    R_meca = np.corrcoef(X_meca.values,rowvar=False)
    #Moyennes
    moyennes_meca = np.mean(X_meca.values,axis=0)
    #vecteur écart-type
    s_meca=np.std(X_meca.values,axis=0)
    #centrage et réduction 
    Z_meca=(X_meca.values-moyennes_meca)/s_meca
    #calcul des valeurs propres
    acp = PCA()
    #coordonnées factorielles
    coord_meca = acp.fit_transform(Z_meca)
    X = coord_meca[-1,:10]
    return X   


# In[3]:


def train_meca(X) :
    #Mecanique
    coord_meca = unpickled("coord_meca")
    #Normalisation
    min_max_scaler_meca = unpickled("min_max_scaler_meca")
    clf_meca = unpickled("clf_meca")
    y_pred = clf_meca.predict(X.reshape(-1, 1).T) 
    y_pred = str(float("{:.2f}".format(y_pred[0]*100))) + "%"
    return y_pred


# In[4]:


X = ACP_meca(10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10) 
print(X)


# In[5]:


y_pred = train_meca(X)
print(y_pred)

