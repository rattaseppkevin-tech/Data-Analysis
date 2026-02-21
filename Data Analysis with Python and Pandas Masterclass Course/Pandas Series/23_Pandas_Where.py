import pandas as pd
import numpy as np

my_series = pd.Series(["Day0", "Day0", "Day2", "Day3", "Day3"])

# Getting the last element in my_series
# print(my_series.str[-1])

# Custom function

def search(string, looking_for):
    if looking_for  in string:
        return "Found It!"
    return "Nope"

# print(my_series.apply(search, args="2"))

# Better version of the previous function.

print(my_series.where(my_series.str.contains("2"), "Nope!").where(
    ~my_series.str.contains("2"), "Found It!"))

print(np.where(my_series.str.contains("2"), "Found it!", "Nope!"))