import numpy as np
import pandas as pd

dataDict = {"Name" : ["Joe1" , "Joe2" , "Joe3"],
            "Age" : [11,22,16],
            "Gender" : ["M","F","M"],
            "Score" : [90,80,70]
            }
df = pd.DataFrame(dataDict)
print(df)
#Note :  
#series is a one dimensional data structure
#dataframe is a two dimensional data structure