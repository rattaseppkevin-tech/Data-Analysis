import numpy as np

products = np.array(['rare tomato', 'gourmet ice cream', 'cola', 'chips', 'apple']) # Create a NumPy array of product names
prices = np.array([30.99, 5.49, 3.50, 8.25, 99.99]) # Create a NumPy array of prices

filtered_prices = prices[prices > 25] # Filter the prices array to include only prices greater than 25
print(filtered_prices) # Print the filtered prices array

fance_feast_special = products[(prices > 25) | (products == 'cola')] # Filter the products array to include only products with prices greater than 25 or equal to 'cola'
print(fance_feast_special) # Print the filtered products array for the fancy feast special

shipping_cost = np.where(prices > 25, 0, 5) # Use np.where to create an array of shipping costs where products with prices greater than 25 have a shipping cost of 0, and others have a shipping cost of 5
print(shipping_cost) # Print the shipping cost array