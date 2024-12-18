import numpy as np
from scipy.spatial import Delaunay

import matplotlib.pyplot as plt

points = np.array([[1,2] , [3,4] , [5,6] , [6 ,7], [10,20]])
simplices = Delaunay(points).simplices

plt.triplot(points[:, 0] , points[:,1] , simplices)
plt.scatter(points[:, 0] , points[:,1]  , color="red")
plt.show()


# now KD tree : 
from scipy.spatial import KDTree

points = [(-1,1) , (2,3) , (-2,3) , (2,-3)]
kdtree = KDTree(points)
res = kdtree.query((1,1))
print(res) #(2.0, 0)
# - 2.0 is the distance between the point (1,1) and the closest point
# - 0 is the index of the closest point in the list of points

res2 = kdtree.query((2,-3))
print(res2) #(0.0, 3)