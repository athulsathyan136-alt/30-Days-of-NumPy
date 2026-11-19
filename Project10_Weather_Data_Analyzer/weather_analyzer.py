
import csv
import numpy as np
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data" / "weather.csv"
OUTPUT_DIR = BASE_DIR / "outputs"

OUTPUT_DIR.mkdir(exist_ok=True)


def load_weather():
    dates = []
    cities = []
    temperatures = []
    rainfall = []
    humidity = []
    wind_speed = []

    with open(DATA_FILE, "r", newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)

        for row in reader:
            dates.append(row["Date"])
            cities.append(row["City"])
            temperatures.append(float(row["Temperature"]))
            rainfall.append(float(row["Rainfall"]))
            humidity.append(float(row["Humidity"]))
            wind_speed.append(float(row["Wind_Speed"]))

    return (
        dates,
        cities,
        np.array(temperatures),
        np.array(rainfall),
        np.array(humidity),
        np.array(wind_speed)
    )


def analyze_weather(dates, cities, temp, rain, humidity, wind):

    # Temperature statistics
    average_temp = np.mean(temp)
    maximum_temp = np.max(temp)
    minimum_temp = np.min(temp)
    median_temp = np.median(temp)
    std_temp = np.std(temp)

    hottest_index = np.argmax(temp)
    coldest_index = np.argmin(temp)

    # Rainfall statistics
    total_rainfall = np.sum(rain)
    average_rainfall = np.mean(rain)
    rainy_days = rain > 0
    rainy_day_count = np.sum(rainy_days)

    # Humidity and wind statistics
    average_humidity = np.mean(humidity)
    average_wind = np.mean(wind)
    high_wind_days = np.sum(wind > 15)

    # Temperature categories
    hot_days = temp >= 33
    moderate_days = (temp >= 29) & (temp < 33)
    cool_days = temp < 29

    # Percentiles
    p25, p50, p75 = np.percentile(temp, [25, 50, 75])

    # IQR outlier analysis
    iqr = p75 - p25
    upper_limit = p75 + 1.5 * iqr
    lower_limit = p25 - 1.5 * iqr

    outliers = temp[(temp > upper_limit) | (temp < lower_limit)]

    # Weekly averages
    weekly_averages = []

    for start in range(0, len(temp), 7):
        weekly_averages.append(np.mean(temp[start:start + 7]))

    # Save daily analysis
    daily_file = OUTPUT_DIR / "daily_weather_analysis.csv"

    with open(daily_file, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Temperature", "Rainfall", "Humidity", "Wind_Speed"])

        for i in range(len(temp)):
            writer.writerow([
                dates[i], temp[i], rain[i], humidity[i], wind[i]
            ])

    # Save weekly summary
    weekly_file = OUTPUT_DIR / "weekly_summary.csv"

    with open(weekly_file, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Week", "Average_Temperature"])

        for week, average in enumerate(weekly_averages, start=1):
            writer.writerow([week, round(average, 2)])

    # Save text report
    report_file = OUTPUT_DIR / "weather_report.txt"

    with open(report_file, "w", encoding="utf-8") as file:
        file.write("WEATHER DATA ANALYZER\n")
        file.write("=" * 40 + "\n\n")

        file.write(f"City: {cities[0]}\n")
        file.write(f"Total days: {len(temp)}\n")
        file.write(f"Average temperature: {average_temp:.2f} C\n")
        file.write(f"Maximum temperature: {maximum_temp:.2f} C\n")
        file.write(f"Minimum temperature: {minimum_temp:.2f} C\n")
        file.write(f"Median temperature: {median_temp:.2f} C\n")
        file.write(f"Temperature standard deviation: {std_temp:.2f}\n\n")

        file.write(f"Total rainfall: {total_rainfall:.2f} mm\n")
        file.write(f"Average rainfall: {average_rainfall:.2f} mm\n")
        file.write(f"Rainy days: {rainy_day_count}\n")
        file.write(f"Average humidity: {average_humidity:.2f}%\n")
        file.write(f"Average wind speed: {average_wind:.2f} km/h\n")
        file.write(f"High wind days: {high_wind_days}\n\n")

        file.write(f"Hot days: {np.sum(hot_days)}\n")
        file.write(f"Moderate days: {np.sum(moderate_days)}\n")
        file.write(f"Cool days: {np.sum(cool_days)}\n\n")

        file.write("HOTTEST DAY\n")
        file.write(f"{dates[hottest_index]}: {maximum_temp} C\n\n")

        file.write("COLDEST DAY\n")
        file.write(f"{dates[coldest_index]}: {minimum_temp} C\n\n")

        file.write(f"Temperature 25th percentile: {p25:.2f}\n")
        file.write(f"Temperature 50th percentile: {p50:.2f}\n")
        file.write(f"Temperature 75th percentile: {p75:.2f}\n")
        file.write(f"IQR upper limit: {upper_limit:.2f}\n")
        file.write(f"Detected temperature outliers: {len(outliers)}\n\n")

        file.write("WEEKLY TEMPERATURE AVERAGES\n")
        for week, average in enumerate(weekly_averages, start=1):
            file.write(f"Week {week}: {average:.2f} C\n")

    # Display results
    print("\nWEATHER DATA ANALYZER")
    print("=" * 40)

    print(f"City: {cities[0]}")
    print(f"Total days: {len(temp)}")
    print(f"Average temperature: {average_temp:.2f} C")
    print(f"Maximum temperature: {maximum_temp:.2f} C")
    print(f"Minimum temperature: {minimum_temp:.2f} C")
    print(f"Median temperature: {median_temp:.2f} C")

    print(f"\nTotal rainfall: {total_rainfall:.2f} mm")
    print(f"Rainy days: {rainy_day_count}")
    print(f"Average humidity: {average_humidity:.2f}%")
    print(f"Average wind speed: {average_wind:.2f} km/h")
    print(f"High wind days: {high_wind_days}")

    print("\nTEMPERATURE CATEGORIES")
    print(f"Hot days: {np.sum(hot_days)}")
    print(f"Moderate days: {np.sum(moderate_days)}")
    print(f"Cool days: {np.sum(cool_days)}")

    print("\nWEEKLY TEMPERATURE AVERAGES")
    for week, average in enumerate(weekly_averages, start=1):
        print(f"Week {week}: {average:.2f} C")

    print(f"\nDetected temperature outliers: {len(outliers)}")
    print("\nReports generated successfully!")


def main():
    data = load_weather()
    analyze_weather(*data)


if __name__ == "__main__":
    main()
