
import numpy as np
import csv

# 1. LOAD EXPENSE DATA
dates = []
categories = []
descriptions = []
amounts = []
payment_methods = []

with open("expenses.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        dates.append(row["Date"])
        categories.append(row["Category"])
        descriptions.append(row["Description"])
        amounts.append(float(row["Amount"]))
        payment_methods.append(row["Payment_Method"])

# Convert amounts into a NumPy array
amounts = np.array(amounts)

print("\n========== MONTHLY EXPENSE ANALYZER ==========")
print("Total Transactions:", len(amounts))

# 2. BASIC EXPENSE SUMMARY
print("\n========== EXPENSE SUMMARY ==========")

total_expense = np.sum(amounts)
average_expense = np.mean(amounts)
highest_expense = np.max(amounts)
lowest_expense = np.min(amounts)
median_expense = np.median(amounts)

print(f"Total Expenses: ₹{total_expense:.2f}")
print(f"Average Expense: ₹{average_expense:.2f}")
print(f"Highest Expense: ₹{highest_expense:.2f}")
print(f"Lowest Expense: ₹{lowest_expense:.2f}")
print(f"Median Expense: ₹{median_expense:.2f}")

# 3. CATEGORY-WISE ANALYSIS
print("\n========== CATEGORY ANALYSIS ==========")

unique_categories = np.unique(categories)

for category in unique_categories:
    category_amounts = amounts[np.array(categories) == category]
    print(
        f"{category}: ₹{np.sum(category_amounts):.2f}"
        f" | Transactions: {len(category_amounts)}"
    )

# 4. FIND THE HIGHEST EXPENSE
highest_index = np.argmax(amounts)

print("\n========== HIGHEST TRANSACTION ==========")
print("Description:", descriptions[highest_index])
print("Category:", categories[highest_index])
print(f"Amount: ₹{amounts[highest_index]:.2f}")
print("Date:", dates[highest_index])

# 5. MONTHLY ANALYSIS
print("\n========== MONTHLY ANALYSIS ==========")

months = np.array([date[:7] for date in dates])
unique_months = np.unique(months)

for month in unique_months:
    monthly_amounts = amounts[months == month]
    print(f"{month}: ₹{np.sum(monthly_amounts):.2f}")

# 6. PAYMENT METHOD ANALYSIS
print("\n========== PAYMENT METHOD ANALYSIS ==========")

unique_methods = np.unique(payment_methods)

for method in unique_methods:
    method_amounts = amounts[np.array(payment_methods) == method]
    print(f"{method}: ₹{np.sum(method_amounts):.2f}")

# 7. EXPENSE LIMIT CHECK
budget = 25000

print("\n========== BUDGET ANALYSIS ==========")
print(f"Budget: ₹{budget:.2f}")
print(f"Total Spent: ₹{total_expense:.2f}")

if total_expense > budget:
    print(f"Budget Exceeded: ₹{total_expense - budget:.2f}")
else:
    print(f"Remaining Budget: ₹{budget - total_expense:.2f}")

# 8. EXPENSIVE TRANSACTIONS
print("\n========== EXPENSIVE TRANSACTIONS ==========")

expensive_expenses = amounts > 2000

print("Number of expenses above ₹2000:", np.sum(expensive_expenses))

for index in np.where(expensive_expenses)[0]:
    print(
        f"{dates[index]} | {descriptions[index]} "
        f"| ₹{amounts[index]:.2f}"
    )

print("\nAnalysis completed successfully!")
