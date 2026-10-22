
import numpy as np

numbers = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120])

print("Original array:")
print(numbers)

# Exercise 1: Reshape into 3 rows and 4 columns
reshapes = numbers.reshape(3,4)
print("\nReshape Array(3,4):")
print(reshapes)

# Exercise 2: Reshape into 4 rows and 3 columns
reshapes = numbers.reshape(4,3)
print("\nReshape Array(4,3):")
print(reshapes)


# Exercise 3: Print the shape of your 3-row array
print("\nOriginal shape:", numbers.shape)
print("New shape:", reshapes.shape)

# Exercise 4: Try reshaping into 5 rows and 3 columns.
# Why does NumPy raise an error?
reshapes = numbers.reshape(5,3)
print("\nReshape Array(5,3):")
print(reshapes)