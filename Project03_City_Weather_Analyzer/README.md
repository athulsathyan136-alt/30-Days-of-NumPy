# Project 03: City Weather Data Analyzer

A Python and NumPy project that analyzes weather data for Kochi using numerical computing and CSV data processing.

## Project Overview

This project analyzes 61 sample weather records from January and March 2026. It calculates temperature, humidity, rainfall, and wind statistics, identifies unusual temperature readings, and exports summary reports.

**Note:** The dataset is synthetic and is intended for learning and demonstration, not as a record of actual weather observations.

## Dataset

The dataset contains the following columns:

- Date
- City
- Temperature_C
- Humidity_Percent
- Rainfall_mm
- Wind_Speed_kmh

## Features

- Temperature analysis: mean, median, maximum, minimum, and standard deviation.
- Humidity analysis and high-humidity day counting.
- Rainfall totals, averages, and heavy-rain day detection.
- Wind speed analysis.
- Monthly weather summaries.
- Temperature classification into cold, moderate, and hot days.
- 25th, 50th, and 75th percentile analysis.
- Unusual temperature detection using standard deviation.
- Export of monthly and overall weather reports.

## Technologies Used

- Python
- NumPy
- CSV module

## NumPy Concepts Practised

- NumPy arrays
- `np.mean()`
- `np.median()`
- `np.max()` and `np.min()`
- `np.std()`
- `np.sum()`
- `np.unique()`
- `np.argmax()`
- Boolean indexing
- `np.percentile()`
- `np.abs()`
- `np.where()`

## Project Structure

```text
Project03_City_Weather_Analyzer/
│
├── weather.csv
├── weather_analyzer.py
├── requirements.txt
├── README.md
│
└── outputs/
    ├── monthly_weather_summary.csv
    └── weather_summary.txt
```

## Installation

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Run the Project

```bash
python weather_analyzer.py
```

## Output Reports

The program generates:

- `outputs/monthly_weather_summary.csv` — monthly temperature, rainfall, and humidity summaries.
- `outputs/weather_summary.txt` — overall weather statistics.

## Learning Objective

The goal of this project is to develop practical NumPy skills by working with structured data, performing numerical analysis, applying conditions, and exporting results.

## Author

Athul Sathyan

GitHub: [athulsathyan136-alt](https://github.com/athulsathyan136-alt)