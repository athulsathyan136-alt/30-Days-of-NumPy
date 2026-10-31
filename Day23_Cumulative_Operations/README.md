# Day 23 – NumPy Cumulative Operations

## Overview

This project explores NumPy cumulative operations used to calculate running totals, running products, and differences between consecutive array elements.

## Concepts Covered

### 1. Cumulative Sum – `np.cumsum()`

Calculates the running sum of array elements.

Example:
```python
numbers = np.array([10, 20, 30, 40])
np.cumsum(numbers)
```
Output:
```text
[10 30 60 100]
```

### 2. Cumulative Product – `np.cumprod()`

Calculates the running product of array elements.

Example:
```python
numbers = np.array([2, 3, 4])
np.cumprod(numbers)
```
Output:
```text
[2 6 24]
```

### 3. Difference – `np.diff()`

Calculates the difference between consecutive elements.

Example:
```python
temperatures = np.array([20, 25, 32, 30])
np.diff(temperatures)
```
Output:
```text
[5 7 -2]
```

## Project Structure

```text
Day23_Cumulative_Operations/
│
├── cumulative_operations.py
├── exercises.py
└── README.md
```

## How to Run

Run the main program:

```bash
python cumulative_operations.py
```

Run the exercises:

```bash
python exercises.py
```

## Learning Objectives

- Understand cumulative sums.
- Calculate cumulative products.
- Find differences between consecutive values.
- Apply cumulative operations to practical datasets.

## Technologies Used

- Python
- NumPy

---

Part of my **30 Days of NumPy** learning journey.
