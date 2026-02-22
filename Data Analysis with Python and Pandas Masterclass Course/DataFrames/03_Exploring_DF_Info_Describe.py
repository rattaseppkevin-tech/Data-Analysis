import pandas as pd

oil = pd.read_csv(r"C:\Users\Kevin\Desktop\oil.csv")

# Checking first 10 rows of the data to understand what is going on.
print(oil.head(10))

# Checking last 10 rows just in case.
print(oil.tail(10))

# Getting random samples from the data.
print(oil.sample(5))

# More information about the data missing data etc.
print(oil.info())

# Showing everything in the data, min, max, std, mean.
print(oil.describe(include="all"))