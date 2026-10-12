# Day 6 — NumPy Random Numbers 🎲

## 📌 Overview
In Day 6 of my 30 Days of NumPy challenge, I learned how to generate random numbers, create random arrays, and select random elements using NumPy.

## 🎯 Learning Objectives
- Generate random integers using `np.random.randint()`
- Generate random decimal values using `np.random.random()`
- Create 2D arrays containing random numbers
- Use random seeds to reproduce results
- Select random elements using `np.random.choice()`
- Generate random decimal values within a specified range using `np.random.uniform()`
- Inspect NumPy array properties

## 📚 Concepts Learned

### 1. Random Integers
```python
np.random.randint(1, 50, size=10)
```
Generates 10 random integers from 1 to 49.

### 2. Random Decimal Numbers
```python
np.random.random(size=(3, 3))
```
Creates a 3 × 3 array of random decimals between 0 (inclusive) and 1 (exclusive).

### 3. Random Numbers Within a Range
```python
np.random.uniform(1, 100, size=(3, 3))
```
Generates random decimal values from 1 up to, but not including, 100.

### 4. Random Selection
```python
np.random.choice(fruits, size=3, replace=False)
```
Selects three unique array positions without replacement.

### 5. Reproducible Random Numbers
```python
np.random.seed(42)
```
Sets the random seed so the same sequence can be reproduced when the same operations are performed.

## 📂 Project Files
- `random_numbers.py` — Demonstrates NumPy random-number functions.
- `exercises.py` — Contains practice exercises.
- `README.md` — Project documentation.

## ▶️ How to Run

Make sure Python and NumPy are installed.

Run the main examples:
```bash
python random_numbers.py
```

Run the exercises:
```bash
python exercises.py
```

## 🤖 Machine Learning Applications
Random-number generation is useful for:
- Sampling datasets
- Running simulations
- Testing algorithms
- Creating experimental data
- Supporting machine-learning experiments

## ✅ Day 6 Status
Completed the basics of NumPy random-number generation and practiced creating arrays and selecting random elements.

## 🚀 Next Step
**Day 7 — NumPy Indexing and Slicing**