
import numpy as np

scores = np.array([45, 90, 32, 75, 60, 88])

print("Original scores:")
print(scores)

# Exercise 1: Sort scores in ascending order
print("Ascending Order: ")
print(np.sort(scores))

# Exercise 2: Sort scores in descending order
print("Descending Order: ")
print(np.sort(scores)[::-1])

# Exercise 3: Find the lowest three scores
print("Find the lowest three scores: ")
low = np.sort(scores)[:3]
print(low)
# Exercise 4: Sort each row of this 2D array
data = np.array([
    [9, 3, 6],
    [8, 2, 5]
])


# Exercise 5: Print the original array again
# Check whether sorting changed it
print("Original 2D Array: ")
print(data)
print("Sort each row: ")
print(np.sort(data,axis=1))