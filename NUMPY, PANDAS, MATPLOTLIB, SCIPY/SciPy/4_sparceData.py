import numpy as np
from scipy.sparse import csr_matrix

dense_matrix = np.array([[0,0,3] , [4,5,6] , [7,8,9]])
sparse_matrix = csr_matrix(dense_matrix)

print("dense Matrix : \n", dense_matrix)
print("Sparse Matrix : \n", sparse_matrix)
'''
dense Matrix : 
 [[0 0 3]
 [4 5 6]
 [7 8 9]]
Sparse Matrix : 
   (0, 0)	0
  (0, 1)	0
  (0, 2)	3
  (1, 0)	4
  (1, 1)	5
  (1, 2)	6
  (2, 0)	7
  (2, 1)	8
  (2, 2)	9'''


# if we want to convert this sparse matrix into a dense matrix, then :
dense_matrix = sparse_matrix.toarray()
print("Dense Matrix : \n", dense_matrix)

'''Dense Matrix : 
 [[0 0 3]
 [4 5 6]
 [7 8 9]]'''

# if we want to count non zero element in the array : 
print("Number of non zero elements in the array : ", np.count_nonzero(dense_matrix))
#Number of non zero elements in the array :  9

# now eliminate zeroes : 
mat = csr_matrix(dense_matrix)
mat.eliminate_zeros()
print("Matrix after eliminating zeroes : \n", mat)

'''Matrix after eliminating zeroes : 
   (0, 2)	3
  (1, 0)	4
  (1, 1)	5
  (1, 2)	6
  (2, 0)	7
  (2, 1)	8
  (2, 2)	9'''