import pandas as pd

sales = pd.read_csv(r"C:\Users\Kevin\Desktop\transactions.csv")

print(sales)

print(sales.shape)
print(sales.columns)

print(sales.dtypes)