import pandas as pd
import numpy as np

oil = pd.read_csv(r"C:\Users\Kevin\Desktop\oil.csv")
oil.columns = ["date", "price"]

oil["buy"] = np.where(oil["price"] > 100, "Too High", "Buy" )
print(oil["buy"].value_counts())

conditions = [
    (oil["price"] > 100),
    (oil["price"] <= 100) & (oil["price"] > 50),
    (oil["price"] <= 50)
]

choices = ["Don't Buy", "Buy", "Strong Buy"]

oil["buy"] = np.select(conditions, choices, default="Missing")
print(oil["buy"].value_counts())