import numpy as np
import pandas as pd

my_series = pd.Series(["Day0", "Day1", "Day2", "Day3", "Day4"])

print(my_series.str.contains("1"))

print(my_series.str.strip("Day").astype("int"))

print(my_series.str.split('', expand=True))