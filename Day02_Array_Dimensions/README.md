# Day 02 - NumPy Array Dimensions

## Topics

- 1D arrays
- 2D arrays
- 3D arrays
- `ndim`
- `shape`
- `size`
- Understanding rows and columns
- Understanding dimensions in Machine Learning datasets

## 1D Array

A 1D array is a single sequence of values.

```python
import numpy as np

array_1d = np.array([10, 20, 30, 40, 50])

print(array_1d)
print(array_1d.ndim)
print(array_1d.shape)
print(array_1d.size)