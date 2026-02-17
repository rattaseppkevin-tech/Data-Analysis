import numpy as np

x = np.ones(4,)# Create a 1D NumPy array of ones with 4 elements
print(x)

# Create a 2D NumPy array of zeros with 2 rows and 5 columns, and specify the data type as integer
y = np.zeros((2, 5), dtype=int)
print(y)

z = np.arange(10)# Create a NumPy array with values from 0 to 9
print(z)

q = np.linspace(0, 100, 5) # Create a NumPy array with 5 evenly spaced values between 0 and 100
print(q)

# Create a NumPy array with values from 1 to 8 with a step of 2, and reshape it to 2 rows and 2 columns
r = np.arange(1, 9, 2).reshape(2, 2) 
print(r)

p = np.identity(3) # Create a 3x3 identity matrix
print(p)