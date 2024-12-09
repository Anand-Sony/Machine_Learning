import matplotlib.pyplot as plt
import numpy as np

x = [1,2,3,4,5]
y = [2,4,6,8,10]
# plt.plot(x,y)
plt.show()

plt.plot(x,y , marker="*" , linestyle="--" ,color="yellow" , label="Data Points")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("Customized Line Plot")
plt.legend()
plt.show()

xpoint= np.array([1,8])
ypoint = np.array([3,10])
plt.plot(xpoint,ypoint ,"o")
plt.show()