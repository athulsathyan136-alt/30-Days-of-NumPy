import numpy as np

data = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120]
])

print("Original array:")
print(data)
print('Element 70: ',data[1,2])

print('Entire second row: ',data[:1,:])
print('Entire third row: ',data[:2,:])

print('First two rows: ',data[:2,:])
print('First two columns: ',data[:,:2])
print("Requested section: ")
print(data[:2,1:3])

print('change 120 to 199')
data[-1,-1] = 999
print(data)