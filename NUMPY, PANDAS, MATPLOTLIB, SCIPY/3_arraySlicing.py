import numpy as np
arr1 = np.array([1,2,3,4,5,6,7,8,9,10])

sliceArr1 = arr1[2:-1]
sliceArr2 = arr1[2:5]
print(sliceArr1)  #[3 4 5 6 7 8 9]
print(sliceArr2)  #[3 4 5]

arr2 = np.array([[1,2,3] , [4,5,6] , [7,8,9]])
print(arr2)

'''
[[1 2 3]
[4 5 6]
[7 8 9]]'''
sliceArr3 = arr2[0:2 , 1:3]
print(sliceArr3)
'''[[2 3]
   [5 6]]'''


arr4 = np.array([1,2,3,4,5,6,7,8,9])
print(arr4[0:-1:2])  #[1 3 5 7]