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
    day_of_week = sales["date"].dt.dayofweek
)


by_store = sales.groupby("store_nbr").agg(
    met_target_rate = ("met_target", "mean"),
    total_bonus = ("bonus_payable", "sum")
).sort_values("met_target_rate", ascending=False)

print(by_store)

by_month = sales.groupby("month").agg(
    total_bonuses = ("bonus_payable", "sum"),
    met_target_rate = ("met_target", "mean")).sort_values(
        "total_bonuses", ascending=False)

print(by_month)

by_day = sales.groupby("day_of_week", as_index=False).agg(
    total_bonuses = ("bonus_payable", "sum"),
    met_target_rate = ("met_target", "mean")).sort_values(
     "total_bonuses", ascending=False)
    
print(by_day)