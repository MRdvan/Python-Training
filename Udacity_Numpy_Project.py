# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 19:45:45 2021

@author: punti
"""

import numpy as np


# create random 1000x20 dataset

X = np.random.rand(1000,20)
X = X*5000
print(X.shape)

X_avarage = X.mean(0)
X_std = X.std(0)
print(X_avarage, X_std)

X_copy = X.copy()

for each in np.arange(X_copy.shape[1]):
    X_copy[:,each] = (X_copy[:,each]-X_avarage[each])/X_std[each]


X_copy_avarage = X_copy.mean()
X_copy_min = X_copy.min()
X_copy_max = X_copy.max()

#%%

row_indices = np.random.permutation(X_copy.shape[0])
X_perm = X_copy[row_indices,:]
train,cross,test = np.vsplit(X_perm, (600,800))
print(train.shape[0],cross.shape[0],test.shape[0])


