import pandas as pd

retail = pd.read_csv(r"C:\Users\Kevin\Desktop\retail.csv")

print(retail.info(memory_usage="deep"))

retail = retail.astype({"family": "category"})

print(retail.loc[:, "family"].value_counts())

print(retail.info(memory_usage="deep"))