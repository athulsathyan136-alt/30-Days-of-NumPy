
import csv
import numpy as np
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data" / "fitness.csv"
OUTPUT_DIR = BASE_DIR / "outputs"

OUTPUT_DIR.mkdir(exist_ok=True)


def load_data():
    dates = []
    steps = []
    calories = []
    sleep = []
    water = []
    workout = []

    with open(DATA_FILE, "r", newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)

        for row in reader:
            dates.append(row["Date"])
            steps.append(float(row["Steps"]))
            calories.append(float(row["Calories"]))
            sleep.append(float(row["Sleep_Hours"]))
            water.append(float(row["Water_Liters"]))
            workout.append(float(row["Workout_Minutes"]))

    return (
        dates,
        np.array(steps),
        np.array(calories),
        np.array(sleep),
        np.array(water),
        np.array(workout)
    )


def analyze_fitness(dates, steps, calories, sleep, water, workout):

    # Basic statistics
    average_steps = np.mean(steps)
    maximum_steps = np.max(steps)
    minimum_steps = np.min(steps)

    average_calories = np.mean(calories)
    average_sleep = np.mean(sleep)
    average_water = np.mean(water)
    average_workout = np.mean(workout)

    # Find the most and least active days
    most_active_index = np.argmax(steps)
    least_active_index = np.argmin(steps)

    # Fitness goals
    goal_days = steps >= 10000
    goal_count = np.sum(goal_days)

    workout_goal_days = workout >= 30
    workout_count = np.sum(workout_goal_days)

    # Sleep analysis
    low_sleep_days = sleep < 7
    low_sleep_count = np.sum(low_sleep_days)

    # Weekly averages (each week has up to 7 records)
    weekly_step_averages = []

    for start in range(0, len(steps), 7):
        weekly_steps = steps[start:start + 7]
        weekly_step_averages.append(np.mean(weekly_steps))

    # Correlation between steps and calories
    correlation = np.corrcoef(steps, calories)[0, 1]

    # Save weekly summary
    weekly_file = OUTPUT_DIR / "weekly_summary.csv"

    with open(weekly_file, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Week", "Average_Steps"])

        for week, average in enumerate(weekly_step_averages, start=1):
            writer.writerow([week, round(average, 2)])

    # Save text report
    report_file = OUTPUT_DIR / "fitness_report.txt"

    with open(report_file, "w", encoding="utf-8") as file:
        file.write("FITNESS DATA ANALYZER\n")
        file.write("=" * 40 + "\n\n")

        file.write(f"Total days: {len(steps)}\n")
        file.write(f"Average steps: {average_steps:.2f}\n")
        file.write(f"Maximum steps: {maximum_steps:.0f}\n")
        file.write(f"Minimum steps: {minimum_steps:.0f}\n")
        file.write(f"Average calories: {average_calories:.2f}\n")
        file.write(f"Average sleep: {average_sleep:.2f} hours\n")
        file.write(f"Average water: {average_water:.2f} liters\n")
        file.write(f"Average workout: {average_workout:.2f} minutes\n\n")

        file.write(f"Days with 10,000+ steps: {goal_count}\n")
        file.write(f"Days with 30+ workout minutes: {workout_count}\n")
        file.write(f"Days with less than 7 hours sleep: {low_sleep_count}\n")
        file.write(f"Steps-calories correlation: {correlation:.3f}\n\n")

        file.write("MOST ACTIVE DAY\n")
        file.write(f"{dates[most_active_index]}: {maximum_steps:.0f} steps\n\n")

        file.write("LEAST ACTIVE DAY\n")
        file.write(f"{dates[least_active_index]}: {minimum_steps:.0f} steps\n\n")

        file.write("WEEKLY AVERAGE STEPS\n")
        for week, average in enumerate(weekly_step_averages, start=1):
            file.write(f"Week {week}: {average:.2f}\n")

    # Display results
    print("\nFITNESS DATA ANALYZER")
    print("=" * 40)

    print(f"Total days: {len(steps)}")
    print(f"Average steps: {average_steps:.2f}")
    print(f"Maximum steps: {maximum_steps:.0f}")
    print(f"Minimum steps: {minimum_steps:.0f}")
    print(f"Average calories: {average_calories:.2f}")
    print(f"Average sleep: {average_sleep:.2f} hours")
    print(f"Average water: {average_water:.2f} liters")
    print(f"Average workout: {average_workout:.2f} minutes")

    print("\nFITNESS GOALS")
    print(f"Days with 10,000+ steps: {goal_count}")
    print(f"Days with 30+ workout minutes: {workout_count}")
    print(f"Days with less than 7 hours sleep: {low_sleep_count}")

    print("\nWEEKLY AVERAGE STEPS")
    for week, average in enumerate(weekly_step_averages, start=1):
        print(f"Week {week}: {average:.2f}")

    print(f"\nSteps-calories correlation: {correlation:.3f}")
    print("\nReports generated successfully!")


def main():
    data = load_data()
    analyze_fitness(*data)


if __name__ == "__main__":
    main()
