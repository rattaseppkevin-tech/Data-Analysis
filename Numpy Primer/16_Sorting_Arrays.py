import numpy as np

product_value = np.array([200.2, 555, 321.4, 996.2, 443.2, 165.3])

#Sorts the values from lowest to highest.
product_value.sort()
print(product_value)

#Easier to index items in the sorted array
print(product_value[0])
print(product_value[-1])

print(product_value[::-1])