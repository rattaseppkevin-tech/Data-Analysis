import numpy as np

my_list = [x * 10 for x in range(1, 11)]

array = np.array(my_list).reshape(2, 5) # Reshape the array to 2 rows and 5 columns
print(array)

print(f"ndim: {array.ndim}") # Number of dimensions
print(f"shape: {array.shape}") # Shape of the array   
print(f"size: {array.size}") # Total number of elements
print(f"dtype: {array.dtype}") # Data type of the elements

