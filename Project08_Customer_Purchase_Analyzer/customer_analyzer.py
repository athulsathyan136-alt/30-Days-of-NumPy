
import numpy as np
from pathlib import Path

# ---------------------------------------
# 1. PATHS
# ---------------------------------------

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data" / "purchases.csv"
OUTPUT_DIR = BASE_DIR / "outputs"

OUTPUT_DIR.mkdir(exist_ok=True)


# ---------------------------------------
# 2. LOAD DATA
# ---------------------------------------

data = np.genfromtxt(
    DATA_FILE,
    delimiter=",",
    skip_header=1,
    dtype=str
)

customer_id = data[:, 0].astype(int)
category = data[:, 1]
quantity = data[:, 2].astype(int)
unit_price = data[:, 3].astype(float)
month = data[:, 4].astype(int)


# ---------------------------------------
# 3. CALCULATE REVENUE
# ---------------------------------------

revenue = quantity * unit_price

total_revenue = np.sum(revenue)
average_purchase = np.mean(revenue)

highest_purchase = np.max(revenue)
lowest_purchase = np.min(revenue)


# ---------------------------------------
# 4. CUSTOMER ANALYSIS
# ---------------------------------------

unique_customers = np.unique(customer_id)

customer_spending = np.array([
    np.sum(revenue[customer_id == customer])
    for customer in unique_customers
])

top_customer_index = np.argmax(customer_spending)

top_customer = unique_customers[top_customer_index]
top_spending = customer_spending[top_customer_index]

customer_ranking = np.argsort(customer_spending)[::-1]

ranked_customers = unique_customers[customer_ranking]
ranked_spending = customer_spending[customer_ranking]


# ---------------------------------------
# 5. CATEGORY ANALYSIS
# ---------------------------------------

categories = np.unique(category)

category_revenue = np.array([
    np.sum(revenue[category == item])
    for item in categories
])

category_ranking = np.argsort(category_revenue)[::-1]

best_category = categories[category_ranking[0]]
best_category_revenue = category_revenue[category_ranking[0]]


# ---------------------------------------
# 6. HIGH VALUE PURCHASES
# ---------------------------------------

purchase_threshold = np.percentile(revenue, 90)

high_value_purchases = data[
    revenue >= purchase_threshold
]


# ---------------------------------------
# 7. PURCHASE FREQUENCY
# ---------------------------------------

purchase_frequency = np.array([
    np.sum(customer_id == customer)
    for customer in unique_customers
])

frequent_customers = unique_customers[
    purchase_frequency >= 2
]


# ---------------------------------------
# 8. MONTHLY REVENUE
# ---------------------------------------

monthly_revenue = np.array([
    np.sum(revenue[month == m])
    for m in range(1, 13)
])


# ---------------------------------------
# 9. CATEGORY REPORT
# ---------------------------------------

category_report = np.column_stack((
    categories,
    category_revenue.astype(str)
))

np.savetxt(
    OUTPUT_DIR / "category_report.csv",
    category_report,
    delimiter=",",
    header="category,revenue",
    comments="",
    fmt="%s"
)


# ---------------------------------------
# 10. CUSTOMER REPORT
# ---------------------------------------

customer_report = np.column_stack((
    ranked_customers,
    ranked_spending
))

np.savetxt(
    OUTPUT_DIR / "customer_ranking.csv",
    customer_report,
    delimiter=",",
    header="customer_id,total_spending",
    comments="",
    fmt="%s"
)


# ---------------------------------------
# 11. MONTHLY REPORT
# ---------------------------------------

monthly_report = np.column_stack((
    np.arange(1, 13),
    monthly_revenue
))

np.savetxt(
    OUTPUT_DIR / "monthly_revenue.csv",
    monthly_report,
    delimiter=",",
    header="month,revenue",
    comments="",
    fmt="%s"
)


# ---------------------------------------
# 12. TEXT REPORT
# ---------------------------------------

report = f"""
CUSTOMER PURCHASE BEHAVIOR ANALYZER
====================================

TOTAL REVENUE: {total_revenue:.2f}

AVERAGE PURCHASE: {average_purchase:.2f}

HIGHEST PURCHASE: {highest_purchase:.2f}

LOWEST PURCHASE: {lowest_purchase:.2f}

TOP CUSTOMER: {top_customer}

TOP CUSTOMER SPENDING: {top_spending:.2f}

BEST PRODUCT CATEGORY: {best_category}

CATEGORY REVENUE: {best_category_revenue:.2f}

HIGH VALUE PURCHASES: {len(high_value_purchases)}

FREQUENT CUSTOMERS: {frequent_customers}

====================================
END OF REPORT
"""

(OUTPUT_DIR / "customer_summary.txt").write_text(
    report,
    encoding="utf-8"
)


# ---------------------------------------
# 13. DISPLAY RESULTS
# ---------------------------------------

print("\nCUSTOMER PURCHASE ANALYZER")
print("=" * 40)

print("Total Revenue:", total_revenue)
print("Average Purchase:", average_purchase)

print("\nTOP CUSTOMER")
print("Customer ID:", top_customer)
print("Spending:", top_spending)

print("\nCATEGORY REVENUE")

for name, amount in zip(categories, category_revenue):
    print(name, amount)

print("\nCUSTOMER RANKING")

for customer, amount in zip(ranked_customers, ranked_spending):
    print(customer, amount)

print("\nMONTHLY REVENUE")

for m, amount in enumerate(monthly_revenue, start=1):
    print(m, amount)

print("\nFrequent Customers:", frequent_customers)
print("High Value Purchases:", len(high_value_purchases))

print("\nReports saved successfully!")
print("Output folder:", OUTPUT_DIR)
