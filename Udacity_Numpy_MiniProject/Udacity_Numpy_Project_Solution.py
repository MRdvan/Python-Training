# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 19:45:45 2021

@author: punti
"""

import numpy as np

# Create a 1000 x 20 ndarray with random integers in the half-open interval [0, 5001).
X = np.random.rand(1000,20)*5000

# print the shape of X
print("dataset shape:",X.shape)
#%%

# Calculate mean normalization formula : i = (i-m)/std 

# Average of the values in each column of X
X_avarage = X.mean(0)
# Standard Deviation of the values in each column of X
X_std = X.std(0)

# Print the shape of ave_cols
print("X_avarage's shape:" ,X_avarage.shape)
# Print the shape of std_cols
print("X_std's shape:" ,X_std.shape)
#%%

# Create a copy of dataset X
X_norm = X.copy()

# Mean normalize X
# Iterate through the columns of X_norm and calculate mean normalization with [i = (i-m)/std]
for each in np.arange(X_norm.shape[1]):
    X_norm[:,each] = (X_norm[:,each]-X_avarage[each])/X_std[each]


# Print the average of all the values of X_norm
X_norm_avarage = X_norm.mean()
print("X_norm avarage :",X_norm_avarage)

# Print the average of the minimum value in each column of X_norm
X_norm_min = X_norm.min()
print("X_norm min :",X_norm_min)

# Print the average of the maximum value in each column of X_norm
X_norm_max = X_norm.max()
print("X_norm max :",X_norm_max)

#%%

#Data Separation

# 1) A Training Set : 60%
# 2) A Cross Validation Set : 20%
# 3) A Test Set : %20

# We create X_perm by taking permutation of 0 to our X_norm'row number(1000)
row_indices = np.random.permutation(X_norm.shape[0])
X_perm = X_norm[row_indices,:]

# Split X_perm into three parts (X_train,X_cross,X_test)
X_perm_split = np.vsplit(X_perm, (600,800))

# Create a Training Set: (0 to 600)
X_train = X_perm_split[0]
# Create a Cross Validation Set : (600 to 800)
X_cross = X_perm_split[1]
# Create a Test Set: (800 to 1000)
X_test = X_perm_split[2]


# Print the shape of X_train
print("X_train shape:" ,X_train.shape)

# Print the shape of X_cross
print("X_cross shape:" ,X_cross.shape)

# Print the shape of X_test
print("X_test shape:" ,X_test.shape)


