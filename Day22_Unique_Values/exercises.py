import numpy as np

numbers = np.array([4, 4, 7, 2, 7, 4, 9, 2])

# Exercise 1: Find all unique values.
unique = np.unique(numbers)
print("All unique values: ")
print(unique)
# Exercise 2: Find unique values and their counts.
value, count = np.unique(numbers,return_counts=True)
print("Count: ",count)
print("Value: ",value)
# Exercise 3: Print only the counts.
print("count: ",count)
# Exercise 4: Find how many times 4 appears.
find = np.count_nonzero(numbers==4)
print(find)