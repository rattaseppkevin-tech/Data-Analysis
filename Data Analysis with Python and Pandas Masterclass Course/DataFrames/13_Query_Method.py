import pandas as pd

oil = pd.read_csv(r"C:\Users\Kevin\Desktop\oil.csv")
oil.columns = ["date", "price"]
oil["benchmark"] = 100

print(oil.query("price > benchmark or date.str.startswith('2013')"))