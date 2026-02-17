import numpy as np
#creates random number generator (rng)
rng = np.random.default_rng(616)
#Generates 10 random numbers and multiyplys them with 10 and rounds decimal points to 2.
prices = (rng.random(10) * 10).round(2) 

print(prices)
# Inventory creates 10 random integers between 0 and 99.
inventory = rng.integers(0, 100, 10)

print(inventory)
#Mean adds everything together and gives the average value.
average_prices = prices.mean()
print(average_prices)

#Sum calculates everything together and gies total value.
sum_prices = prices.sum()
print(sum_prices)

#Min gives the lowest value in array and max gives the highest.
minmax_prices = prices.max() and prices.min()

#Std measures how spread out are the numbers.
# a low std means numbers are close to the average
#a hight std means there is a lot of vareity in the data.
std_prices = prices.std()
print(std_prices)

#Argmin gives the smallest number index location and argmax gives the highest number index.
arg_prices = prices.argmin() and prices.argmax()

#Takes prices array and makes it 2d each column needs to have exactly same amount of elements.
prices_2d = prices.reshape(5, 2)
print(prices_2d)

#axis=0 calculates the column of the array
#axis=1 calculates the row of the array
row_prices = prices_2d.sum(axis=0)
column_prices = prices_2d.sum(axis=1)
print(f" Row prices: {row_prices}")
print(f"Column prices: {column_prices}")