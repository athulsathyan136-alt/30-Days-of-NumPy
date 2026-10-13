import numpy as np

numbers = np.array([5, 10, 15, 20, 25, 30, 35])

print('First element: ',numbers[0])

print('Last element: ',numbers[-1])

print(numbers[1:4])

print('Every second element: ',numbers[::2])

print('reverse array :',numbers[::-1])

matrix = np.arange(1,10).reshape(3,3)
print(matrix)

print('Number 5: ',matrix[1,1])