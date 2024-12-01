import pandas as pd
import numpy as np

filePath = "Pandas\data.csv"
df = pd.read_csv(filePath)

print(df)

print(df.options.discplay.max_rows)
pd.options.display.max_rows = 20
# maximum number of rows to display when printing a DataFrame. If the DataFrame
# has more rows than this number, it will be truncated and a message will be displayed indicating that
# more rows exist.