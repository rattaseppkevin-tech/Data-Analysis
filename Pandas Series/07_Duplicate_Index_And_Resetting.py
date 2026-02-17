import numpy as np
import pandas as pd


my_series = pd.Series([0, 1, 2, 3, 4], index=["Day0", "Day0", "Day0", "Day3", "Day4"])

print(my_series["Day0"])

reset_index = my_series.reset_index(drop=True)
print(reset_index)
