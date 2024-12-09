import matplotlib.pyplot as plt
import numpy as np

yPoints = np.array([3,8,1,10])

plt.plot(yPoints , marker="o" , label="data" , linestyle="--")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Plotting Points")
plt.legend()
plt.show()