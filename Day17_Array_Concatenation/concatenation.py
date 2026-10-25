import numpy as np

first_week = np.array([5,8,6])
second_week = np.array([7,9,4])

combined = np.concatenate((first_week,second_week))

print("First Week: ")
print(first_week)

print("Second Week: ")
print(second_week)

print("Combined usage: ")
print(combined)

print("Combined shape: ")
print(combined.shape)