import pandas as pd

oil =[
    46.66, 45.32, 44.66, 44.07, 44.88, 44.96, 45.2, 44.62, 43.39, 43.29,
    45.86, 45.56, 45.37, 45.69, 47.48, 48.07, 46.72, 46.72, 45.66, 45.29,
    49.41, 51.08, 51.7, 51.72, 50.95, 49.85, 50.84, 51.51, 52.74, 52.99,
    51.01, 50.9, 51.93, 52.13, 52.22, 51.44, 51.98, 52.01, 52.82, 54.01,
    53.8, 53.75, 52.36, 53.26, 53.77, 53.98, 51.95, 50.82, 52.19, 53.01,
    52.36, 52.45, 51.12, 51.39, 52.33, 52.77, 52.38, 52.14, 53.24, 53.18,
    52.63, 52.75, 53.9, 53.55, 53.81, 53.01, 52.19, 52.37, 52.99, 53.84,
    52.96, 53.21, 53.11, 53.41, 53.41, 54.02, 53.61, 54.48, 53.99, 54.04,
    54.0, 53.82, 52.63, 53.33, 53.19, 52.68, 49.83, 48.75, 48.05, 47.95,
    47.24, 48.34, 48.3, 48.34, 47.79, 47.02
]

dates = pd.date_range(start="2016-12-20", periods=len(oil))
oil_series = pd.Series(oil, index=dates, name="oil_prices")

march_index = oil_series.index.month == 3
march_prices = oil_series[march_index]
march_mean = march_prices.mean()
march_sum = march_prices.sum()

print(f"Sum is {march_sum} and mean is {march_mean}")

jan_feb_sales = oil_series.isin([1, 2]).count()
print(jan_feb_sales)

tenth = oil_series.quantile(.10)
ninth = oil_series.quantile(.90)

print(f"Tenth is {tenth} and ninth is {ninth}")

integer_counts = oil_series.astype(int).value_counts(normalize=True)
print(integer_counts)