import numpy as np

# Create an array
marks = np.array([80, 90, 75, 85, 95])

# Save the array
np.save("marks.npy", marks)

print("Original marks:", marks)
print("Array saved successfully!")

# Load the saved array
loaded_marks = np.load("marks.npy")

print("Loaded marks:", loaded_marks)

# Save multiple arrays
students = np.array(["Athul", "Alex", "Sam"])
scores = np.array([80, 90, 75])

np.savez("student_data.npz", students=students, scores=scores)

# Load multiple arrays
data = np.load("student_data.npz")

print("Student names:", data["students"])
print("Student scores:", data["scores"])