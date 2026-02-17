import numpy as np
import pandas as pd

my_series = pd.Series([0, 1, 2, 3, 4], index=["Day0", "Day1,", "Day2", "Day3", "Day4"])

print(my_series.loc["Day0":"Day4"])

my_series.index = [0, 55, 22, 2, 6]

print(my_series[0:5])

reset = my_series.reset_index(drop=True).loc[:3]

print(reset)
