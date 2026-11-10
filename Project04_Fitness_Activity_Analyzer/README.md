# Project 04 – Fitness Activity Analyzer

A Python and NumPy project that analyzes 90 days of fitness activity data using CSV files and numerical analysis.

## Project Overview

The Fitness Activity Analyzer examines daily fitness records, including steps, calories burned, sleep duration, workout time, and water intake.

It calculates statistical summaries, tracks activity goals, compares monthly performance, and generates reports.

**Note:** The dataset contains synthetic sample data for learning purposes. It does not represent real personal health records.

## Dataset

The dataset contains 90 daily records from January 1 to March 31, 2026.

| Column | Description |
|---|---|
| Date | Activity date |
| Steps | Daily steps |
| Calories_Burned | Estimated daily calories |
| Sleep_Hours | Daily sleep duration |
| Workout_Minutes | Daily workout duration |
| Water_Liters | Daily water intake |

## Features

- Average, maximum, minimum, and median steps
- Standard deviation and percentiles
- Calories burned analysis
- Sleep duration analysis
- Workout duration analysis
- Water intake statistics
- 10,000-step goal tracking
- Most and least active days
- Sleep and steps correlation
- Monthly fitness summaries
- CSV and text report generation

## NumPy Concepts Practiced

- NumPy array creation
- `np.mean()`
- `np.median()`
- `np.max()` and