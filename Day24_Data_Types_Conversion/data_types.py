import numpy as np

# Original array
marks = np.array([85, 90, 78, 92, 88])

print("Original marks:", marks)
print("Original data type:", marks.dtype)

# Convert integers to floats
float_marks = marks.astype(float)

print("\nMarks as floats:", float_marks)
print("New data type:", float_marks.dtype)

# Convert floats to integers
temperatures = np.array([25.7, 30.9, 28.4, 35.6])

integer_temperatures = temperatures.astype(int)

print("\nOriginal temperatures:", temperatures)
print("Integer temperatures:", integer_temperatures)

# Check array properties
print("\nNumber of dimensions:", marks.ndim)
print("Array shape:", marks.shape)
print("Number of elements:", marks.size)