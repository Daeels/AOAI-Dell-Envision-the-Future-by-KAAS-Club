#!/usr/bin/env python
# coding: utf-8

# 24                 
# filière  moyenneS1(cycle ing)   confidence	 insertionSatisfaction	relatedToField	  conditions  salaire  moyenne(cycle prepa)
# 

# In[1]:


import pandas as pd
import numpy as np
import pickle 
import os.path
from pickled.pickled import *


# In[2]:


dataFrame = pd.read_csv('dodo.csv',header=None)


# In[3]:


dataFrame


# In[4]:


for i in range(10000) :
    dataFrame.loc[i,23] = int(round(dataFrame.loc[i,23],0))
    if(dataFrame.loc[i,23] == 3) :
        dataFrame.loc[i,23] = 2
    if(dataFrame.loc[i,23] == -1) :
        dataFrame.loc[i,23] = 0
    for j in range(25,30) :
        dataFrame.loc[i,j] = round(dataFrame.loc[i,j])
        if dataFrame.loc[i,j] == 0 :
            dataFrame.loc[i,j] = 1
        if dataFrame.loc[i,j] == 6 :
            dataFrame.loc[i,j] = 5 


# In[5]:


#pd.set_option('display.max_rows', 5)
dataFrame


# In[6]:


#Description des statistiques sommaires
dataFrame.describe()
pickled(dataFrame,"dataFrame")


# In[7]:


X = dataFrame.loc[:,:24]
X = X.assign(MOYENNE=dataFrame.loc[:,30])
X = X.assign(OUTPUT=dataFrame.loc[:,24])
print(X)
#print(Y)


# In[8]:


X.drop(24,inplace=True,axis=1)
X.columns = ['ANALYSE 1','ANALYSE 2','ALGEBRE 2','PROCE FABRIC/DESSIN TECHN','ANALYSE DES CIRCUI /OPTIQ','ALGEBRE 1','CHIMIE','ELECTRICITE','THERMODYNAMIQUE','LANGUES','TECHNI D\'EXPRESS & COMMU1','Mécanique du point','ELECTROMAGNETISME','ELECTRONIQUE','ANALYS NUMER /PROB & STAT','ALGORITHMIQUE & PROGRAMMA','BASE DE LA CONCEPTION','TECHNO/METALL ET THERMO','TECHNI DOC /PROD DOC/ENTR','DAO ET OUTILS DE MATLAB','ALGEBRE 3','MECANIQUE DU SOLIDE','TECHN D\'EXPRE ET DE COMM','FILIERE','MOYENNE','OUTPUT']
X.head()


# In[9]:


X_new = X.copy(deep=True)
X_new.drop(['FILIERE','OUTPUT'],inplace=True,axis=1)
X_new.head()


# In[10]:


R = np.corrcoef(X_new.values,rowvar=False)
#print(R_indus)
#Moyennes
moyennes = np.mean(X_new.values,axis=0)
print(moyennes)
#vecteur écart-type
s=np.std(X_new.values,axis=0)
#centrage et réduction 
Z=(X_new.values-moyennes)/s


# In[11]:


#Application de l'ACP
from sklearn.decomposition import PCA
acp = PCA()
#coordonnées factorielles
acp.fit(Z)


# In[12]:


pickled(acp,"acp")


# In[13]:


# X = unpickled("X")
# X.head()


# In[14]:


moyennes = np.mean(X,axis=0)
print(moyennes)


# In[15]:


X.head()


# In[16]:


#Diviser le dataset en trois parties
X_indus = X[X['FILIERE'] == 0]; X_meca = X[X['FILIERE'] == 1] ; X_elec = X[X['FILIERE'] == 2]
Y_indus = X_indus['OUTPUT'] ; Y_meca = X_meca['OUTPUT'] ; Y_elec = X_elec['OUTPUT']
X_indus.drop(columns=['OUTPUT','FILIERE'],inplace=True,axis=1); X_meca.drop(columns=['OUTPUT','FILIERE'],inplace=True,axis=1); X_elec.drop(columns=['OUTPUT','FILIERE'],inplace=True,axis=1)
print(X_indus.shape)
X_indus.head()


