
import numpy as np

# Exercise 1:
# Create a 5x3 student marks array.
# Calculate the average of each subject.
marks = np.array([[1,2,3],[6,7,8],[11,12,13],[15,16,17],[18,19,20]])
avg = np.nanmean(marks,axis=0)
print("Average Marks: ",avg)
# Exercise 2:
# Detect all missing values using np.isnan().
print("Missing values: ",np.isnan(marks))
# Exercise 3:
# Replace missing values with the average
# of their respective columns.
mark = np.array([
    [10, 20, 30],
    [40, 0, 60],
    [70, 80, 90]
], dtype=float)
sub = np.nanmean(mark,axis=0)
missing = np.where(np.isnan(mark),sub,mark)

print("Missing value with avg: ",missing)
# Exercise 4:
# Find the highest average score.
student = np.mean(mark,axis=1)
best = np.max(student)
print("Highest average score ",best)
# Exercise 5:
# Rank students from highest to lowest.
students = np.mean(marks,axis=1)
rank = np.argsort(students)[::-1]
print("Student ranking (highest to lowest):", rank)
print("Ranked averages:", students[rank])
# Exercise 6:
# Calculate the standard deviation
# of each subject.
std = np.std(marks,axis=0)
print("Standard deviation of each subject:", std)
# Exercise 7:
# Use np.where() to classify students:
# Average >= 50: PASS
# Average < 50: FAIL
cal = np.mean(marks,axis=1)
result = np.where(avg>=50,"Pass","Fail")
print("Student averages:", cal)
print("Student results:", result)
# Exercise 8:
# Calculate weighted scores using np.dot().
weight = np.dot(marks,mark)
print("Weighted scores: ",weight)