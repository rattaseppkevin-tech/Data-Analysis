import pandas as pd

my_series = pd.Series(["Day0", "Day0", "Day2", "Day3", "Day3"])

print(my_series.nunique())

print(my_series.unique())

print(my_series.value_counts(normalize=True))


