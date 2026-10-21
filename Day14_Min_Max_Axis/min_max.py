import numpy as np

data = np.array([
    [10, 20, 15],
    [30, 25, 35],
    [12, 18, 24]
])

print("Electricity data")
print(data)

print("\nMinimum for each house")
print(np.min(data,axis=1))

print("\nMaximum for each house")
print(np.max(data,axis=1))

print("\nMinimum for each day")
print(np.min(data,axis=0))

print("\nMaximum for each day")
print(np.max(data,axis=0))