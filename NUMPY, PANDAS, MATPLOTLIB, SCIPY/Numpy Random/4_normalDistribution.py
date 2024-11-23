from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x= random.normal(size=(2,3)) 
print(x)

y = random.normal(loc=1 ,scale=2 , size=(2,3)) 
#loc=1 means the mean of the distribution is 1
#scale=2 means the standard deviation of the distribution is 2
print(y)
sns.distplot(y)
plt.show()

# z = random.normal(size=100)
# sns.distplot(z , hist=False)
# plt.show()