# In[17]:


pickled(X_indus,"X_indus")
pickled(X_meca,"X_meca")
pickled(X_elec,"X_elec")
pickled(Y_indus,"Y_indus")
pickled(Y_meca,"Y_meca")
pickled(Y_elec,"Y_elec")


# In[18]:


from sklearn import preprocessing
#Industriel
#Matrice de Correlation
R_indus = np.corrcoef(X_indus.values,rowvar=False)
#print(R_indus)
#Moyennes
moyennes_indus = np.mean(X_indus.values,axis=0)
print(moyennes_indus)
#vecteur écart-type
s_indus=np.std(X_indus.values,axis=0)
#centrage et réduction 
Z_indus=(X_indus.values-moyennes_indus)/s_indus
print(Z_indus)


# In[19]:


#calcul des valeurs propres
pr_indus = np.linalg.eig(R_indus)
print(pr_indus)


# In[20]:


t = sorted(pr_indus[0],reverse=True)
v = t/sum(t)
w = np.cumsum(v)
t = [t,v,w]
print(pd.DataFrame(np.transpose(t),columns=['Val.P','%','cumsum %'],index=range(X_indus.shape[1])))


# In[21]:


#coordonnées factorielles
coord_indus = acp.transform(Z_indus)
#afficher les nouvelles coordonées
print(pd.DataFrame(coord_indus[:,:10],index=X_indus.index))


# In[22]:


pickled(coord_indus,"coord_indus")


# In[23]:


#Mécanique
#Matrice de Correlation
R_meca = np.corrcoef(X_meca.values,rowvar=False)
#print(R_meca)
#Moyennes
moyennes_meca = np.mean(X_meca.values,axis=0)
print(moyennes_meca)
#vecteur écart-type
s_meca=np.std(X_meca.values,axis=0)
#centrage et réduction 
Z_meca=(X_meca.values-moyennes_meca)/s_meca
print(Z_meca)
#calcul des valeurs propres
pr_meca = np.linalg.eig(R_meca)
print(pr_meca)
t = sorted(pr_meca[0],reverse=True)
v = t/sum(t)
w = np.cumsum(v)
t = [t,v,w]
print(pd.DataFrame(np.transpose(t),columns=['Val.P','%','cumsum %'],index=range(X_meca.shape[1])))
#coordonnées factorielles
coord_meca = acp.transform(Z_meca)
#afficher les nouvelles coordonées
print(pd.DataFrame(coord_meca[:,:10],index=X_meca.index))


# In[24]:


pickled(coord_meca,"coord_meca")


# In[25]:


#Electrique 
#Matrice de Correlation
R_elec = np.corrcoef(X_elec.values,rowvar=False)
#print(R_elec)
#Moyennes
moyennes_elec = np.mean(X_elec.values,axis=0)
print(moyennes_elec)
#vecteur écart-type
s_elec=np.std(X_elec.values,axis=0)
#centrage et réduction 
Z_elec=(X_elec.values-moyennes_elec)/s_elec
print(Z_elec)
#calcul des valeurs propres
pr_elec = np.linalg.eig(R_elec)
print(pr_elec)
t = sorted(pr_elec[0],reverse=True)
v = t/sum(t)
w = np.cumsum(v)
t = [t,v,w]
print(pd.DataFrame(np.transpose(t),columns=['Val.P','%','cumsum %'],index=range(X_elec.shape[1])))
#coordonnées factorielles
coord_elec = acp.transform(Z_elec)
#afficher les nouvelles coordonées
print(pd.DataFrame(coord_elec[:,:10],index=X_elec.index))


# In[26]:


pickled(coord_elec,"coord_elec")

