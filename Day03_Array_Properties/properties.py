import numpy as np

numbers = np.array([[10,20,30],[40,50,60,]])

print('=======ARRAY=========')
print(numbers)

print('\n===========PROPERTIES============')

print('Number of dimensions: ',numbers.ndim)

print('Shape: ',numbers.shape)

print('Total elements: ',numbers.size)

print('Data Type: ',numbers.dtype)

print('Byte per elements: ',numbers.itemsize)

print('Total bytes: ',numbers.nbytes)
