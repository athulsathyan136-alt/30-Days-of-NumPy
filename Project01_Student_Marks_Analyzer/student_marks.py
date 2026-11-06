
import numpy as np

# 1. Student names and subject names
students = np.array([
    "Student 1",
    "Student 2",
    "Student 3",
    "Student 4",
    "Student 5"
])

subjects = np.array(["Python", "Math", "ML", "SQL"])

# 2. Create the student marks array
marks = np.array([
    [85, 78, 92, 80],
    [65, 70, 75, 68],
    [90, 95, 88, 92],
    [35, 45, 50, 38],
    [72, 80, 69, 75]
])

# 3. Display the dataset
print("\n========== STUDENT MARKS ==========")
print(marks)
print("Array shape:", marks.shape)

# 4. Calculate total marks for each student
totals = np.sum(marks, axis=1)

print("\n========== STUDENT TOTALS ==========")
for i in range(len(students)):
    print(students[i], ":", totals[i])

# 5. Calculate average marks for each student
averages = np.mean(marks, axis=1)

print("\n========== STUDENT AVERAGES ==========")
for i in range(len(students)):
    print(students[i], ":", round(averages[i], 2))

# 6. Calculate average marks for each subject
subject_averages = np.mean(marks, axis=0)

print("\n========== SUBJECT AVERAGES ==========")
for i in range(len(subjects)):
    print(subjects[i], ":", round(subject_averages[i], 2))

# 7. Find the highest and lowest individual marks
highest_mark = np.max(marks)
lowest_mark = np.min(marks)

print("\n========== HIGHEST AND LOWEST MARKS ==========")
print("Highest mark:", highest_mark)
print("Lowest mark:", lowest_mark)

# 8. Find the top-performing student
top_index = np.argmax(totals)

print("\n========== TOP STUDENT ==========")
print("Student:", students[top_index])
print("Total marks:", totals[top_index])

# 9. Find individual marks below 40
low_positions = np.argwhere(marks < 40)

print("\n========== MARKS BELOW 40 ==========")

if len(low_positions) == 0:
    print("No marks below 40.")
else:
    for position in low_positions:
        student_index, subject_index = position

        print(
            students[student_index],
            "-",
            subjects[subject_index],
            ":",
            marks[student_index, subject_index]
        )

print("\n========== ANALYSIS COMPLETED ==========")
