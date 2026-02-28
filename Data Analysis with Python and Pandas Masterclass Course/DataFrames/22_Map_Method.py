import pandas as pd
import numpy as np

retail = pd.read_csv(r"C:\Users\Kevin\Desktop\retail.csv")


product_category_dict = {
    "PRODUCE": "Grocery",
    "POULTRY": "Grocery",
    "GROCERY I": "Grocery",
    "GROCERY II": "Grocery",
    "EGGS": "Grocery"
}

print(retail.loc[:, "family"].map(product_category_dict).value_counts(dropna=False))
