import csv
import numpy as np
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "fitness.csv"
OUTPUT_DIR = BASE_DIR / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

# Load dataset
dates = []
steps = []
calories = []
sleep = []
workout = []
water = []

with open(DATA_FILE, "r", encoding="utf-8-sig", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        dates.append(row["Date"])
        steps.append(int(row["Steps"]))
        calories.append(float(row["Calories_Burned"]))
        sleep.append(float(row["Sleep_Hours"]))
        workout.append(int(row["Workout_Minutes"]))
        water.append(float(row["Water_Liters"]))

# Convert lists into NumPy arrays
steps = np.array(steps)
calories = np.array(calories)
sleep = np.array(sleep)
workout = np.array(workout)
water = np.array(water)

# Overall statistics
print("\n========== FITNESS ACTIVITY ANALYZER ==========")
print("Total Days:", len(dates))

print("\n--- Daily Activity Statistics ---")
print("Average Steps:", round(np.mean(steps), 2))
print("Maximum Steps:", np.max(steps))
print("Minimum Steps:", np.min(steps))
print("Median Steps:", np.median(steps))
print("Step Standard Deviation:", round(np.std(steps), 2))

print("\n--- Calories ---")
print("Average Calories:", round(np.mean(calories), 2))
print("Maximum Calories:", np.max(calories))
print("Minimum Calories:", np.min(calories))

print("\n--- Sleep ---")
print("Average Sleep Hours:", round(np.mean(sleep), 2))
print("Days with Less Than 7 Hours:", np.sum(sleep < 7))

print("\n--- Workout ---")
print("Average Workout Minutes:", round(np.mean(workout), 2))
print("Total Workout Minutes:", np.sum(workout))
print("Days with at Least 30 Minutes:", np.sum(workout >= 30))

print("\n--- Water Intake ---")
print("Average Water Intake:", round(np.mean(water), 2), "liters")

# Step goal analysis
step_goal = 10000
goal_days = np.sum(steps >= step_goal)
goal_percentage = (goal_days / len(steps)) * 100

print("\n--- Step Goal ---")
print("Daily Goal:", step_goal)
print("Days Achieved:", goal_days)
print("Goal Achievement:", round(goal_percentage, 2), "%")

# Most and least active days
best_index = np.argmax(steps)
least_index = np.argmin(steps)

print("\n--- Activity Highlights ---")
print("Most Active Day:", dates[best_index], "-", steps[best_index], "steps")
print("Least Active Day:", dates[least_index], "-", steps[least_index], "steps")

# Percentiles
print("\n--- Step Percentiles ---")
print("25th Percentile:", np.percentile(steps, 25))
print("50th Percentile:", np.percentile(steps, 50))
print("75th Percentile:", np.percentile(steps, 75))

# Correlation analysis
sleep_steps_correlation = np.corrcoef(sleep, steps)[0, 1]

print("\n--- Correlation ---")
print("Sleep vs Steps:", round(sleep_steps_correlation, 3))

# Monthly analysis
monthly_data = {}

for index, date in enumerate(dates):
    month = date[:7]

    if month not in monthly_data:
        monthly_data[month] = {
            "steps": [],
            "calories": [],
            "workout": []
        }

    monthly_data[month]["steps"].append(steps[index])
    monthly_data[month]["calories"].append(calories[index])
    monthly_data[month]["workout"].append(workout[index])

monthly_rows = []

print("\n--- Monthly Summary ---")

for month, values in monthly_data.items():
    average_steps = np.mean(values["steps"])
    average_calories = np.mean(values["calories"])
    total_workout = np.sum(values["workout"])

    print(
        month,
        "| Average Steps:", round(average_steps, 2),
        "| Average Calories:", round(average_calories, 2),
        "| Total Workout:", total_workout
    )

    monthly_rows.append([
        month,
        round(average_steps, 2),
        round(average_calories, 2),
        int(total_workout)
    ])

# Save monthly CSV report
monthly_file = OUTPUT_DIR / "monthly_fitness_summary.csv"

with open(monthly_file, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow([
        "Month",
        "Average_Steps",
        "Average_Calories",
        "Total_Workout_Minutes"
    ])
    writer.writerows(monthly_rows)

# Save text report
summary_file = OUTPUT_DIR / "fitness_summary.txt"

with open(summary_file, "w", encoding="utf-8") as file:
    file.write("FITNESS ACTIVITY ANALYSIS REPORT\n")
    file.write("================================\n")
    file.write(f"Total Days: {len(dates)}\n")
    file.write(f"Average Steps: {np.mean(steps):.2f}\n")
    file.write(f"Average Calories: {np.mean(calories):.2f}\n")
    file.write(f"Average Sleep: {np.mean(sleep):.2f} hours\n")
    file.write(f"Average Workout: {np.mean(workout):.2f} minutes\n")
    file.write(f"Average Water: {np.mean(water):.2f} liters\n")
    file.write(f"Step Goal Achievement: {goal_percentage:.2f}%\n")
    file.write(f"Sleep-Steps Correlation: {sleep_steps_correlation:.3f}\n")

print("\nReports saved successfully!")
print("Monthly report:", monthly_file)
print("Text report:", summary_file)

