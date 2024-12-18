import numpy as np
from scipy.sparse.csgraph import connected_components
from scipy.sparse.csgraph import dijkstra
from scipy.sparse.csgraph import bellman_ford

from scipy.sparse import csr_matrix

arr = np.array([[1,2,3] , [0,1,5] ,[7,82,0]])
 
new_Array = csr_matrix(arr)
print(connected_components(new_Array)) #(1, array([0, 0, 0]))

print(dijkstra(new_Array , return_predecessors=True , indices=0)) #(array([0., 2., 3.]), array([-9999,     0,     0]))

y = np.array([[2,-1,0] , [8,7,1] ,[1,4,0]])
newarray = csr_matrix(y)
print(bellman_ford(newarray , return_predecessors = True , indices=0)) #(array([ 0., -1.,  0.]), array([-9999,     0,     1]))
