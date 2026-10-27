import numpy as np

scores = np.array([15, 25, 35, 45, 55, 65])

# Exercise 1: Split scores into 2 equal parts.
parts = np.split(scores,2)

# Exercise 2: Print the first part.
print("\nFirst parts:")
print(parts[0])

# Exercise 3: Print the second part.
print("\nSecond parts:")
print(parts[1])

# Exercise 4: Split scores into 3 equal parts and print each part.

part = np.split(scores,3)
print("\nFirst parts:")
print(part[0])
print("\nSecond parts:")
print(part[1])
print("\nThird parts:")
print(part[2])