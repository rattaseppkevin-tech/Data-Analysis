import numpy as np

# Exercise: Can you calculate the mean, min, max and meidan of our 3 most expensive product prices?
#Sorting the array first should help! Then calculate the number of unique price tiers we have.

prices = np.array([10.99, 5.49, 8.25, 9.99, 10.85, 50.50])
price_tiers = np.array(["Budget", "Budget", "Mid-Tier", "Luxury", "Mid-Tier", "Luxury"])

prices.sort()

top_3 = prices[-3:]


min_price = top_3.min()
max_price = top_3.max()
mean_price = top_3.mean()
median_price = np.median(top_3)
print(f"Min: {min_price}\nMax: {max_price}\nMean: {mean_price}\nMedian: {median_price}")

unique_tiers = np.unique(price_tiers)
print(unique_tiers)