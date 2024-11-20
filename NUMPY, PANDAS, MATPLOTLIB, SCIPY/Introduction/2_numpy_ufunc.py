import numpy as np

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

arrAdd = np.add(arr1 , arr2)
print("Addition of the array : ", arrAdd) #[5 7 9]

arrSub = np.subtract(arr1 , arr2)
print("Subtraction of the array :",arrSub) #[-3 -3 -3]

from numpy import random
Arr1 = random.randint(10,  size=(2,2))
Arr2 = random.randint(10,  size=(2,2))
print (Arr1)   
print (Arr2)
'''        Arr1=[[1 0]     Arr2= [[0 2]
                [8 7]]           [8 0]]
                  
      '''
arrMult = np.multiply(Arr1 , Arr2)
print(arrMult)    #  mult. : [[ 0  0]
                    #        [64  0]]