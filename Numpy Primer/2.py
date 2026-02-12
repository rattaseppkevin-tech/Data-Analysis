import numpy as np

array = np.array(range(5)) # Create a NumPy array with values from 0 to 4
print(array) # Print the 1D array

array_2d = np.array([range(5), range(5)]) # Create a 2D NumPy array with two rows of values from 0 to 4
print(array_2d ) # Print the 2D array

print(array_2d.T) # Transpose the 2D array and print it
print(array_2d.ndim) # Print the number of dimensions of the original array
print(array_2d.T.ndim) # Print the number of dimensions of the transposed array