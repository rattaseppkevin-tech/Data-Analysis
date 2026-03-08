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


new = sales.melt(id_vars = "store_nbr",
                 value_vars = ["transactions", "bonus_payable"],
                 value_name = "Something")\
                 
print(new)