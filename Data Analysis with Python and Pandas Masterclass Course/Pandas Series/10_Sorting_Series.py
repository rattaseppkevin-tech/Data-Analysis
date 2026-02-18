import numpy as np
import pandas as pd

my_series = pd.Series([2, 0, 1, 3, 4], index=["Day0", "Day1", "Day2", "Day3", "Day4"])

print(my_series.sort_values())
print(my_series.sort_values(ascending=False))
print(my_series.sort_index())