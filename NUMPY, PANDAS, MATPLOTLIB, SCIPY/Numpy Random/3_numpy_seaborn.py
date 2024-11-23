import seaborn as sns
import matplotlib.pyplot as plt

sns.distplot([0,1,2,2,4,5])  #wth curve and shaded part
sns.distplot([0,1,2,2,4,5] , hist=False) #only curve without shaded part
plt.show()