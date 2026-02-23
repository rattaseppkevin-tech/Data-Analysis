import pandas as pd

sales = pd.read_csv(r"C:\Users\Kevin\Desktop\transactions.csv")

final_subset = sales.loc[1:][["store_nbr", "transactions"]]
print(final_subset)

unique_stores = sales["store_nbr"].nunique()
print(f"Unikaalseid poode: {unique_stores}")

total_txns_millions = sales["transactions"].sum() / 1000000

print(f"Tehinguid kokku: {total_txns_millions:.2f} miljonit")