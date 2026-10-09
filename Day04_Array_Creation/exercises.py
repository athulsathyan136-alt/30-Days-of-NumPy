import numpy as np


ten_array = np.zeros(10)

print('\n=======TEN ARRAY==========')
print(ten_array)

one_array = np.ones((3,4))

print('\n======= ONE ARRAY==========')
print(one_array)

full_array = np.full((2,3),9)

print('\n======FULL ARRAY============')
print(full_array)

identity_array = np.eye(4)

print('\n=====IDENTITY ARRAY==========')
print(identity_array)

integer_array = np.zeros(5,dtype=int)
print('\n========INTEGER ARRAY==========')
print(integer_array)
print('DataType: ',integer_array.dtype)
print()