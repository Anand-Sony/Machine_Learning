import matplotlib.pyplot as plt
import numpy as np

x= [1,2,3,4,5]
y = [2,3,5,7,11]

plt.plot(x,y , marker="o")
# plt.grid(True) 
# or we can also write :

plt.grid(color="yellow" , linestyle="--" , linewidth=1.2) 
plt.show()