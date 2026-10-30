import numpy as np

marks = np.array([80, 90, 80, 70, 90, 80])

print("Orginal marks: ")
print(marks)

print("\nUnique marks: ")
print(np.unique(marks))

print("\nUnique marks and their counts: ")
values,count = np.unique(marks,return_counts=True)

print("Values: ",values)
print("Counts: ",count)