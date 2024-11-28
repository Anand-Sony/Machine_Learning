import numpy as np

arr1 = np.array([[1,2,3] , [4,5,6]])
print(arr1)
'''[[1 2 3]
 [4 5 6]]'''

print(" ")

arr = np.array([1,2,3,4,5,6] , ndmin=4)
# ndmin is used to specify the minimum number of dimensions that the array should have. It is
# used to create a multi-dimensional array from a 1-D array. The default value of nd
# is 0.

print(arr) #[[[[1 2 3 4 5 6]]]]