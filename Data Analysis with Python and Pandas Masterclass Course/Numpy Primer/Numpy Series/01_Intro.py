import numpy as np

sales = [100, 200, 300, 400, 500]
sales_array = np.array(sales) # Convert the list to a NumPy array

# Print the type of the sales_array
print(type(sales_array))


print(f"ndim: {sales_array.ndim}") # Number of dimensions
print(f"shape: {sales_array.shape}") # Shape of the array   
print(f"size: {sales_array.size}") # Total number of elements
print(f"dtype: {sales_array.dtype}") # Data type of the elements

sales = [[100, 200, 300, 400, 500], [150, 250, 350, 450, 550]]
sales_array = np.array(sales) # Convert the list to a NumPy array
print(sales_array) # Print the NumPy array

print(f"ndim: {sales_array.ndim}") # Number of dimensions
print(f"shape: {sales_array.shape}") # Shape of the array   
print(f"size: {sales_array.size}") # Total number of elements
print(f"dtype: {sales_array.dtype}") # Data type of the elements

####################################################################