import numpy as np

# create a 2x2 empty boolean type array
arr = np.empty((2,2),bool)

# create an all-False array
arr = np.full((2,2),False)

# changing shape of array
arr = arr.reshape((3, 2))

# gettig unique values and their count from an a list
values, counts = np.unique(arr, return_counts= True)

# range of float numbers
# (start,stop,step)
np.arange(0,1,0.1)

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



