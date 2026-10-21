
import numpy as np

temperatures = np.array([
    [28, 30, 29],
    [32, 35, 31],
    [25, 27, 26]
])

print("Temperatures:")
print(temperatures)

# Exercise 1: Find the maximum temperature for each day (each row)
print("maximum temperature for each day")
print(np.max(temperatures,axis=0))

# Exercise 2: Find the minimum temperature for each day (each row)

print("minimum temperature for each day")
print(np.min(temperatures,axis=0))

# Exercise 3: Find the average temperature for each day (each row)

print("average temperature for each day")
print(np.mean(temperatures,axis=0))

# Exercise 4: Find the highest temperature across all values

print("highest temperature across all values")
print(np.max(temperatures))
# Exercise 5: Find the lowest temperature across all values
print("lowest temperature across all values")
print(np.min(temperatures))