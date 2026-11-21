
import numpy as np

# Load weather dataset
data = np.genfromtxt(
    "data/weather_data.csv",
    delimiter=",",
    skip_header=1
)

# Extract columns
days = data[:, 0]
temperature = data[:, 1]
humidity = data[:, 2]
rainfall = data[:, 3]

# Temperature analysis
average_temp = np.mean(temperature)
median_temp = np.median(temperature)
highest_temp = np.max(temperature)
lowest_temp = np.min(temperature)

hottest_day = np.argmax(temperature)
coldest_day = np.argmin(temperature)

# Humidity analysis
average_humidity = np.mean(humidity)

# Rainfall analysis
total_rainfall = np.sum(rainfall)
average_rainfall = np.mean(rainfall)
maximum_rainfall = np.max(rainfall)

rainy_days = np.count_nonzero(rainfall > 0)

# Display results
print("\n===== WEATHER DATA ANALYZER =====")

print("\nTEMPERATURE")
print("Average:", average_temp)
print("Median:", median_temp)
print("Highest:", highest_temp)
print("Lowest:", lowest_temp)
print("Hottest day:", int(days[hottest_day]))
print("Coldest day:", int(days[coldest_day]))

print("\nHUMIDITY")
print("Average humidity:", average_humidity)

print("\nRAINFALL")
print("Total rainfall:", total_rainfall)
print("Average rainfall:", average_rainfall)
print("Maximum rainfall:", maximum_rainfall)
print("Number of rainy days:", rainy_days)

# Save summary
report = np.array([
    average_temp,
    median_temp,
    highest_temp,
    lowest_temp,
    average_humidity,
    total_rainfall,
    average_rainfall,
    maximum_rainfall,
    rainy_days
])

np.savetxt(
    "outputs/weather_report.txt",
    report,
    fmt="%.2f"
)

print("\nReport saved successfully!")
