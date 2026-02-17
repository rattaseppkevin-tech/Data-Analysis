import numpy as np

my_array = np.arange(20) # Create a NumPy array with values from 0 to 19

print(np.where(my_array % 2 == 0, "even", "odd")) # Use np.where to create an array of "even" and "odd" based on the values in my_array

print(np.where(my_array % 2 == 0, "even", np.where(my_array == 9, my_array, "odd"))) # Use nested np.where to create an array where even numbers are labeled "even", the number 9 is kept as is, and odd numbers are labeled "odd"