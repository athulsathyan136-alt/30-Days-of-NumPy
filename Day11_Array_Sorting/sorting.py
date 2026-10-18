import numpy as np

number = np.array([50,10,40,20,40])

print("Original Array: ")
print(number)

ascending = np.sort(number)
print("Ascending Order: ")
print(ascending)

descending = np.sort(number)[::-1]
print("descending Order: ")
print(descending)

marks = np.array([75,45,85,65,22,44])
print("Original Marks: ")
print(marks)
print("Sorted Marks: ")
print(np.sort(marks))

data = np.array([[30,10,20],[90,70,80]])

print("Original 2D Array: ")
print(data)

print("Sorted Within each row: ")
print(np.sort(data,axis=1))