
# Project 06 – E-commerce Sales Performance Analyzer

## Overview

A Python and NumPy project that analyzes e-commerce sales data to discover revenue trends, product performance, category performance, monthly sales, and regional performance.

## Dataset

The project uses a synthetic dataset containing 30 orders across January, February, and March 2026.

Columns:
- Date
- Order_ID
- Product
- Category
- Region
- Quantity
- Unit_Price

## Features

- Total revenue calculation
- Average, maximum, minimum, and median order revenue
- Total quantity sold
- Product revenue comparison
- Top five products
- Category performance analysis
- Monthly sales analysis
- Regional revenue analysis
- Revenue standard deviation and percentile
- CSV and text report generation

## NumPy Concepts

- NumPy arrays
- Array multiplication
- np.sum()
- np.mean()
- np.max()
- np.min()
- np.median()
- np.std()
- np.percentile()
- np.unique()
- Boolean indexing
- np.argmax()
- np.argmin()
- np.argsort()

## Project Structure

```text
Project06_Ecommerce_Sales_Analyzer/
├── data/
│   └── sales.csv
├── outputs/
│   ├── category_summary.csv
│   ├── monthly_summary.csv
│   └── sales_report.txt
├── sales_analyzer.py
├── requirements.txt
└── README.md
```

## Installation

```bash
pip install -r requirements.txt
```

## Run

```bash
python sales_analyzer.py
```

## Outputs

The program generates:
- category_summary.csv
- monthly_summary.csv
- sales_report.txt

## Technologies

- Python
- NumPy
- CSV

## Author

Athul Sathyan
