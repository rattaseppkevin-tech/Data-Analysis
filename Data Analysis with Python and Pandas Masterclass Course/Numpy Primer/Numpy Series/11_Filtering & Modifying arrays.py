import numpy as np

my_array = np.arange(20) # Create a NumPy array with values from 0 to 19
print(my_array) # Print the array

bool_array = my_array % 2 == 0 # Create a boolean array where True represents even numbers, False represents odd numbers
print(bool_array) # Print the array of boolean values indicating even/odd status


even_odd = np.array(["even", "odd"] * 10) # Create a NumPy array with "even" and "  odd" repeated 10 times
print(even_odd) # Print the array of "even" and "odd" strings

print(even_odd != "odd") # Print a boolean array where True represents "even" and False represents "odd" in the even_odd array

print(even_odd[even_odd != "odd"]) # Print only the "even" values from the even_odd array using boolean indexing

my_array[even_odd != "odd"] = 0 # Set the values in my_array to 0 where the corresponding values in even_odd are not "odd" (i.e., where they are "even")
print(my_array) # Print the updated my_array with even numbers set to 0

mask = (even_odd != "odd") | (even_odd != "even")# Create a boolean mask that is True for all elements in even_odd (since every element is either "even" or "odd")
print(mask) # Print the boolean mask (which will be all True)