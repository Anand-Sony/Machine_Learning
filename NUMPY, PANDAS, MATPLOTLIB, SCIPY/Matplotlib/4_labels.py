import matplotlib.pyplot as plt
import numpy as np

x =[1,2,3,4,5]
y = [1,4,9,16,25]
y2 = [4,5,8,0,4]

plt.plot(x, y , label="Line-1")
plt.plot(x, y2, color='red', label="Line-2")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Plotting a simple line graph")
plt.legend(loc = "upper left" ,fontsize =12 , frameon=False )
# frameon means : box containing the label : line-1 and line-2 at top left. it will borderless.

plt.show()