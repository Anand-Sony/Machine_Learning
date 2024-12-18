import scipy.io
import numpy as np
from scipy.stats import ttest_ind

v1 = np.random.normal(size=5)
v2 = np.random.normal(size=5)
print(v1)
print(v2)
# [ 1.17239445  0.38917748 -1.63654759  0.80714071 -0.53454525]
# [-0.0630819   1.68464492 -0.11648014  1.26972424  0.55951995]
res = ttest_ind(v1 , v2)
print(res) 
# TtestResult(statistic=-1.0116469757789113, pvalue=0.34132247527711657, df=8.0)


from scipy.stats import describe
res2 = describe(v2) #v2=[-0.65055381 -0.91961859  0.47848573  0.626594   -0.63742903]
print(res2)    
'''DescribeResult(nobs=5, minmax=(-0.9196185859391349, 0.6265940021764939),
 mean=-0.22050433918290763, variance=0.5134230487710931, skewness=0.3462028750624766,
   kurtosis=-1.7470059760230061)'''
#nobs is the number of observations in the data set. In this case, it is 5
#minmax is the minimum and maximum values in the data set. In this case, it is

# A skewness of 0 means that the distribution is perfectly symmetrical. A positive skewness means
# that the distribution is skewed to the right, while a negative skewness means that the distribution
# is skewed to the left.
