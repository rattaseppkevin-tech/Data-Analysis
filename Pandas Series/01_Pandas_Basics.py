import numpy as np
import pandas as pd

sales = [0, 5, 155, 0, 512, 1763, 542, 652, 888]

# Convert the Python list into a Pandas Series object
# The 'name' parameter assigns a label to the column for easier identification
series = pd.Series(sales, name="Sales")

print(series)

array = np.arange(5)

# Convert the array to a Pandas Series
# Pandas automatically adds an index column to label each element
print(pd.Series(array, name="Test_Array"))

print(series.values)
print(series.mean())
series.index = [11, 22, 33, 44, 55,66, 77, 88, 99]
series.name = "Special Series"
print(series)