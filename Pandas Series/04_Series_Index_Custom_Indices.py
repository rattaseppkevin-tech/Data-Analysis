import pandas as pd
import numpy as np

my_series = pd.Series(range(5))

print(my_series[1::2])

my_series = pd.Series(range(5), index=["Day0", "Day1,", "Day2", "Day3", "Day4"])

print(my_series)