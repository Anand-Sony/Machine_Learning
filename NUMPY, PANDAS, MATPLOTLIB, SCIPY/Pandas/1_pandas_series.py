import numpy as np
import pandas as pd

a = [7,5,8,1,5]
myData1 = pd.Series(a)
myData2 = pd.Series(a , index=["p","r" ,"s" , "t" , "u"])

print(myData1)# 0    7
#                 1    5
#                 2    8
#                 3    1
#                 4    5
#                dtype: int64

print(myData2)
# p    7
# r    5
# s    8
# t    1
# u    5
#dtype: int64