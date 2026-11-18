
import csv
import numpy as np
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data" / "students.csv"
OUTPUT_DIR = BASE_DIR / "outputs"

OUTPUT_DIR.mkdir(exist_ok=True)


def load_data():
    names = []
    student_ids = []
    marks = []

    with open(DATA_FILE, "r", newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)

        subjects = [
            "Math", "Science", "English",
            "Computer", "Social_Studies"
        ]

        for row in reader:
            student_ids.append(row["Student_ID"])
            names.append(row["Name"])
            marks.append([float(row[subject]) for subject in subjects])

    return student_ids, names, subjects, np.array(marks)


def analyze_students(student_ids, names, subjects, marks):

    # Calculate student averages
    averages = np.mean(marks, axis=1)

    # Calculate subject averages
    subject_averages = np.mean(marks, axis=0)

    # Overall statistics
    class_average = np.mean(marks)
    highest_mark = np.max(marks)
    lowest_mark = np.min(marks)
    median_mark = np.median(marks)
    standard_deviation = np.std(marks)

    # Highest and lowest performing students
    top_index = np.argmax(averages)
    lowest_index = np.argmin(averages)

    # Pass/fail: average >= 40
    passed = averages >= 40
    failed = averages < 40

    pass_count = np.sum(passed)
    fail_count = np.sum(failed)

    # Assign grades based on student average
    grades = []

    for average in averages:
        if average >= 90:
            grades.append("A")
        elif average >= 80:
            grades.append("B")
        elif average >= 70:
            grades.append("C")
        elif average >= 60:
            grades.append("D")
        elif average >= 40:
            grades.append("E")
        else:
            grades.append("F")

    # Top five students
    top_indices = np.argsort(averages)[::-1][:5]

    # Save student results
    student_report = OUTPUT_DIR / "student_results.csv"

    with open(student_report, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Student_ID", "Name", "Average", "Grade", "Result"])

        for i in range(len(names)):
            result = "Pass" if passed[i] else "Fail"
            writer.writerow([
                student_ids[i],
                names[i],
                round(averages[i], 2),
                grades[i],
                result
            ])

    # Save subject summary
    subject_report = OUTPUT_DIR / "subject_summary.csv"

    with open(subject_report, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Subject", "Average_Marks"])

        for i, subject in enumerate(subjects):
            writer.writerow([subject, round(subject_averages[i], 2)])

    # Save text report
    report_file = OUTPUT_DIR / "performance_report.txt"

    with open(report_file, "w", encoding="utf-8") as file:
        file.write("STUDENT PERFORMANCE ANALYZER\n")
        file.write("=" * 40 + "\n\n")

        file.write(f"Total students: {len(names)}\n")
        file.write(f"Class average: {class_average:.2f}\n")
        file.write(f"Highest mark: {highest_mark:.2f}\n")
        file.write(f"Lowest mark: {lowest_mark:.2f}\n")
        file.write(f"Median mark: {median_mark:.2f}\n")
        file.write(f"Standard deviation: {standard_deviation:.2f}\n\n")

        file.write(f"Passed students: {pass_count}\n")
        file.write(f"Failed students: {fail_count}\n\n")

        file.write("SUBJECT AVERAGES\n")
        for i, subject in enumerate(subjects):
            file.write(f"{subject}: {subject_averages[i]:.2f}\n")

        file.write("\nTOP FIVE STUDENTS\n")
        for rank, index in enumerate(top_indices, start=1):
            file.write(
                f"{rank}. {names[index]} - {averages[index]:.2f}\n"
            )

        file.write("\nLOWEST PERFORMING STUDENT\n")
        file.write(f"{names[lowest_index]} - {averages[lowest_index]:.2f}\n")

    # Display results
    print("\nSTUDENT PERFORMANCE ANALYZER")
    print("=" * 40)
    print(f"Total students: {len(names)}")
    print(f"Class average: {class_average:.2f}")
    print(f"Highest mark: {highest_mark:.2f}")
    print(f"Lowest mark: {lowest_mark:.2f}")
    print(f"Median mark: {median_mark:.2f}")
    print(f"Standard deviation: {standard_deviation:.2f}")

    print(f"\nPassed: {pass_count}")
    print(f"Failed: {fail_count}")

    print("\nSUBJECT AVERAGES")
    for i, subject in enumerate(subjects):
        print(f"{subject}: {subject_averages[i]:.2f}")

    print("\nTOP FIVE STUDENTS")
    for rank, index in enumerate(top_indices, start=1):
        print(f"{rank}. {names[index]}: {averages[index]:.2f}")

    print("\nReports generated successfully!")


def main():
    student_ids, names, subjects, marks = load_data()
    analyze_students(student_ids, names, subjects, marks)


if __name__ == "__main__":
    main()
