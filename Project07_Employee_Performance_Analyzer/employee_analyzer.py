
import numpy as np
from pathlib import Path

# --------------------------------------------------
# 1. PROJECT PATHS
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data" / "employees.csv"
OUTPUT_DIR = BASE_DIR / "outputs"

OUTPUT_DIR.mkdir(exist_ok=True)


# --------------------------------------------------
# 2. LOAD EMPLOYEE DATA
# --------------------------------------------------

data = np.genfromtxt(
    DATA_FILE,
    delimiter=",",
    skip_header=1,
    dtype=float
)

employee_id = data[:, 0].astype(int)
age = data[:, 1]
salary = data[:, 2]
performance = data[:, 3]
hours = data[:, 4]
attendance = data[:, 5]


# --------------------------------------------------
# 3. BASIC INFORMATION
# --------------------------------------------------

total_employees = len(employee_id)

average_age = np.mean(age)
average_salary = np.mean(salary)
average_performance = np.mean(performance)
average_attendance = np.mean(attendance)

total_salary = np.sum(salary)

highest_salary = np.max(salary)
lowest_salary = np.min(salary)

highest_performance = np.max(performance)
lowest_performance = np.min(performance)


# --------------------------------------------------
# 4. TOP PERFORMER
# --------------------------------------------------

top_index = np.argmax(performance)

top_employee_id = employee_id[top_index]
top_employee_score = performance[top_index]


# --------------------------------------------------
# 5. PERFORMANCE CLASSIFICATION
# --------------------------------------------------

performance_category = np.select(
    [
        performance >= 90,
        performance >= 75
    ],
    [
        "Excellent",
        "Good"
    ],
    default="Needs Improvement"
)


# --------------------------------------------------
# 6. FILTER EMPLOYEES
# --------------------------------------------------

high_performers = data[performance >= 85]

low_attendance = data[attendance < 80]

high_salary_employees = data[salary >= 40000]


# --------------------------------------------------
# 7. PERFORMANCE RANKING
# --------------------------------------------------

ranking_indices = np.argsort(performance)[::-1]

ranked_employees = data[ranking_indices]


# --------------------------------------------------
# 8. SALARY ANALYSIS
# --------------------------------------------------

salary_median = np.median(salary)
salary_25_percentile = np.percentile(salary, 25)
salary_75_percentile = np.percentile(salary, 75)


# --------------------------------------------------
# 9. WORKING HOURS ANALYSIS
# --------------------------------------------------

average_hours = np.mean(hours)

maximum_hours = np.max(hours)
minimum_hours = np.min(hours)


# --------------------------------------------------
# 10. SAVE REPORTS
# --------------------------------------------------

np.savetxt(
    OUTPUT_DIR / "high_performers.csv",
    high_performers,
    delimiter=",",
    header="employee_id,age,salary,performance,hours,attendance",
    comments="",
    fmt="%.2f"
)

np.savetxt(
    OUTPUT_DIR / "low_attendance.csv",
    low_attendance,
    delimiter=",",
    header="employee_id,age,salary,performance,hours,attendance",
    comments="",
    fmt="%.2f"
)

np.savetxt(
    OUTPUT_DIR / "performance_ranking.csv",
    ranked_employees,
    delimiter=",",
    header="employee_id,age,salary,performance,hours,attendance",
    comments="",
    fmt="%.2f"
)

classification_data = np.column_stack(
    (employee_id, performance, performance_category)
)

np.savetxt(
    OUTPUT_DIR / "performance_categories.csv",
    classification_data,
    delimiter=",",
    header="employee_id,performance,category",
    comments="",
    fmt="%s"
)


# --------------------------------------------------
# 11. GENERATE TEXT SUMMARY
# --------------------------------------------------

report = f"""
EMPLOYEE PERFORMANCE AND SALARY ANALYZER
=========================================

GENERAL INFORMATION

Total Employees: {total_employees}
Average Age: {average_age:.2f}
Average Monthly Salary: {average_salary:.2f}
Total Monthly Salary Expenditure: {total_salary:.2f}

SALARY ANALYSIS

Highest Salary: {highest_salary:.2f}
Lowest Salary: {lowest_salary:.2f}
Median Salary: {salary_median:.2f}
25th Percentile: {salary_25_percentile:.2f}
75th Percentile: {salary_75_percentile:.2f}

PERFORMANCE ANALYSIS

Average Performance: {average_performance:.2f}
Highest Performance: {highest_performance:.2f}
Lowest Performance: {lowest_performance:.2f}

Top Employee ID: {top_employee_id}
Top Employee Score: {top_employee_score}

EMPLOYEE FILTERS

High Performers: {len(high_performers)}
Low Attendance Employees: {len(low_attendance)}
High Salary Employees: {len(high_salary_employees)}

WORKING HOURS

Average Hours: {average_hours:.2f}
Maximum Hours: {maximum_hours}
Minimum Hours: {minimum_hours}

=========================================
END OF REPORT
"""

report_path = OUTPUT_DIR / "employee_summary.txt"
report_path.write_text(report, encoding="utf-8")


# --------------------------------------------------
# 12. DISPLAY RESULTS
# --------------------------------------------------

print("\nEMPLOYEE PERFORMANCE ANALYZER")
print("=" * 40)

print("Total Employees:", total_employees)
print("Average Salary:", round(average_salary, 2))
print("Total Salary Expenditure:", total_salary)

print("\nTOP PERFORMER")
print("Employee ID:", top_employee_id)
print("Performance:", top_employee_score)

print("\nPERFORMANCE CATEGORIES")

for emp_id, score, category in zip(
    employee_id,
    performance,
    performance_category
):
    print(emp_id, score, category)

print("\nHIGH PERFORMERS")
print(high_performers[:, 0].astype(int))

print("\nLOW ATTENDANCE EMPLOYEES")
print(low_attendance[:, 0].astype(int))

print("\nPERFORMANCE RANKING")
print(ranked_employees[:, 0].astype(int))

print("\nReports saved successfully!")
print("Output folder:", OUTPUT_DIR)
