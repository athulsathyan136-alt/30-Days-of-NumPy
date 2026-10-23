
import numpy as np

temperatures = np.array([
    [28, 30, 32],
    [25, 27, 29],
    [31, 33, 35]
])

print("Original temperatures:")
print(temperatures)

# Exercise 1: Convert temperatures into a 1D array using flatten()
flat = temperatures.flatten()
print("temperatures into a 1D array using flatten() :")
print(flat)

# Exercise 2: Convert temperatures into a 1D array using ravel()
raw = temperatures.ravel()
print("temperatures into a 1D array using Ravel() :")
print(raw)

# Exercise 3: Print the shape of the original array
print("shape of the original array:")
print(temperatures.shape)

# Exercise 4: Print the shape of the flattened array
print("shape of the flattened array: ")
print(flat.shape)