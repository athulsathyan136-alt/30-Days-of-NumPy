import numpy as np
import csv
import os

dates = []
cities = []
temperatures = []
humidity = []
rainfall = []
wind_speed = []

with open("weather.csv", "r", newline="", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)
    for row in reader:
        dates.append(row["Date"])
        cities.append(row["City"])
        temperatures.append(float(row["Temperature_C"]))
        humidity.append(float(row["Humidity_Percent"]))
        rainfall.append(float(row["Rainfall_mm"]))
        wind_speed.append(float(row["Wind_Speed_kmh"]))

# Convert numerical data into NumPy arrays
temperatures = np.array(temperatures)
humidity = np.array(humidity)
rainfall = np.array(rainfall)
wind_speed = np.array(wind_speed)

dates = np.array(dates)
cities = np.array(cities)

print("\n========== CITY WEATHER ANALYZER ==========")
print("Total Weather Records:", len(dates))
print("Cities:", np.unique(cities))

# ==========================================
# 2. TEMPERATURE ANALYSIS
# ==========================================

print("\n========== TEMPERATURE ANALYSIS ==========")

print("Average Temperature:", round(np.mean(temperatures), 2), "°C")
print("Median Temperature:", np.median(temperatures), "°C")
print("Maximum Temperature:", np.max(temperatures), "°C")
print("Minimum Temperature:", np.min(temperatures), "°C")
print("Temperature Standard Deviation:",
      round(np.std(temperatures), 2), "°C")

# Hottest and coldest days
hottest_index = np.argmax(temperatures)
coldest_index = np.argmin(temperatures)

print("\nHottest Day:", dates[hottest_index])
print("Hottest Temperature:", temperatures[hottest_index], "°C")

print("\nColdest Day:", dates[coldest_index])
print("Coldest Temperature:", temperatures[coldest_index], "°C")

# ==========================================
# 3. HUMIDITY ANALYSIS
# ==========================================

print("\n========== HUMIDITY ANALYSIS ==========")

print("Average Humidity:", round(np.mean(humidity), 2), "%")
print("Highest Humidity:", np.max(humidity), "%")
print("Lowest Humidity:", np.min(humidity), "%")

high_humidity = humidity > 80

print("Days with Humidity Above 80%:",
      np.sum(high_humidity))

# ==========================================
# 4. RAINFALL ANALYSIS
# ==========================================

print("\n========== RAINFALL ANALYSIS ==========")

print("Total Rainfall:", np.sum(rainfall), "mm")
print("Average Rainfall:", round(np.mean(rainfall), 2), "mm")
print("Maximum Rainfall:", np.max(rainfall), "mm")

rainy_days = rainfall > 0
heavy_rain_days = rainfall >= 10

print("Rainy Days:", np.sum(rainy_days))
print("Heavy Rain Days:", np.sum(heavy_rain_days))

rainiest_index = np.argmax(rainfall)

print("Rainiest Date:", dates[rainiest_index])
print("Rainiest Amount:", rainfall[rainiest_index], "mm")

# ==========================================
# 5. WIND SPEED ANALYSIS
# ==========================================

print("\n========== WIND SPEED ANALYSIS ==========")

print("Average Wind Speed:",
      round(np.mean(wind_speed), 2), "km/h")

print("Maximum Wind Speed:", np.max(wind_speed), "km/h")
print("Minimum Wind Speed:", np.min(wind_speed), "km/h")

windy_days = wind_speed > 15

print("Days with Wind Above 15 km/h:",
      np.sum(windy_days))

# ==========================================
# 6. MONTHLY WEATHER ANALYSIS
# ==========================================

print("\n========== MONTHLY ANALYSIS ==========")

months = np.array([date[:7] for date in dates])
unique_months = np.unique(months)

for month in unique_months:
    monthly_mask = months == month

    monthly_temp = temperatures[monthly_mask]
    monthly_rain = rainfall[monthly_mask]
    monthly_humidity = humidity[monthly_mask]

    print("\nMonth:", month)
    print("Average Temperature:",
          round(np.mean(monthly_temp), 2), "°C")
    print("Total Rainfall:",
          np.sum(monthly_rain), "mm")
    print("Average Humidity:",
          round(np.mean(monthly_humidity), 2), "%")

# ==========================================
# 7. TEMPERATURE RANGE CLASSIFICATION
# ==========================================

print("\n========== TEMPERATURE CLASSIFICATION ==========")

cold_days = temperatures < 29
moderate_days = (temperatures >= 29) & (temperatures <= 32)
hot_days = temperatures > 32

print("Cold Days:", np.sum(cold_days))
print("Moderate Days:", np.sum(moderate_days))
print("Hot Days:", np.sum(hot_days))

# ==========================================
# 8. PERCENTILE ANALYSIS
# ==========================================

print("\n========== PERCENTILE ANALYSIS ==========")

print("25th Percentile:",
      np.percentile(temperatures, 25), "°C")

print("50th Percentile:",
      np.percentile(temperatures, 50), "°C")

print("75th Percentile:",
      np.percentile(temperatures, 75), "°C")

# ==========================================
# 9. DETECT UNUSUAL TEMPERATURES
# ==========================================

print("\n========== UNUSUAL TEMPERATURES ==========")

temperature_mean = np.mean(temperatures)
temperature_std = np.std(temperatures)

unusual_mask = (
    np.abs(temperatures - temperature_mean)
    > 2 * temperature_std
)

print("Unusual Temperature Records:",
      np.sum(unusual_mask))

for index in np.where(unusual_mask)[0]:
    print(dates[index], temperatures[index], "°C")

# ==========================================
# 10. SAVE ANALYSIS OUTPUTS
# ==========================================

os.makedirs("outputs", exist_ok=True)

monthly_results = []

for month in unique_months:
    mask = months == month

    monthly_results.append([
        month,
        round(float(np.mean(temperatures[mask])), 2),
        round(float(np.sum(rainfall[mask])), 2),
        round(float(np.mean(humidity[mask])), 2)
    ])

with open("outputs/monthly_weather_summary.csv",
          "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow([
        "Month",
        "Average_Temperature_C",
        "Total_Rainfall_mm",
        "Average_Humidity_Percent"
    ])

    writer.writerows(monthly_results)

with open("outputs/weather_summary.txt", "w") as file:
    file.write("CITY WEATHER ANALYSIS SUMMARY\n")
    file.write("==============================\n")
    file.write(f"Records: {len(dates)}\n")
    file.write(f"Average Temperature: {np.mean(temperatures):.2f} C\n")
    file.write(f"Total Rainfall: {np.sum(rainfall):.2f} mm\n")
    file.write(f"Average Humidity: {np.mean(humidity):.2f}%\n")
    file.write(f"Average Wind Speed: {np.mean(wind_speed):.2f} km/h\n")

print("\n========== EXPORT COMPLETE ==========")
print("Monthly summary saved.")
print("Weather summary saved.")
print("\nWeather analysis completed successfully!")
