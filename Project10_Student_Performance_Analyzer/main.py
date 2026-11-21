
import numpy as np

# Load dataset
data = np.genfromtxt(
    "data/student_marks.csv",
    delimiter=",",
    skip_header=1
)

student_ids = data[:, 0].astype(int)
marks = data[:, 1:]

subjects = ["Math", "Science", "English", "Computer"]

# Individual student averages
student_averages = np.mean(marks, axis=1)

# Subject averages
subject_averages = np.mean(marks, axis=0)

# Subject analysis
print("\n===== SUBJECT PERFORMANCE =====")

for i in range(len(subjects)):
    print(subjects[i], "Average:", subject_averages[i])

best_subject = np.argmax(subject_averages)
weakest_subject = np.argmin(subject_averages)

print("\nBest subject:", subjects[best_subject])
print("Weakest subject:", subjects[weakest_subject])

# Overall class performance
class_average = np.mean(marks)
class_median = np.median(marks)
class_std = np.std(marks)

print("\n===== CLASS PERFORMANCE =====")
print("Class average:", class_average)
print("Class median:", class_median)
print("Standard deviation:", class_std)

# Student ranking
top_student_position = np.argmax(student_averages)
weak_student_position = np.argmin(student_averages)

print("\n===== STUDENT PERFORMANCE =====")

print(
    "Top student:",
    student_ids[top_student_position],
    "Average:",
    student_averages[top_student_position]
)

print(
    "Lowest student:",
    student_ids[weak_student_position],
    "Average:",
    student_averages[weak_student_position]
)

# Pass and fail analysis
passed = np.where(student_averages >= 50)[0]
failed = np.where(student_averages < 50)[0]

print("\nPassed students:", len(passed))
print("Failed students:", len(failed))

# Identify students needing support
support_students = student_ids[student_averages < 60]

print("Students needing support:", support_students)

# Top five students
ranking = np.argsort(student_averages)[::-1]

print("\n===== TOP FIVE STUDENTS =====")

for position in ranking[:5]:
    print(
        "Student:",
        student_ids[position],
        "Average:",
        round(student_averages[position], 2)
    )

# Percentile analysis
print("\n75th percentile:", np.percentile(student_averages, 75))

# Grade distribution
grades = np.where(
    student_averages >= 90, "A",
    np.where(
        student_averages >= 75, "B",
        np.where(
            student_averages >= 60, "C",
            np.where(student_averages >= 50, "D", "F")
        )
    )
)

unique_grades, grade_counts = np.unique(
    grades,
    return_counts=True
)

print("\n===== GRADE DISTRIBUTION =====")

for grade, count in zip(unique_grades, grade_counts):
    print(grade, ":", count)

# Save student report
student_report = np.column_stack((
    student_ids,
    student_averages,
    grades
))

np.savetxt(
    "outputs/student_report.csv",
    student_report,
    delimiter=",",
    fmt="%s",
    header="Student_ID,Average,Grade",
    comments=""
)

print("\nReport saved successfully!")
