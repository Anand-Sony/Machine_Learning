import numpy as np
from numpy import random

originalArray = np.array([1,2,3,4,5,6])

print("Original Array :", originalArray)  #Original Array : [1 2 3 4 5 6]
np.random.shuffle(originalArray)
print("Array after shuffle :", originalArray)  #Array after shuffle : [3 2 6 1 5 4]

permutedArray = np.random.permutation(originalArray)
print("Permuted Array :", permutedArray)  #Permuted Array : [2 4 6 5 3 1]


Arr1 = np.array([[1,2,3] , [4,5,6], [7,8,9]])
print("Original Array 2D :\n", Arr1)  #Original Array 2D : [[
                                                            # [1 2 3]
                                                            # [4 5 6]
                                                            # [7 8 9]]
permutedRow = np.random.permutation(Arr1)
print("Permuted Array 2D :\n", permutedRow)  #Permuted Array 2D : 
                                                        # [[8 9 7]
                                                        #  [5 6 4]
                                                        # [2 3 1]]
permutedCol = np.random.permutation(Arr1.T)
print("Permuted Array 2D (Column) :\n", permutedCol.T)  #Permuted Array 2D (Column) :
                                                            # [[2 5 8]
                                                            #  [3 6 9]
                                                            #  [1 4 7]]