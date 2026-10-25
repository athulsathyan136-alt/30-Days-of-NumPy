import numpy as np

morning = np.array([10, 20, 30])
evening = np.array([40, 50, 60])

# Exercise 1: Join morning and evening into one array.
combined = np.concatenate((morning,evening))


# Exercise 2: Print the combined array.
print("Combined array: ")
print(combined)

# Exercise 3: Print the shape of the combined array.
print("Combined shape: ")
print(combined.shape)