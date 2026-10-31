# Day 24 – NumPy Data Types and Type Conversion

## Overview
This project explores NumPy data types and how to convert arrays from one data type to another.

## Concepts Covered
- Checking array data types using `dtype`
- Understanding integer and floating-point data types
- Converting data types using `astype()`
- Converting integers to floats
- Converting floats to integers
- Understanding decimal truncation during integer conversion
- Checking array properties using `ndim`, `shape`, and `size`

## Project Structure

```text
Day24_Data_Types_Conversion/
├── data_types.py
├── exercises.py
└── README.md
```

## Run the Programs

```bash
python data_types.py
python exercises.py
```

## Key Learning

The NumPy `astype()` method converts an array into a specified data type.

For example:

```python
numbers.astype(float)
```

Converting floating-point values to integers with `astype(int)` removes the decimal part rather than rounding the value.

## Learning Progress
Day 24 of 30 Days of NumPy completed.
