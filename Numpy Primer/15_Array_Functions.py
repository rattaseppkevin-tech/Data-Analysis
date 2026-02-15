import numpy as np

prices = np.array([30.99, 5.49, 3.50, 8.25, 99.99, 30.99, 5.49, 3.50, 8.25, 99.99])
inventory = np.array([20, 11, 27, 2, 55, 6, 3, 66, 77, 2])

inventory_value = prices * inventory

#Sort the prices from lowest to highest.
inventory_value.sort()

print(inventory_value)

reshaped_inventory_value = inventory_value.reshape(2, 5)
print(reshaped_inventory_value)

#Calculates the median value of the prices
#useful for avoiding the influence of outliers
#if there is 10 items in the array for example then the middle point is the mean of index 5 and 6.
median_value = np.median(reshaped_inventory_value).round(2)
print(median_value)

#Calculate the value at a specific percentile (e.g., 25th, 75th)
percentile_value = np.percentile(reshaped_inventory_value, 50).round(2)
print(percentile_value)

#Calculates the square root of all elements in the array.
sqrt_value = np.sqrt(reshaped_inventory_value).round(2)
print(sqrt_value)


test_array = ([1, 1, 2, 3, 4, 5, 6, 2, 5, 6, 8, 9, 1])
#
unique_value = np.unique(test_array)
print(unique_value)