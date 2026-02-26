import pandas as pd

sales = pd.read_csv(r"C:\Users\Kevin\Desktop\transactions.csv")

sales["pct_to_target"] = sales.loc[:, "transactions"] / 2500

sales["met_target"] = sales.loc[:, "pct_to_target"] >= 1

sales["bonus_payable"] = (sales.loc[:, "met_target"] == True) * 100

sales["date"] = pd.to_datetime(sales["date"])
sales["month"] = sales["date"].dt.month
sales["day_of_week"] = sales["date"].dt.dayofweek
print(sales)
print(sales[ "bonus_payable"].sum())