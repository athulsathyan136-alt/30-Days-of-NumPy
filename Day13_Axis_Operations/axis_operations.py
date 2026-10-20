
import numpy as np

marks = np.array([
    [80, 90],
    [70, 85],
    [60, 95]
])

print("Student marks:")
print(marks)

# Total marks for each subject (each column)
print("\nColumn totals:")
print(np.sum(marks, axis=0))

# Total marks for each student (each row)
print("\nRow totals:")
print(np.sum(marks, axis=1))

# Average marks for each subject
print("\nColumn averages:")
print(np.mean(marks, axis=0))

# Average marks for each student
print("\nRow averages:")
print(np.mean(marks, axis=1))
