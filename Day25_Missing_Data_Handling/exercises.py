import numpy as np

# Exercise 1: Detect missing values
scores = np.array([80.0, np.nan, 90.0, 70.0, np.nan])

missing_positions = np.isnan(scores)

print("Original scores:", scores)
print("Missing positions:", missing_positions)

# Exercise 2: Count missing values
missing_count = np.count_nonzero(missing_positions)

print("Number of missing values:", missing_count)

# Exercise 3: Calculate average while ignoring missing values
average_score = np.nanmean(scores)

print("Average score:", average_score)

# Exercise 4: Replace missing values with the average
cleaned_scores = np.where(
    np.isnan(scores),
    average_score,
    scores
)

print("Cleaned scores:", cleaned_scores)