import numpy as np

def myAdd(x,y):
    return x+y
myAdd = np.frompyfunc(myAdd , 2 , 1)
print(myAdd([1,2,3,4,5] , [6,7,8,9,1]))  #[7 9 11 13 6]

print(type(myAdd)) #<class 'numpy.ufunc'>