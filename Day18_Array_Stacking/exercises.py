import numpy as np

morning = np.array([10, 20, 30])
evening = np.array([40, 50, 60])

# Exercise 1: Stack the arrays vertically using np.vstack().
print("Vertical stack: ")
print(np.vstack((morning,evening)))

# Exercise 2: Stack the arrays horizontally using np.hstack().
print("Horizontal stack: ")
print(np.hstack((morning,evening)))

# Exercise 3: Print the shape of each result.
print("Vertical stack shape: ")
print(np.vstack((morning,evening)).shape)

print("Horizontal stack shape: ")
print(np.hstack((morning,evening)).shape)