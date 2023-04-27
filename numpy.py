import numpy as np

# create a 2x2 empty boolean type array
arr = np.empty((2,2),bool)

# create an all-False array
arr = np.full((2,2),False)

# gettig unique values and their count from an a list
values, counts = np.unique(arr, return_counts= True)

# range of float numbers
# (start,stop,step)
np.arange(0,1,0.1)

# deleting a row or column
numpy.delete(arr, row_index, axis=0)
numpy.delete(arr, col_index, axis=1)
