import numpy as np
from numpy import random

data = np.array([1,2,3,4,5])
productList = np.product(data)
print(productList)  # Output: 120

x= np.array(random.randint(10, size=(3,3)))
print(x)  
print(np.prod(x , axis=0))
# [[9 6 8]
#  [1 7 0]
#  [5 4 8]]
# [ 45 168   0]


y = np.array([2,3,4,5,6])
cumProduct = np.cumprod(y)
print(cumProduct)  # Output: [  2   6  24 120 720]
