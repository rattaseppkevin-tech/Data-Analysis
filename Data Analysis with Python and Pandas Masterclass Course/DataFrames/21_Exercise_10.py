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
print(sales["seasonal_bonus"].value_counts().iloc[1:].sum() * 100)