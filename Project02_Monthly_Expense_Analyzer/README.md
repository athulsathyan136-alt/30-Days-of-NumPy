
# Monthly Expense Analyzer

## Project Overview
A personal expense analysis project built with Python and NumPy.

It analyzes 30 transactions across three months to understand spending patterns, category-wise expenses, payment methods, and budget performance.

## Dataset
- 30 transactions
- 6 expense categories
- 3 months of expense records
- 3 payment methods
- Currency: Indian Rupees (INR)

## Features
1. Load expense data from CSV.
2. Calculate total, average, median, highest and lowest expenses.
3. Analyze spending by category.
4. Identify the highest individual transaction.
5. Compare monthly expenses.
6. Analyze payment methods.
7. Check spending against a budget.
8. Identify transactions above ₹2,000.

## Technologies
- Python
- NumPy
- CSV

## NumPy Concepts Practised
- NumPy arrays
- np.array()
- np.sum()
- np.mean()
- np.median()
- np.max()
- np.min()
- np.argmax()
- np.unique()
- Boolean indexing
- np.where()

## Project Structure

```text
Project02_Monthly_Expense_Analyzer/
├── expenses.csv
├── expense_analyzer.py
├── README.md
└── requirements.txt
```

## How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the project:

```bash
python expense_analyzer.py
```

## Sample Results

| Metric | Result |
|---|---:|
| Total Expenses | ₹43,450 |
| Average Expense | ₹1,448.33 |
| Highest Expense | ₹3,000 |
| Lowest Expense | ₹400 |
| Highest Spending Category | Food |
| Highest Spending Month | February |
| Budget Exceeded | ₹18,450 |

## Author
Athul Sathyan

GitHub: https://github.com/athulsathyan136-alt
