
import numpy as np

data = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print("Original 2D array:")
print(data)

flat = data.flatten()

print("\nUsing flatten():")
print(flat)

raw = data.ravel()

print("\nUsing Ravel():")
print(raw)

print("\nOriginal shape:", data.shape)
print("Flattened shape:", flat.shape)