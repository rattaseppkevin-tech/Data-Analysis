import pandas as pd
import numpy as np

oil = pd.read_csv(r"C:\Users\Kevin\Desktop\oil.csv")
oil.columns = ["dates", "price"]

# Calculating Dollars to Euros and making new column for the euro_price
oil["euro_price"] = oil["price"] * 1.1

last_row = oil.iloc[[-1]] # Topelt sulud teevad sellest DataFrame'i, mitte Series'i
oil = pd.concat([oil, last_row], ignore_index=True)

print(oil.tail())

print(oil.shape)

print(oil.nunique(dropna=False))

print(oil.duplicated(subset="price").sum())

print(oil.drop_duplicates(subset=["price"], ignore_index=True))