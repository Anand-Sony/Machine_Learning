import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = [2,4,5,7,8]
y = [1,3,5,7,9]
plt.scatter(x, y , color="yellow", marker="o", s=100, edgecolors="green" )
# s is the size of the scatter plot markers in points squared. The default value is 50.

plt.title("Scatter plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()