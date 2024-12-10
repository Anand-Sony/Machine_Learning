import matplotlib.pyplot as plt
import numpy as np

data = [10,21,25,25,30,30,35,40,43]
plt.hist(data , bins=50, color="blue", edgecolor="black")
plt.title("Histogram Plot")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

# x= np.random.normal(170, 10,250)
# plt.hist(x)
# plt.show()