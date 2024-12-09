import matplotlib.pyplot as plt
import numpy as np

plt.subplot(2,2,1)  #top left
plt.plot([1,2,3] ,[4,5,6])
plt.title('Plot 1')

plt.subplot(2,2,2) #top right
plt.plot([1,4,5], [0,1,2])
plt.title('Plot 2')

plt.subplot(2,2,3) #bottom left
plt.plot([1,2,3] ,[4,5,6] , color="yellow")
plt.title('Yellow Plot' )

plt.subplot(2,2,4) #bottom right
plt.plot([1,4,5], [0,1,2] ,color="pink")
plt.title('Pink Plot')

plt.show()