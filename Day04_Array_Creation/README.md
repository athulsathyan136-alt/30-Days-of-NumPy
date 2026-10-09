# Day 04 - NumPy Array Creation

## Topics

* `np.zeros()`
* `np.ones()`
* `np.full()`
* `np.eye()`
* Specifying a data type with `dtype`

## Examples

```python
import numpy as np

print(np.zeros(5))
print(np.ones((2, 3)))
print(np.full((3, 2), 7))
print(np.eye(3))
print(np.zeros(4, dtype=int))
```

## What I Learned

* `np.zeros()` creates an array of zeros.
* `np.ones()` creates an array of ones.
* `np.full()` fills an array with a chosen value.
* `np.eye()` creates an identity matrix.
* `dtype=int` creates integer values instead of floating-point values.

## Machine Learning Connection

Array creation functions are useful for initializing arrays, creating test data, and building matrices for mathematical operations in machine learning.

## Status

Completed after running the code and exercises.
