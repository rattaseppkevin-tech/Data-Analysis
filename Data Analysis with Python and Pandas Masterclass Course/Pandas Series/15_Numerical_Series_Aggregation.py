import pandas as pd
import numpy as np

path = r"C:\Users\Kevin\Documents\GitHub\Data-Analysis-Specialization\Data Analysis with Python and Pandas Masterclass Course\Pandas Series\transactions.csv"

transactions = pd.read_csv(path)
transactions_series = pd.Series(transactions["transactions"])

print(transactions_series)

print(transactions_series.count())

print(transactions_series.iloc[:5].quantile([.5], interpolation="nearest"))