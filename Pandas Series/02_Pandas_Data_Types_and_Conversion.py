import numpy as np
import pandas as pd

series = pd.Series(range(5))
print(series)

series_float = pd.Series(range(5)).astype("float")
print(series_float)

series_bool = pd.Series(range(5)).astype("bool")
print(series_bool)