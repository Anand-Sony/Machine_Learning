import matplotlib.pyplot as plt
import numpy as np

y = np.array([10,20,30,40])
mylabels = ["Apple" , "banana", "Orange" , "Watermelon"]

# plt.pie(y, labels=mylabels , startangle=90)
plt.pie(y, labels=mylabels , startangle=0)
plt.legend(loc = "upper left" , edgecolor ="black") #edgecolor will make the legend box's border radius color = "Black" 
plt.show()