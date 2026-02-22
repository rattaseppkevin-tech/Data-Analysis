import pandas as pd
import numpy as np

oil = pd.read_csv(r"C:\Users\Kevin\Desktop\oil.csv")
oil.columns = ["dates", "price"]

# Calculating Dollars to Euros and making new column for the euro_price
oil["euro_price"] = oil["price"] * 1.1

print(oil.head())

print(oil.iloc[:10, :])
print(oil.iloc[:10, -2:])

print(oil.loc[:5, ["dates", "euro_price"]])
print(oil.loc[:5, "dates":"euro_price"])