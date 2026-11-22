
import numpy as np

# Load dataset
data = np.genfromtxt(
    "data/employees.csv",
    delimiter=",",
    skip_header=1,
    dtype=None,
    encoding="utf-8"
)

# Extract columns
employee_ids = data["f0"]
departments = data["f1"]
experience = data["f2"]
salaries = data["f3"]
performance = data["f4"]

# 1. Overall salary analysis
print("\n===== SALARY ANALYSIS =====")

average_salary = np.mean(salaries)
median_salary = np.median(salaries)
minimum_salary = np.min(salaries)
maximum_salary = np.max(salaries)
salary_std = np.std(salaries)

print("Average salary:", average_salary)
print("Median salary:", median_salary)
print("Minimum salary:", minimum_salary)
print("Maximum salary:", maximum_salary)
print("Salary standard deviation:", salary_std)

# 2. Salary percentiles
print("\n===== SALARY DISTRIBUTION =====")

print("25th percentile:", np.percentile(salaries, 25))
print("50th percentile:", np.percentile(salaries, 50))
print("75th percentile:", np.percentile(salaries, 75))

# 3. Highest and lowest paid employees
highest_position = np.argmax(salaries)
lowest_position = np.argmin(salaries)

print("\n===== EMPLOYEE ANALYSIS =====")

print("Highest-paid employee:", employee_ids[highest_position])
print("Highest salary:", salaries[highest_position])

print("Lowest-paid employee:", employee_ids[lowest_position])
print("Lowest salary:", salaries[lowest_position])

# 4. Department analysis
print("\n===== DEPARTMENT ANALYSIS =====")

unique_departments = np.unique(departments)

department_averages = []

for department in unique_departments:

    selected = departments == department

    average = np.mean(salaries[selected])
    department_averages.append(average)

    print(department, "Average salary:", average)

department_averages = np.array(department_averages)

best_department = np.argmax(department_averages)

print("Highest-paying department:",
      unique_departments[best_department])

# 5. Performance analysis
print("\n===== PERFORMANCE ANALYSIS =====")

high_performers = np.where(performance >= 85)[0]

print("High-performing employees:", len(high_performers))

# 6. Promotion eligibility
promotion_positions = np.where(
    (experience >= 5) & (performance >= 85)
)[0]

print("\n===== PROMOTION ANALYSIS =====")

print("Eligible employees:")

for position in promotion_positions:
    print(employee_ids[position])

# 7. Performance categories
conditions = [
    performance >= 90,
    performance >= 80,
    performance >= 70
]

choices = ["Excellent", "Good", "Average"]

ratings = np.select(
    conditions,
    choices,
    default="Needs Improvement"
)

print("\n===== PERFORMANCE RATINGS =====")

for i in range(len(employee_ids)):
    print(employee_ids[i], ratings[i])

# 8. Experience and salary correlation
correlation = np.corrcoef(experience, salaries)[0, 1]

print("\nExperience-salary correlation:", correlation)

# 9. Top five highest-paid employees
ranking = np.argsort(salaries)[::-1]

print("\n===== TOP FIVE EMPLOYEES =====")

for position in ranking[:5]:
    print(
        employee_ids[position],
        salaries[position]
    )

# 10. Save employee report
employee_report = np.column_stack((
    employee_ids,
    departments,
    experience,
    salaries,
    performance,
    ratings
))

np.savetxt(
    "outputs/employee_report.csv",
    employee_report,
    delimiter=",",
    fmt="%s",
    header="Employee_ID,Department,Experience,Salary,Performance,Rating",
    comments=""
)

# Save department report
department_report = np.column_stack((
    unique_departments,
    department_averages
))

np.savetxt(
    "outputs/department_report.csv",
    department_report,
    delimiter=",",
    fmt="%s",
    header="Department,Average_Salary",
    comments=""
)

print("\nReports saved successfully!")
