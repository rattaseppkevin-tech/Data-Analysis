import numpy as np

prices = np.array([10.99, 5.49, 3.50, 8.25, 9.99, 10.85, 50.50]) # Create a NumPy array of prices

shipping_prices = prices + 5 # Add 5 to each element in the prices array
print(shipping_prices) # Print the updated prices array

discount_pct = np.random.random(6) # Generate a 1D array of 6 random numbers between 0 and 1 to represent discount percentages
pct_owed = 1 - discount_pct # Calculate the percentage owed after applying the discount

total_with_shipping = shipping_prices[:6] # Take the first 6 elements of the shipping_prices array (excluding the last one)


final_amounts = total_with_shipping * pct_owed # Calculate the final amounts to pay after applying the discount
print(final_amounts.round(2)) # Print the final amounts after discount, rounded to 2 decimal places