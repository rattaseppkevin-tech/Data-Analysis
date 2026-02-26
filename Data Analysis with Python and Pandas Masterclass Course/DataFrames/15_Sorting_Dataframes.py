import pandas as pd

oil = pd.read_csv(r"C:\Users\Kevin\Desktop\oil.csv")
oil.columns = ["date", "price"]
oil["benchmark"] = 100

print(oil.sort_index(ascending=False, axis=1))

oil["date"] = pd.to_datetime(oil["date"])
oil["month"] = oil["date"].dt.month

print(oil.sort_values(["month", "price"], ascending=[True, False]))