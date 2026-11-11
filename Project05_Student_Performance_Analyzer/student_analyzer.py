
import csv
import numpy as np
from pathlib import Path

# Project paths
BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "students.csv"
OUTPUT_DIR = BASE_DIR / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

# Subject names
subjects = ["Math", "Science", "English", "Computer", "Social_Studies"]

# Load student data
student_ids = []
names = []
study_hours = []
marks_data = []

with open(DATA_FILE, "r", encoding="utf-8-sig", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        student_ids.append(row["Student_ID"])
        names.append(row["Name"])
        study_hours.append(float(row["Study_Hours"]))

        student_marks = [float(row[subject]) for subject in subjects]
        marks_data.append(student_marks)

# Convert data into NumPy arrays
marks = np.array(marks_data)
study_hours = np.array(study_hours)

# Calculate total and average marks
total_marks = np.sum(marks, axis=1)
average_marks = np.mean(marks, axis=1)

print("\n========== STUDENT PERFORMANCE ANALYZER ==========")
print("Total Students:", len(names))
print("Number of Subjects:", len(subjects))

# Overall statistics
print("\n--- Overall Performance ---")
print("Average Student Score:", round(np.mean(average_marks), 2))
print("Highest Student Average:", round(np.max(average_marks), 2))
print("Lowest Student Average:", round(np.min(average_marks), 2))
print("Median Student Average:", round(np.median(average_marks), 2))
print("Standard Deviation:", round(np.std(average_marks), 2))

# Subject-wise analysis
print("\n--- Subject-wise Performance ---")

subject_averages = np.mean(marks, axis=0)
subject_highest = np.max(marks, axis=0)
subject_lowest = np.min(marks, axis=0)

for index, subject in enumerate(subjects):
    print(
        subject,
        "| Average:", round(subject_averages[index], 2),
        "| Highest:", subject_highest[index],
        "| Lowest:", subject_lowest[index]
    )

best_subject_index = np.argmax(subject_averages)
weakest_subject_index = np.argmin(subject_averages)

print("\nBest Performing Subject:", subjects[best_subject_index])
print("Lowest Performing Subject:", subjects[weakest_subject_index])

# Pass and fail analysis
pass_mark = 40

passed_all = np.all(marks >= pass_mark, axis=1)
failed_students = np.where(~passed_all)[0]

print("\n--- Pass and Fail Analysis ---")
print("Students Passing All Subjects:", np.sum(passed_all))
print("Students with at Least One Failed Subject:", len(failed_students))

# Grade classification based on average marks
def calculate_grade(score):
    if score >= 90:
        return "A+"
    elif score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 50:
        return "D"
    else:
        return "F"

grades = [calculate_grade(score) for score in average_marks]

print("\n--- Grade Distribution ---")

for grade in ["A+", "A", "B", "C", "D", "F"]:
    count = grades.count(grade)
    print(grade, ":", count)

# Top five students
top_indices = np.argsort(average_marks)[::-1][:5]

print("\n--- Top Five Students ---")

for rank, index in enumerate(top_indices, start=1):
    print(
        rank,
        names[index],
        "| Average:", round(average_marks[index], 2),
        "| Grade:", grades[index]
    )

# Study hours and marks correlation
correlation = np.corrcoef(study_hours, average_marks)[0, 1]

print("\n--- Study Hours Analysis ---")
print("Average Study Hours:", round(np.mean(study_hours), 2))
print("Study Hours vs Marks Correlation:", round(correlation, 3))

# Percentile analysis
print("\n--- Performance Percentiles ---")
print("25th Percentile:", round(np.percentile(average_marks, 25), 2))
print("50th Percentile:", round(np.percentile(average_marks, 50), 2))
print("75th Percentile:", round(np.percentile(average_marks, 75), 2))

# Save student performance report
student_report = OUTPUT_DIR / "student_performance_report.csv"

with open(student_report, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    writer.writerow([
        "Student_ID",
        "Name",
        "Total_Marks",
        "Average_Marks",
        "Grade",
        "Study_Hours",
        "Passed_All_Subjects"
    ])

    for index in range(len(names)):
        writer.writerow([
            student_ids[index],
            names[index],
            total_marks[index],
            round(average_marks[index], 2),
            grades[index],
            study_hours[index],
            passed_all[index]
        ])

# Save subject summary report
subject_report = OUTPUT_DIR / "subject_summary.csv"

with open(subject_report, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    writer.writerow([
        "Subject",
        "Average",
        "Highest",
        "Lowest"
    ])

    for index, subject in enumerate(subjects):
        writer.writerow([
            subject,
            round(subject_averages[index], 2),
            subject_highest[index],
            subject_lowest[index]
        ])

# Save text summary
text_report = OUTPUT_DIR / "student_summary.txt"

with open(text_report, "w", encoding="utf-8") as file:
    file.write("STUDENT PERFORMANCE ANALYSIS\n")
    file.write("=============================\n")
    file.write(f"Total Students: {len(names)}\n")
    file.write(f"Average Score: {np.mean(average_marks):.2f}\n")
    file.write(f"Students Passing All Subjects: {np.sum(passed_all)}\n")
    file.write(f"Best Subject: {subjects[best_subject_index]}\n")
    file.write(f"Lowest Subject: {subjects[weakest_subject_index]}\n")
    file.write(f"Study Hours Correlation: {correlation:.3f}\n")

print("\nReports generated successfully!")
print("Student Report:", student_report)
print("Subject Report:", subject_report)
print("Text Report:", text_report)
