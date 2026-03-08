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


avg_sale = sales.assign(store_avg = sales.groupby(["store_nbr", "day_of_week"])["transactions"].transform("mean"),
                        trans_diff = lambda x: x["transactions"] - x["store_avg"])

new = avg_sale.query("1 <= store_nbr <= 11 and bonus_payable != 0").pivot_table(
    index = "store_nbr",
    columns ="day_of_week",
    values = "bonus_payable",
    aggfunc = "sum")
    #.style.background_gradient(cmap="RdYlGn", axis=None)

print(new)

final = new.reset_index().melt(
    id_vars="store_nbr",
    var_name="day",
    value_name="avg_bonus"
)

print(final)



