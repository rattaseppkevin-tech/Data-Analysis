import pandas as pd

# 1. Andmete laadimine ja ettevalmistus
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

avg_sale = sales.assign(store_avg = sales.groupby(["store_nbr", "day_of_week"])["transactions"].transform("mean"),
                        trans_diff = lambda x: x["transactions"] - x["store_avg"])

# Võtame sinu tehtud tabelist ainult poe 1
pood_1 = avg_sale.loc[avg_sale["store_nbr"] == 1]

# Vaatame, kuidas tal keskmiselt läheb igal nädalapäeval võrreldes ajalooga
print(pood_1.groupby("day_of_week")["trans_diff"].mean())