import pandas as pd

oil = pd.read_csv(r"C:\Users\Kevin\Desktop\oil.csv")
oil.columns = ["dates", "price"]

# Calculating Dollars to Euros and making new column for the euro_price
oil["euro_price"] = oil["price"] * 1.1

oil_eur = oil.drop("price", axis=1)

print(oil.drop(1, axis=0))