import numpy as np
from numpy.random import default_rng    
rng = default_rng(12345) # Create a random number generator instance

array = np.array(range(10, 101, 10)) # Create a NumPy array with values from 10 to 100 (inclusive) with a step of 10
print(array) # Print the array

y = np.linspace(10, 100, 10) # Create a NumPy array with 10 evenly spaced values between 10 and 100 (inclusive)
print(y) # Print the array of evenly spaced values between 10 and 100 (inclusive

x = np.arange(10, 101, 10).reshape((5, 2)) # Create a NumPy array with values from 10 to 100 (inclusive) with a step of 10, and reshape it to 2 rows and 5 columns
print(x) # Print the reshaped array

random_array = rng.random((9)).reshape((3,3)) # Generate a 1D array of 9 random numbers between 0 and 1, then reshape it into a 3x3 array
print(random_array) # Print the random array   