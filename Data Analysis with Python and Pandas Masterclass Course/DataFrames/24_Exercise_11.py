import pandas as pd
import numpy as np

sales = pd.read_csv(r"C:\Users\Kevin\Desktop\transactions.csv")

sales["pct_to_target"] = sales.loc[:, "transactions"] / 2500

sales["met_target"] = sales.loc[:, "pct_to_target"] >= 1

sales["bonus_payable"] = (sales.loc[:, "met_target"] == True) * 100

sales["date"] = pd.to_datetime(sales["date"])
sales["month"] = sales["date"].dt.month
sales["day_of_week"] = sales["date"].dt.dayofweek

conditions = [
    sales["month"] == 12,
    (sales["month"] == 5) & (sales["day_of_week"] == 6),
    (sales["month"] == 7) & (sales["day_of_week"] == 0)
]

choices = ["Holiday Bonus", "Corporate Month", "Summer Special"]

sales["seasonal_bonus"] = np.select(conditions, choices, default="NoNe")

# Exercise Drop all the columns we made and recreate them with assign method.
sales = sales.drop(sales.columns[3:], axis=1)
transactions = sales.assign(
    target_pct = sales["transaction_count"] / 2500,
    met_target = (sales["transaction_count"] / 2500) >= 1,
    bonus_payable = ((sales["transaction_count"] / 2500) >= 1) * 100,
    month = sales.date.dt.month,
    day_of_week = sales.date.dt.dayofweek,
    seasonal_bonus = np.select(conditions, choices, default="None")
)
print(transactions)



