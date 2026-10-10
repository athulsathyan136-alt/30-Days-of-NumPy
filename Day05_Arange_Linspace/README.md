# Day 05 - NumPy arange and linspace

## Topics

- `np.arange()`
- `np.linspace()`
- Start, stop, and step
- Evenly spaced numerical values
- Array properties

## 1. np.arange()

Generates values using a start, stop, and step.

```python
import numpy as np

numbers = np.arange(0, 11, 2)
print(numbers)
```

Output:

```text
[ 0  2  4  6  8 10]
```

The stop value is excluded.

## 2. np.linspace()

Generates a specified number of evenly spaced values between two endpoints.

```python
numbers = np.linspace(0, 10, 5)
print(numbers)
```

Output:

```text
[ 0.   2.5  5.   7.5 10. ]
```

By default, both endpoints are included.

## Differences

- `arange()` uses a step size.
- `linspace()` uses a number of values.
- `arange()` excludes the stop value.
- `linspace()` includes the endpoints by default.

## Machine Learning Connection

These functions can generate test data, numerical ranges, and evenly spaced values for graphs and mathematical calculations.

## What I Learned

- Generate sequences with `np.arange()`.
- Generate evenly spaced values with `np.linspace()`.
- Understand the difference between step size and number of values.
- Inspect array shape and size.

## Status

Complete after running the code and exercises.