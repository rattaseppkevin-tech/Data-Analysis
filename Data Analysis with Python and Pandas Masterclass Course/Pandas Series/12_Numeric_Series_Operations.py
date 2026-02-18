import numpy as np
import pandas as pd

my_series = pd.Series([0, np.nan, 2, 3, 4], index=["Day0", "Day1", "Day2", "Day3", "Day4"])

print(my_series + 1)

my_series2 = my_series.add(1, fill_value=0).astype("int")

my_series3 = (my_series2 + my_series) * 2 + 5
print(my_series3)