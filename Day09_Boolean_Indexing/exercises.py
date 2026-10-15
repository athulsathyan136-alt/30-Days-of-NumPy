
import numpy as np

data = np.array([12, 45, 67, 23, 89, 34, 90, 56, 10, 75])

print("Original array:")
print(data)

# Exercise 1: Select all values greater than 50
print('all values greater than 50: ')
print(data[data>50])

# Exercise 2: Select all values less than 30

print('all values less than 30: ')
print(data[data < 30])
# Exercise 3: Select all even numbers
print('Select all even numbers')
even = data %2 ==0
print(data[even])

# Exercise 4: Select values between 30 and 70,
# including both 30 and 70

print('Select values between 30 and 70,including both 30 and 70:')
middle = data[(data >= 30)&(data<=70)]
print(middle)
# Exercise 5: Select all values that are NOT equal to 45
print('all values that are NOT equal to 45')
not_45 = data[data != 45]
print(not_45)
