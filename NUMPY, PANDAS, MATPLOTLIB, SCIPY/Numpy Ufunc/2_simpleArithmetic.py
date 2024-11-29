import numpy as np
arr1 = np.array([1,2,3,4,5])
arr2 = np.array([6,7,8,9,10])

addResult = np.add(arr1, arr2)
print(addResult)  # Output: [ 7  9 11 13 15]

divideResult = np.divide(arr1 , arr2)
print(divideResult)  # Output: [0.16666667  0.28571429  0.375  0.44444444  0.5]

scaleDivide = np.divide(arr2 , 2)
print(scaleDivide)  # Output: [3.  3.5 4.  4.5 5. ]
