import pandas as pd
import numpy as np

df = pd.read_csv("Pandas\data.csv")
print(df.head(10)) 
#give the data for the top 10 rows

print(df.tail())
#gives data for the last 5 rows

print(df.info())
#gives information about the data types of the columns and the number of non-null values in each column