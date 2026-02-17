import numpy as np
from numpy.random import default_rng
rng = default_rng(12345) # Create a random number generator instance

random_array = rng.random((10)) # Generate a 1D array of 10 random numbers between 0 and 1
print(random_array) # Print the random array    

rng1 = np.random.default_rng(12345) # Create another random number generator instance with the same seed
random_array2 = rng1.random((10)) # Generate another 1D array of
print(random_array2) # Print the second random array, which should be the same as the first one due to the same seed

rng2 = rng.integers(0, 10, 100)# Generate an array of 100 random integers between 0 and 10 (exclusive) using the same random number generator instance
print(rng2) # Print the array of random integers between 0 and 10 (exclusive) with a size of 100