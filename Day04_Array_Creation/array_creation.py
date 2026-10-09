import numpy as np

zero_array = np.zeros(5)

print('\n======ZERO ARRAY==========')
print(zero_array)

one_array = np.ones((2,3))

print('\n=======ONE ARRAY=========')
print(one_array)

full_array = np.full((3,3),5)

print('\n=======FULL ARRAY=========')
print(full_array)

identity_matrix = np.eye(3)

print('\n========IDENTITY MATRIX==========')
print(identity_matrix)

ineger_zero = np.zeros(4, dtype=int)

print('\n=====INTEGER ZEROS=========')
print(ineger_zero)
print('Data type :',ineger_zero.dtype)
print()