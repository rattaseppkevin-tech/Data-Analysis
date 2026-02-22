import pandas as pd

sales = pd.read_csv(r"C:\Users\Kevin\Desktop\transactions.csv")

# Assignment inspect first 5 rows of the transactions data.
print(sales.head(5))

# Dive a bit more deeply into the data and check if there are any missing values.
print(sales.info())

print(sales.nunique())


print(sales["transactions"].describe().round())