# DESCRIPTION:

# Create a function that calculates all possible diagonals of a given (square) matrix. Diagonals must be laid out from top to bottom

# Matrix = array of n length whose elements are n length arrays of integers.

# 2x2 example:

# diagonals( [
#  [ 1, 2 ],
#  [ 3, 4 ]
# ] ); 

# returns -> [ [ 1 ], [ 2, 3 ], [ 4 ], [ 2 ], [ 1, 4 ], [ 3 ] ]

# it is valid too -> [ [ 1, 4 ], [ 3 ], [ 2 ], [ 2 , 3 ], [ 1 ], [ 4 ] ] //Order of the returned array does not matter

# it is invalid -> [ [ 1 ], [ 3, 2 ], [ 4 ], [ 2 ], [ 1, 4 ], [ 3 ] ] //Order of each diagonal must be preserved

# 3x3 example:

# diagonals( [
 # [ 1, 2, 3 ],
  #[ 4, 5, 6 ],
  #[ 7, 8, 9 ]
# ] ); 

# returns ->

# [ [ 1 ],
#   [ 2, 4 ],
 #  [ 3, 5, 7 ],
  # [ 6, 8 ],
  # [ 9 ],
  # [ 3 ],
  # [ 2, 6 ],
  # [ 1, 5, 9 ],
  # [ 4, 8 ],
  # [ 7 ] ]

# The tests verify that the implementation is efficient (1000x1000 matrix are used in tests).

# MY SOLUTION

import numpy as np
def diagonals(matrix):
    if matrix == []:
        return []
    elif len(matrix) == 1:
        return matrix

    else:
        matrix = np.array(matrix)
        mi = np.rot90(matrix, k = 1)
        y = range(-(len(matrix)-1),len(matrix))
        z = []  

        for i in y:
            h = np.diag(mi,k=i)
            z.append(list(h))
    
        for j in reversed(y):
            x = np.diag(matrix,k = j)
            z.append(list(x))
        return z
