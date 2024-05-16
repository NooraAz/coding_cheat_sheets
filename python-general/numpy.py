import numpy as np

# ------- create an array ------------
# Initializing arrays :
np.empty((2,2),bool) # boolean
np.full((2,2),False) # all False
np.zeros((2, 2))     # all zero
np.linspace(1,20,20) # linearly spaced (start,stop,number of elements)
np.arange(0,1,0.1)   # linearlr spaced (start,stop,step)
np.random.randn(2,2) # array of shape (2,2) filled with random floats 
# sampled from a univariate Gaussian distribution of mean 0 and variance 1
np.diag(v) # create a diagonal matrix with values of v as its diagonal values


# -------- array transformations ------
# changing shape of array
arr = arr.reshape((3, 2))

# -------- solving matrix --------------
np.linalg.solve(a, b) # finds x for ax = b

# gettig unique values and their count from an a list
values, counts = np.unique(arr, return_counts= True)

# deleting a row or column
numpy.delete(arr, row_index, axis=0)
numpy.delete(arr, col_index, axis=1)

# add values of two lists together (one by one)
result = np.add(list1,list2)
# append a list to another one
result = np.append(arr1,arr2)

# matrix multiplication
result = np.matmul(arr1,arr2)
result = np.dot(arr1,arr2)
result = np.multiply(arr1,arr2)

# matrix transpose
# needs double bracket for 1D lists
arr.transpose()
arr.T

# getting 5 random numbers between 0 and 100
numbers = np.random.randint(100, size=(5))

#----- reading files

# second column
np.loadtxt("myfile.txt")[:, 1]



