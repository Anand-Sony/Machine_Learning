import numpy as np

originalArr1 = np.array([1,2,3,4,5,6])

copiedArr1 = originalArr1.copy()
copiedArr1[0] = 0;

print("original Array is : ",originalArr1) #original Array is :  [1 2 3 4 5 6]
print("copied Array is : ",copiedArr1)     #copied Array is :  [0 2 3 4 5 6]

print()

originalArr2 = np.array([1,2,3,4,5,6])
viewArr2 = originalArr2.view()
viewArr2[0] = 69
print("original Array is : ",originalArr2)  #original Array is :  [69  2  3  4  5  6]
print("view Array is : ",viewArr2)          #view Array is :  [69  2  3  4  5  6]
#So, any changes made to the new array will be reflected in the original array.

print()


#now let's use shape method : 
arr3 = np.array([[1,2,3], [4,5,6]])
print(arr3)
'''[[1 2 3]
   [4 5 6]]'''

print("Shape of the array :",arr3.shape) #Shape of the array : (2, 3)

arr3.shape = (3,2)
print(arr3)
'''[[1 2]
   [3 4]
   [5 6]]'''

print()


#now let's use reshape method :
arr4 = np.array([[1,2,3,0], [4,5,6,0]])    # 8 elements : so combinations = (1,8) (2,4) (4,2) (8,1)
arr4 = arr4.reshape(1,8)
print(arr4)  #[[ 1  2  3  0  4  5 6  0]]

arr4.shape = (2,4)
print(arr4)
'''[[1 2 3 0]
   [4 5 6 0]]'''