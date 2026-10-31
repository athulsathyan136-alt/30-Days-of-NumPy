import numpy as np

sales = np.array([10, 20, 30, 40])

# Cumulative sum
total = np.cumsum(sales)

print("Daily sales:", sales)
print("Cumulative sales:", total)

# Cumulative product
numbers = np.array([2, 3, 4])

product = np.cumprod(numbers)

print("Numbers:", numbers)
print("Cumulative product:", product)

# Difference between consecutive values
temperatures = np.array([20, 25, 32, 30])

difference = np.diff(temperatures)

print("Temperatures:", temperatures)
print("Temperature differences:", difference)