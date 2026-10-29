import numpy as np

values = np.array([9, 16, 25, 36])

# Exercise 1: Calculate the square root of every value.
sqrt = np.sqrt(values)
print("Sqaure root: ")
print(sqrt)
# Exercise 2: Square every value.
square = np.square(values)
print("Square of every numbers: ")
print(square)
# Exercise 3: Calculate the absolute values of [-8, 4, -3, 7].
neg = np.array([-8, 4, -3, 7])
print("Absolute value: ")
print(np.abs(neg))
# Exercise 4: Print the original values to check whether they changed.
print("Original array: ")
print(neg)