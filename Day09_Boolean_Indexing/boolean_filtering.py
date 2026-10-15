import numpy as np

marks = np.array([45,78,92,65,88,35])

print("Original Marks:")
print(marks)

condition = marks > 80

print('Condition (marks > 80): ')
print(condition)

high_marks = marks[condition]

print('\nMarks greater than 80')
print(high_marks)

low_marks = marks[marks < 50]
print('\nMarks less than 50:')
print(low_marks)

equal_marks = marks[marks == 65]
print("\nMarks equal to 65:")
print(equal_marks)

pass_marks = marks[marks >= 70]
print("\nMarks greater than or equal to 70:")
print(pass_marks)

middle_marks = marks[(marks >= 50) & (marks <=80)]
print("\nMarks between 50 and 80:")
print(middle_marks)
