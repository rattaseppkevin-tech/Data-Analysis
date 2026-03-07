import pandas as pd
import numpy as np

sales = pd.read_csv(r"C:\Users\Kevin\Desktop\transactions.csv")

sales = pd.read_csv(r"C:\Users\Kevin\Desktop\transactions.csv")
sales["date"] = pd.to_datetime(sales["date"])
sales["month"] = sales["date"].dt.month

sales["random"] = sales["transactions"] * 2.5
sales["rand_shop"] = np.random.randint(1, 55, size=len(sales))

print(sales.head())

avg_sales = sales.assign(avg_transaction = sales.groupby(["store_nbr"])["transactions"].transform("mean"),
                         difference = lambda x: x["transactions"] - x["avg_transaction"])

compareson = avg_sales.groupby(["store_nbr", "rand_shop"]).agg({"difference": "mean"}).sort_values("difference")
print(compareson)


