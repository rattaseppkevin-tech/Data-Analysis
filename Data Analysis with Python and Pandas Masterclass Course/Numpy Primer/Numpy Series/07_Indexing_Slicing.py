import numpy as np  

integer_array = np.arange(12) # Create a NumPy array of integers

print(integer_array) # Print the integer array
print(integer_array[0]) # Print the integer array
print(integer_array[-1]) # Print the last element of the integer array
print(integer_array[:5]) # Print the first 5 elements of the integer array
print(integer_array[5:]) # Print the elements of the integer array starting from index 5 to the end
print(integer_array[2:8:2]) # Print every second element of the integer array
print(integer_array[::2]) # Print every second element of the integer array starting from the first element
print(integer_array[1::2]) # Print every second element of the integer array starting from the second element

new_array = integer_array.reshape((3, 4)) # Reshape the integer array into a 3x4 array
print(new_array) # Print the reshaped array
print(new_array[:, :]) # Print all elements of the reshaped array
print(new_array[1:, :]) # Print all rows of the reshaped array starting from the second row
print(new_array[:, 1:]) # Print all columns of the reshaped array starting from