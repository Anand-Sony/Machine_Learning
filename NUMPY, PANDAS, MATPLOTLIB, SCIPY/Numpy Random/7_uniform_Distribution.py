from numpy import random
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

x= random.uniform(size=2)
y= random.uniform(size=(2,2))
print(x)
print(y)

sns.distplot(random.uniform(size=1000))
plt.show()