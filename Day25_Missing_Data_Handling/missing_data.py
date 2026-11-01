import numpy as np

# Original temperature readings
temperatures = np.array([25.0, 30.0, np.nan, 35.0, np.nan])

print("Original temperatures:", temperatures)

# Detect missing values
missing = np.isnan(temperatures)
print("Missing value positions:", missing)

# Count missing values
missing_count = np.count_nonzero(missing)
print("Number of missing values:", missing_count)

# Calculate mean without missing values
valid_values = temperatures[~np.isnan(temperatures)]
average = np.mean(valid_values)
print("Average temperature:", average)

# Replace missing values with mean
cleaned = np.where(np.isnan(temperatures), average, temperatures)
print("Cleaned temperatures:", cleaned)