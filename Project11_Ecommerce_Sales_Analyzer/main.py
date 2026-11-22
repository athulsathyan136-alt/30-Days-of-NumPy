
import numpy as np

# Load dataset
data = np.genfromtxt(
    "data/sales.csv",
    delimiter=",",
    skip_header=1,
    dtype=None,
    encoding="utf-8"
)

order_ids = data["f0"]
products = data["f1"]
categories = data["f2"]
quantities = data["f3"]
unit_prices = data["f4"]

# Calculate revenue
revenue = quantities * unit_prices

# Overall analysis
total_revenue = np.sum(revenue)
average_order_value = np.mean(revenue)
median_order_value = np.median(revenue)

print("\n===== SALES OVERVIEW =====")
print("Total revenue: ₹", total_revenue)
print("Average order value: ₹", average_order_value)
print("Median order value: ₹", median_order_value)

# Highest and lowest orders
highest_order = np.argmax(revenue)
lowest_order = np.argmin(revenue)

print("\n===== ORDER ANALYSIS =====")
print("Highest revenue order:", order_ids[highest_order])
print("Highest order revenue: ₹", revenue[highest_order])

print("Lowest revenue order:", order_ids[lowest_order])
print("Lowest order revenue: ₹", revenue[lowest_order])

# Category analysis
unique_categories = np.unique(categories)

print("\n===== CATEGORY ANALYSIS =====")

category_revenues = []

for category in unique_categories:
    selected = np.isin(categories, category)
    category_total = np.sum(revenue[selected])

    category_revenues.append(category_total)

    print(category, ": ₹", category_total)

category_revenues = np.array(category_revenues)

best_category = np.argmax(category_revenues)

print(
    "\nBest category:",
    unique_categories[best_category]
)

# Product quantity analysis
unique_products = np.unique(products)
product_quantities = []

print("\n===== PRODUCT ANALYSIS =====")

for product in unique_products:
    selected = products == product
    quantity_sold = np.sum(quantities[selected])

    product_quantities.append(quantity_sold)

product_quantities = np.array(product_quantities)

top_product_position = np.argmax(product_quantities)

print("Top-selling product:", unique_products[top_product_position])
print("Units sold:", product_quantities[top_product_position])

# High-value orders
high_value_orders = np.where(revenue > 10000)[0]

print("\nOrders above ₹10,000:", len(high_value_orders))

# Low-revenue products
low_revenue = np.where(revenue < 5000)[0]

print("Orders below ₹5,000:")

for index in low_revenue:
    print(products[index], "₹", revenue[index])

# Revenue ranking
ranking = np.argsort(revenue)[::-1]

print("\n===== TOP FIVE ORDERS =====")

for index in ranking[:5]:
    print(order_ids[index], products[index], "₹", revenue[index])

# Revenue standard deviation
print("\nRevenue standard deviation:", np.std(revenue))

# Save report
report = np.column_stack((
    order_ids,
    products,
    categories,
    quantities,
    unit_prices,
    revenue
))

np.savetxt(
    "outputs/sales_report.csv",
    report,
    delimiter=",",
    fmt="%s",
    header="Order_ID,Product,Category,Quantity,Unit_Price,Revenue",
    comments=""
)

print("\nSales report saved successfully!")
