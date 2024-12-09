import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3,4,5])
y = np.array([1,4,9,16,25])
y2 = np.array([4,5,8,2,0])

plt.plot(x,y , label="line-1")
plt.plot(x,y2, color="yellow", linestyle="--",  label="line-2")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Plotting Multiple lines")
plt.legend(loc="upper right")
plt.show()