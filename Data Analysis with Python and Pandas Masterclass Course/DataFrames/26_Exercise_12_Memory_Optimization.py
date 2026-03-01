import pandas as pd
import numpy as np

sales = pd.read_csv(r"C:\Users\Kevin\Desktop\transactions.csv")

print(sales.info(memory_usage="deep"))
print(sales.describe())

sales["store_nbr"] = sales["store_nbr"].astype("uint8")
sales["transactions"] = sales["transactions"].astype("float16")
sales["date"] = pd.to_datetime(sales["date"])

print(sales.info(memory_usage="deep"))
print(sales.head(40))