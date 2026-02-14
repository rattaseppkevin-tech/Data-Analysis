import numpy as np

rng = np.random.default_rng(616) # Create a random number generator with a fixed seed for reproducibility

inventory = rng.integers(0, 100, 10) # Generate a 1D array of 10 random integers between 0 and 100
print(inventory) # Print the inventory array

inventory = inventory - 24 # Subtract 24 from each element in the inventory array
print(inventory) # Print the inventory array after subtraction (note: this modifies the inventory array)

inventory = inventory * 2 # Multiply each element in the inventory array by 2
print(inventory) # Print the inventory array after multiplication (note: this modifies the inventory array

price = (rng.random(10,) * 10).round(2) # Generate a 10D array of random numbers between 0 and 1, with shape, and round each element to 2 decimal places
print(price) # Print the price array

total_value = inventory * price # Calculate the total value by multiplying the inventory and price arrays element-wise
print(total_value) # Print the total value array

total_value = total_value.sum() # Calculate the sum of all elements in the total value array
print(total_value) # Print the total value (sum of all elements)

inventory_list = list(inventory) # Convert the inventory array to a list
print(inventory_list) # Print the inventory list