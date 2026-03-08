import pandas as pd

sales = pd.read_csv(r"C:\Users\Kevin\Desktop\transactions.csv")

sales = pd.read_csv(r"C:\Users\Kevin\Desktop\transactions.csv")
sales["date"] = pd.to_datetime(sales["date"])
sales["month"] = sales["date"].dt.month

sales = sales.assign(
    target_pct = sales["transactions"] / 2500,
    met_target = (sales["transactions"] / 2500) >= 1,
    bonus_payable = ((sales["transactions"] / 2500) >= 1) * 100,
    month = sales["date"].dt.month,
    day_of_week = sales["date"].dt.dayofweek)


conversion = sales.pivot_table(index = "store_nbr",
                         columns = "date",
                         values = "transactions",
                         aggfunc = ({"transactions": ["sum", "mean"]}))

print(conversion)