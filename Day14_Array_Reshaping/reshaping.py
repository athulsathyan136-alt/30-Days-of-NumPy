import numpy as np

numbers = np.array([1, 2, 3, 4, 5, 6])

print("Original array:")
print(numbers)

reshaped = numbers.reshape(2,3)
print("\nReshaped array: ")
print(reshaped)


print("\nOriginal shape:", numbers.shape)
print("New shape:", reshaped.shape)