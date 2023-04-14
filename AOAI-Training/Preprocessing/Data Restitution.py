#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn.neighbors import *
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.stats import norm
import random as r
import math
from pickled import *


# In[2]:


data6 = pd.read_csv("filtered_2016.csv")
data7 = pd.read_csv("filtered_2017.csv")
data8 = pd.read_csv("filtered_2018_S1n.csv")

result = pd.merge(data6, data7, on="code")
merged_data = pd.merge(result, data8, on="code")

merged_data.to_csv('merged_all_data.csv')



merged_data = merged_data.drop(['code', 'Nature', 'Barem', 'Annee'], axis=1)


# In[3]:


def strong():
    return round((norm.cdf(r.uniform(0.4,2)) * 5) , 0)

def weak():
    return round((norm.cdf(r.uniform(-0.4,-1.69)) * 5) , 0) + 1


# In[4]:


data1 = merged_data.values
print(data1)
rev = np.zeros((len(data1),5))
f = 0
for i in range(len(data1)):
    mean = data1[i,0:-2].mean()
#     print(mean) 
    if mean < 11.5 :
        f = 1
    for j in range(5):
        
        if f == 1:
            if r.uniform(0,1) < 0.05:
                rev[i,j] = strong()

            else:
                rev[i,j] = weak()
        else:
            if r.uniform(0,1) < 0.05:
                rev[i,j] = weak()
            else:
                rev[i,j] = strong()
#         print(rev[i,j])    


# In[5]:


data1 = np.hstack((data1,rev))


# In[6]:


kde = KernelDensity(kernel='gaussian', bandwidth=0.25).fit(data1)
kde.get_params(deep=True)


# In[7]:


data = kde.sample(10000)
type(data)
np.savetxt('notes.csv', data, fmt='%5.3f', delimiter=',')


# In[8]:


o = []
for i in range(len(data)):
    o.append(data[i,0:-7].mean())
    
o = np.array(o);p=o.reshape((10000,1))
data = np.hstack((data,p))


# In[9]:


np.savetxt('dodo.csv', data, fmt='%5.3f', delimiter=',')

