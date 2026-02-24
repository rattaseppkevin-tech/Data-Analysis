import pandas as pd

oil = pd.read_csv(r"C:\Users\Kevin\Desktop\oil.csv")
oil.columns = ["date", "price"]
oil["benchmark"] = 100

print(oil.head())

print(oil.loc[oil["price"] > oil["benchmark"]])

print(oil.loc[oil["date"].str[:4] == "2013"])

mask = ((oil["price"] > oil["benchmark"]) 
      & (oil["date"].str[:4] == "2013"))

