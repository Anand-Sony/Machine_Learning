import pandas as pd
import numpy as np

# filePath = "Pandas\data2.json"
# df = pd.read_json(filePath)

# print(df)


# or we can do the same as  : 
data = {
    "Duration" : {
        "min" : 0.0,
        "max" : 0.0,
        "mean" : 0.0,
        "std" : 0.0 
    },
    "Speed" : {
        "min" : 0.0,
        "max" : 0.0,
        "mean" : 0.0,
        "std" : 0.0
        },
    "Distance" : {
        "min" : 0.0,
        "max" : 0.0,
        "mean" : 0.0,
        "std" : 0.0
    }
}
data = pd.DataFrame(data)
print(data)