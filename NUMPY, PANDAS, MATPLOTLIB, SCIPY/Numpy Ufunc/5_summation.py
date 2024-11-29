import numpy as np
from numpy import random

arr = np.array([1,2,3,4,5])
summationArray = np.sum(arr)
print(summationArray)  # Output: 15

axisSum = np.sum(arr , axis=0)
print(axisSum)  # Output: [15]

# summationArray is the summation of all elements in the array
# axisSum is the summation of all elements in each row of the array. If the array is
# 1D, then it will be the summation of all elements in the array. If the array
# is 2D, then it will be the summation of all elements in each row of the
# array. If the array is 3D, then it will be the summation of all elements

x = np.array(random.randint(10, size =(3,3)))
print(x)
print(np.sum(x , axis=0))
# [[0 8 1]
#  [7 3 8]
#  [8 1 7]]
# [15 12 16]


y= np.array([1,2,3,4,5])
print(np.cumsum(y))  # [ 1  3  6 10 15]