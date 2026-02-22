import pandas as pd

oil = pd.read_csv(r"C:\Users\Kevin\Desktop\oil.csv")
print(oil)

print(oil.index)
print(oil.columns)
oil_c = oil.columns = ["price_date", "oil_price"]
print(oil_c)
print(oil.axes)
print(oil.dtypes)