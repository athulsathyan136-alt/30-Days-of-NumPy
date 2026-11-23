
import numpy as np

# =====================================
# 1. LOAD EXPENSE DATA
# =====================================

data = np.genfromtxt(
    "data/expenses.csv",
    delimiter=",",
    skip_header=1,
    dtype=str
)

dates = data[:, 0]
categories = data[:, 1]
descriptions = data[:, 2]
amounts = data[:, 3].astype(float)

# =====================================
# 2. FINANCIAL INFORMATION
# =====================================

monthly_income = 40000

print("\n===== PERSONAL FINANCE ANALYZER =====")

# =====================================
# 3. BASIC EXPENSE ANALYSIS
# =====================================

total_expenses = np.sum(amounts)
average_expense = np.mean(amounts)
median_expense = np.median(amounts)

print("\n===== EXPENSE SUMMARY =====")

print("Total expenses:", total_expenses)
print("Average expense:", average_expense)
print("Median expense:", median_expense)

# =====================================
# 4. HIGHEST AND LOWEST EXPENSE
# =====================================

highest_position = np.argmax(amounts)
lowest_position = np.argmin(amounts)

print("\n===== EXPENSE RECORDS =====")

print("Highest expense:", amounts[highest_position])
print("Description:", descriptions[highest_position])

print("Lowest expense:", amounts[lowest_position])
print("Description:", descriptions[lowest_position])

# =====================================
# 5. CATEGORY ANALYSIS
# =====================================

unique_categories = np.unique(categories)

print("\n===== CATEGORY ANALYSIS =====")

for category in unique_categories:

    category_expenses = amounts[categories == category]

    category_total = np.sum(category_expenses)

    print(category, ":", category_total)

# =====================================
# 6. SAVINGS ANALYSIS
# =====================================

savings = monthly_income - total_expenses

savings_percentage = (
    savings / monthly_income
) * 100

print("\n===== SAVINGS ANALYSIS =====")

print("Monthly income:", monthly_income)
print("Total expenses:", total_expenses)
print("Remaining savings:", savings)
print("Savings percentage:", savings_percentage)

# =====================================
# 7. BUDGET ANALYSIS
# =====================================

budget_categories = np.array([
    "Food",
    "Transport",
    "Shopping",
    "Utilities",
    "Entertainment"
])

budget_limits = np.array([
    10000,
    5000,
    6000,
    4000,
    3000
])

print("\n===== BUDGET ANALYSIS =====")

for i in range(len(budget_categories)):

    category = budget_categories[i]

    actual_expense = np.sum(
        amounts[categories == category]
    )

    budget = budget_limits[i]

    difference = budget - actual_expense

    print("\nCategory:", category)
    print("Budget:", budget)
    print("Actual:", actual_expense)
    print("Remaining:", difference)

    if actual_expense > budget:
        print("Status: OVER BUDGET")
    else:
        print("Status: WITHIN BUDGET")

# =====================================
# 8. EXPENSE RANKING
# =====================================

sorted_positions = np.argsort(amounts)[::-1]

print("\n===== TOP 5 EXPENSES =====")

for position in sorted_positions[:5]:

    print(
        descriptions[position],
        ":",
        amounts[position]
    )

# =====================================
# 9. EXPENSE PERCENTAGES
# =====================================

expense_percentages = (
    amounts / total_expenses
) * 100

print("\n===== EXPENSE CONTRIBUTION =====")

for i in range(len(amounts)):

    print(
        descriptions[i],
        ":",
        round(expense_percentages[i], 2),
        "%"
    )

# =====================================
# 10. SAVE FINANCIAL REPORT
# =====================================

report = np.column_stack((
    dates,
    categories,
    descriptions,
    amounts.astype(str),
    np.round(expense_percentages, 2).astype(str)
))

np.savetxt(
    "outputs/financial_report.csv",
    report,
    delimiter=",",
    fmt="%s",
    header="Date,Category,Description,Amount,Percentage",
    comments=""
)

print("\nFinancial report saved successfully!")
