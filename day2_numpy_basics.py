# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 09:05:49 2020

@author: anshu
"""

'''
Numpy - mathematical computing
'''
x = [4,5,3]
y = [3,2,8]

print(x+y)

import numpy as np
x = np.array([7,2,6])
y = np.array([6,3,4])
print(x+y)

x = np.array([7.0,2,6,8,'3'])
x.dtype
print(x)

x = np.array([[7,5,3],
              [3,2,6],
              [3,6,9],
              [3,2,5]])
print(x)
print(x.dtype)
print(x.shape)
print(x.size)

x.min()
x.max()
x.mean()
x.max(axis=0) #column wise operation
x.max(axis=1) # row wise operation

#################################################

x = np.arange(2,20,3)
x = np.arange(10)
x = np.linspace(2,20,21)
x = np.ones(5)
x = np.ones((3,5))
x = np.ones((3,5),dtype='int32')
x = np.zeros((2,3))
x = np.linspace(0,6,7)
x = np.logspace(0,6,7)

##############################
# Random Numbers in numpy

# uniform distribution b/w 0 1to 1
x = np.random.rand(2,5)
x

# normal distribution with mean = 0 and std =1
x = np.random.randn(10)
x

# integer random numbers
x = np.random.randint(low=10,high=100,size=5)
x

x = np.random.randint(10,100,5)
x

x = np.random.randint(low=10,high=100,size=(4,3))
x
#############################################

np.sin(np.deg2rad(90))
np.log10(100000)
np.sqrt(456788)

##############################################
# Linear Algebra
m = np.matrix([[4,5,6],[3,1,8],[6,7,2]])
np.linalg.inv(m)
np.linalg.det(m)

'''
3x - 7y = 1
4x + y = 22
'''
a = [[3,-7],[4,1]]
b = [1,22]
np.linalg.solve(a,b)

x = np.random.randint(low=10,high=100,size=5)
x




















