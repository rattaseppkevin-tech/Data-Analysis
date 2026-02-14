import numpy as np
from numpy.random import default_rng    

rng = default_rng(12345) # Create a random number generator with a fixed seed for reproducibility

random_array = rng.random((9)).reshape((3,3)) # Generate a 1D array of 9 random numbers between 0 and 1, then reshape it into a 3x3 array
print(random_array) # Print the random array

print(random_array[:2, :]) # Print the first 2 rows of the random array

print(random_array[:, 0]) # Print the first column of the random array

print(random_array[2, 1])# Print the element in the 3rd row and 2nd column of the random array