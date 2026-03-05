import pandas as pd

# 1. Andmete laadimine ja ettevalmistus
sales = pd.read_csv(r"C:\Users\Kevin\Desktop\transactions.csv")
sales["date"] = pd.to_datetime(sales["date"])
sales["month"] = sales["date"].dt.month

print(sales.head())

print(sales.groupby(["store_nbr", "date"], as_index=False)
      .agg(transaction_sum = ("transactions", "sum"),
            month_avg = ("month", "mean")))