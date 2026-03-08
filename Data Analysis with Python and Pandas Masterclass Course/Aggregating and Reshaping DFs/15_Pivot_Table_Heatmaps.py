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


print(sales.head())

conversion = sales.pivot_table(index = "store_nbr",
                         columns = "date",
                         values = "transactions",
                         aggfunc = "sum")


conversion2 = sales.query("store_nbr in [1, 10, 15, 33, 51]").pivot_table(index = "store_nbr",
                         columns = "date",
                         values = "transactions",
                         aggfunc = "sum",
                         margins=True).style.background_gradient(cmap="RdYlGn", axis=None)

print(conversion2)