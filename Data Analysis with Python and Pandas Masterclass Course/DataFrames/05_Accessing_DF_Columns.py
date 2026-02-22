import pandas as pd
import numpy as np

oil = pd.read_csv(r"C:\Users\Kevin\Desktop\oil.csv")
oil.columns = ["dates", "prices"]

print(oil)
print(oil["prices"]) # or oil.prices

print(oil[["dates", "prices"]])