import pandas as pd
import numpy as np

# Numpy missing values.
my_series = pd.Series([np.nan] * 5)
print(my_series)
# In numpy you can not convert nan to int.
# converting2 = my_series.astype("int")

# Pandas missing values.
my_series2 = pd.Series([pd.NA]* 5)
print(my_series2)
# In pandas you can convert NA to int.
converting = my_series2.astype("Int64")
print(converting)

print(my_series2.isna().sum())
print(my_series2.value_counts(dropna=False))

random_series = pd.Series(range(5))
random_series.loc[1:2] = pd.NA

print(random_series.isna())
print(random_series.value_counts(dropna=False))

# Filling missing numbers #
# random_series = random_series.fillna(0)
# random_series = random_series.fillna(random_series.mean())
# print(random_series)

# Dropping missing numbers #
# If dropping na-s then you should reset index too.
random_series = random_series.dropna().reset_index(drop=True)
print(random_series)