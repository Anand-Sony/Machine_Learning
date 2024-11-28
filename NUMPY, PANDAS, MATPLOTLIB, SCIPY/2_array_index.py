import numpy as np
arr = np.array([1,2,3,4,5,6])
print(arr[2])  #3
print(arr[-1])  #6

arr2 = np.array([[1,2,3], [4,5,6]])
print(arr2[0][1])  #2

arr3 = np.array([1,2,3,4,5,6])
a = arr3>2
print(a)     #[False False  True  True  True  True]