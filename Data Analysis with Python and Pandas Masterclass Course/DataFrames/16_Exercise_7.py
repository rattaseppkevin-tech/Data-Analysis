import pandas as pd

sales = pd.read_csv(r"C:\Users\Kevin\Desktop\transactions.csv")

print(sales.sort_values("transactions",ascending=False).head())

print(sales.sort_values(["date", "transactions"], ascending=[True, False]).head())

print(sales.sort_index(ascending=False, axis=1).head())