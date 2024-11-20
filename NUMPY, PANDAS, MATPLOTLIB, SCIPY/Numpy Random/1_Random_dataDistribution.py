from numpy import random
import numpy as np

x = random.choice([5,6,9,8]  , p=[0.5 ,0, 0,0.5], size=16)
#The p parameter is a list of probabilities associated with each element in the sequence.
#The size parameter is the number of random elements to return. In this case, we want to    
#return 100 random elements.
print(x)
print(np.count_nonzero(x==5)) #12
print(np.count_nonzero(x==6)) #0
print(np.count_nonzero(x==9)) #0
print(np.count_nonzero(x==8)) #4

y = random.choice([1,2,3,4] ,p=[0.2,0,0.8,0] , size=(5,5))
print(y)
'''[[3 1 3 3 1]
 [3 1 3 3 3]
 [3 3 3 3 3]
 [3 3 3 3 3]
 [3 1 3 3 3]]'''

print(np.count_nonzero(y==3)) #21
print(np.count_nonzero(y==1)) #4