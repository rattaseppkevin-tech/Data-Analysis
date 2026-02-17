import pandas as pd
import numpy as np

my_series = pd.Series([0, 1, 2, 3, 4], index=["Day0", "Day1,", "Day2", "Day3", "Day4"])

print(my_series.iloc[-1])
print(my_series.iloc[1])
print(my_series.iloc[1:])
print(my_series.iloc[[0, 2, 4]])