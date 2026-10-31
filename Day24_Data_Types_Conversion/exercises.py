import numpy as np

# Exercise 1: Check the data type
numbers = np.array([10, 20, 30, 40])
print("Exercise 1:", numbers.dtype)

# Exercise 2: Convert integers into floats
float_numbers = numbers.astype(float)
print("Exercise 2:", float_numbers)

# Exercise 3: Convert floats into integers
prices = np.array([10.8, 20.5, 30.9])
integer_prices = prices.astype(int)
print("Exercise 3:", integer_prices)

# Exercise 4: Check array properties
print("Exercise 4 - Dimensions:", numbers.ndim)
print("Exercise 4 - Shape:", numbers.shape)
print("Exercise 4 - Size:", numbers.size)