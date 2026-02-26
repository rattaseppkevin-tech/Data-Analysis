import pandas as pd

oil = pd.read_csv(r"C:\Users\Kevin\Desktop\oil.csv")
oil.columns = ["date", "price"]
oil["benchmark"] = 90

print(oil.sort_index(ascending=False, axis=1))

oil["date"] = pd.to_datetime(oil["date"])
oil["month"] = oil["date"].dt.month

oil["benchmark_ratio"] = (oil.loc[:, "price"] / oil.loc[:, "benchmark"]) * 100

oil["buy"] = (oil.loc[:, "benchmark_ratio"] < 80) * (1000000 / oil.loc[:, "price"])
print(oil)