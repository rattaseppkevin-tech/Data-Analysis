import pandas as pd
import numpy as np

sales = [0, 5, 166, np.nan, 456]

sales_series = pd.Series(sales, name="Sales")
print(sales_series)

print(sales_series.add(2, fill_value=0))