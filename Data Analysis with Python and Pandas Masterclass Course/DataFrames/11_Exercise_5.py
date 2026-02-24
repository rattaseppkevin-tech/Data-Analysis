import pandas as pd
import numpy as np

oil = pd.read_csv(r"C:\Users\Kevin\Desktop\oil.csv")
oil.columns = ["date", "price"]

print(oil.isna().sum())

print(oil.info())

current_mean = oil["price"].mean()
fill_0 = oil["price"].fillna(0)
fill_mean = oil["price"].fillna(current_mean)

print(f"Algne keskmine (NA-d välja jäetud): {current_mean}")
print(f"Uus keskmine (nullidega täidetud): {fill_0.mean()}")
print(f"Uus keskmine (keskmisega täidetud): {fill_mean.mean()}")