import pandas as pd
import numpy as np

my_series = pd.Series([0, 1, 2, 3, 4], index=["Day0", "Day1", "Day2", "Day3", "Day4"])

print(my_series.loc[my_series != 2])
print(my_series.loc[~(my_series != 2)])

print(my_series.loc[my_series.isin([1, 2])])
print(my_series.loc[~my_series.isin([1, 2])])