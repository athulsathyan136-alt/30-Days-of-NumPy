
import numpy as np

# Load dataset
data = np.genfromtxt(
    "data/energy_data.csv",
    delimiter=",",
    skip_header=1
)

days = data[:, 0].astype(int)
consumption = data[:, 1]

# 1. Basic statistics
total_consumption = np.sum(consumption)
average_consumption = np.mean(consumption)
median_consumption = np.median(consumption)
standard_deviation = np.std(consumption)

print("\n===== ENERGY CONSUMPTION ANALYSIS =====")

print("Total consumption:", total_consumption, "kWh")
print("Average consumption:", average_consumption, "kWh")
print("Median consumption:", median_consumption, "kWh")
print("Standard deviation:", standard_deviation)

# 2. Highest and lowest consumption
highest_position = np.argmax(consumption)
lowest_position = np.argmin(consumption)

print("\n===== PEAK CONSUMPTION =====")

print("Highest consumption:", consumption[highest_position])
print("Highest consumption day:", days[highest_position])

print("Lowest consumption:", consumption[lowest_position])
print("Lowest consumption day:", days[lowest_position])

# 3. Daily consumption changes
daily_changes = np.diff(consumption)

print("\n===== DAILY CHANGES =====")

print("Daily changes:", daily_changes)

# Insert zero for the first day
daily_changes = np.insert(daily_changes, 0, 0)

# 4. Cumulative consumption
cumulative_consumption = np.cumsum(consumption)

print("\n===== CUMULATIVE CONSUMPTION =====")

print(cumulative_consumption)

# 5. Anomaly detection
threshold = average_consumption + (2 * standard_deviation)

anomaly_positions = np.where(consumption > threshold)[0]

print("\n===== ANOMALY DETECTION =====")

print("Anomaly threshold:", threshold)
print("Unusual consumption days:")

for position in anomaly_positions:
    print(
        "Day:", days[position],
        "Consumption:", consumption[position]
    )

# 6. Consumption percentiles
print("\n===== CONSUMPTION DISTRIBUTION =====")

print("25th percentile:", np.percentile(consumption, 25))
print("50th percentile:", np.percentile(consumption, 50))
print("90th percentile:", np.percentile(consumption, 90))

# 7. Peak day contribution
peak_percentage = (
    consumption[highest_position] / total_consumption
) * 100

print("\nPeak day contribution:", peak_percentage, "%")

# 8. Consumption increase and decrease
increase_days = np.where(daily_changes > 0)[0]
decrease_days = np.where(daily_changes < 0)[0]

print("\nDays with increased consumption:", len(increase_days))
print("Days with decreased consumption:", len(decrease_days))

# 9. Save daily analysis
report = np.column_stack((
    days,
    consumption,
    daily_changes,
    cumulative_consumption
))

np.savetxt(
    "outputs/energy_analysis.csv",
    report,
    delimiter=",",
    fmt="%.2f",
    header="Day,Consumption_kWh,Daily_Change,Cumulative_Consumption",
    comments=""
)

print("\nEnergy report saved successfully!")
