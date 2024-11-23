from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x = random.poisson(lam=50 , size=1000)
#lam is the average rate of events occurring in a fixed interval of time or space.
#size is the number of values to generate
print(x)
sns.distplot(x , hist=False ,label="Poisson") 
sns.distplot(random.normal(loc=50, scale=7 ,size=1000 ) , label="Normal")

plt.show()