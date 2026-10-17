import numpy as np

marks = np.array([35, 82, 47, 90, 66, 28, 75])

print("Original marks: ")
print(marks)

postions = np.where(marks>60)
print("\nIndexes where marks > 60:")
print(postions)

print("\nMarks above 60: ")
print(marks[marks >60])

result = np.where(marks>=50,"Pass","Fail")
print("\nExam Result: ")
print(result)

updated = np.where(marks<50,0,marks)
print("\nMarks after replacing failures with zero:")
print(updated)

bonus_marks = np.where(marks < 50, marks + 5, marks)
print("\nMarks after conditional bonus:")
print(bonus_marks)