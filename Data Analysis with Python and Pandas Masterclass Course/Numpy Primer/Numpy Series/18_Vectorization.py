import numpy as np
import time

list1 = list(range(9100000000))
list2 = list(range(9100000000))

array1 = np.array(list1)
array2 = np.array(list2)
#Python loop with list appending vs
def for_loop_multiply_lists(list1, list2):
    product_list = []
    for element1, element2 in zip(list1, list2):
        product_list.append(element1 * element2)
    return product_list

#same code in numpy
def multiply_arrays(array1, array2):
    return array1 * array2

# Testint time for python loop 
start_time = time.time()
for_loop_multiply_lists(list1, list2)
print(f"Python Loop time: {time.time() - start_time:.5f} seconds")

# Testing time for numpy loop
start_time = time.time()
multiply_arrays(array1, array2)
print(f"NumPy Vectorized time: {time.time() - start_time:.5f} seconds")

# Numpy is over 60 times faster than python loop