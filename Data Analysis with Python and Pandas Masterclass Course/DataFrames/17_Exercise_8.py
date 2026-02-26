import pandas as pd

sales = pd.read_csv(r"C:\Users\Kevin\Desktop\transactions.csv")

sales = sales.rename(columns={"transactions": "TRANSACTIONS", "store_nbr": "STORE", "date": "DATE"})

sales = sales.reindex(columns=["DATE", "TRANSACTIONS", "STORE"])

print(sales)