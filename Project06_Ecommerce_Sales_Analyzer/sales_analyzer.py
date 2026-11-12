import csv 
from pathlib import Path
import numpy as np

# Project paths
BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data" / "sales.csv"
OUTPUT_DIR = BASE_DIR / "outputs"

OUTPUT_DIR.mkdir(exist_ok=True)

# Load dataset
dates = []
order_ids = []
products = []
categories = []
regions = []
quantities = []
unit_prices = []

with open(DATA_FILE, "r", encoding="utf-8-sig", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        dates.append(row["Date"])
        order_ids.append(row["Order_ID"])
        products.append(row["Product"])
        categories.append(row["Category"])
        regions.append(row["Region"])
        quantities.append(int(row["Quantity"]))
        unit_prices.append(float(row["Unit_Price"]))

# Convert data into NumPy arrays
dates = np.array(dates)
order_ids = np.array(order_ids)
products = np.array(products)
categories = np.array(categories)
regions = np.array(regions)

quantities = np.array(quantities)
unit_prices = np.array(unit_prices)

# Calculate revenue for every order
revenue = quantities * unit_prices

# Overall sales analysis
total_revenue = np.sum(revenue)
average_order_revenue = np.mean(revenue)
highest_order = np.max(revenue)
lowest_order = np.min(revenue)
median_revenue = np.median(revenue)
total_quantity = np.sum(quantities)

# Product analysis
unique_products = np.unique(products)
product_revenues = []

for product in unique_products:
    mask = products == product
    product_revenues.append(np.sum(revenue[mask]))

product_revenues = np.array(product_revenues)

best_product_index = np.argmax(product_revenues)
worst_product_index = np.argmin(product_revenues)

best_product = unique_products[best_product_index]
worst_product = unique_products[worst_product_index]

# Top five products by revenue
top_indices = np.argsort(product_revenues)[::-1][:5]

# Category analysis
unique_categories = np.unique(categories)
category_revenues = []

for category in unique_categories:
    mask = categories == category
    category_revenues.append(np.sum(revenue[mask]))

category_revenues = np.array(category_revenues)

best_category_index = np.argmax(category_revenues)

# Monthly analysis
months = np.array([date[:7] for date in dates])
unique_months = np.unique(months)

monthly_revenues = []

for month in unique_months:
    mask = months == month
    monthly_revenues.append(np.sum(revenue[mask]))

monthly_revenues = np.array(monthly_revenues)

best_month_index = np.argmax(monthly_revenues)

# Regional analysis
unique_regions = np.unique(regions)
region_revenues = []

for region in unique_regions:
    mask = regions == region
    region_revenues.append(np.sum(revenue[mask]))

region_revenues = np.array(region_revenues)

best_region_index = np.argmax(region_revenues)

# Additional statistics
revenue_std = np.std(revenue)
revenue_75_percentile = np.percentile(revenue, 75)

# Save category report
category_file = OUTPUT_DIR / "category_summary.csv"

with open(category_file, "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Category", "Total_Revenue"])

    for i, category in enumerate(unique_categories):
        writer.writerow([category, category_revenues[i]])

# Save monthly report
monthly_file = OUTPUT_DIR / "monthly_summary.csv"

with open(monthly_file, "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Month", "Total_Revenue"])

    for i, month in enumerate(unique_months):
        writer.writerow([month, monthly_revenues[i]])

# Save text report
report_file = OUTPUT_DIR / "sales_report.txt"

with open(report_file, "w", encoding="utf-8") as file:
    file.write("ECOMMERCE SALES PERFORMANCE REPORT\n")
    file.write("=" * 45 + "\n\n")

    file.write(f"Total Orders: {len(order_ids)}\n")
    file.write(f"Total Quantity Sold: {total_quantity}\n")
    file.write(f"Total Revenue: {total_revenue:.2f}\n")
    file.write(f"Average Order Revenue: {average_order_revenue:.2f}\n")
    file.write(f"Highest Order Revenue: {highest_order:.2f}\n")
    file.write(f"Lowest Order Revenue: {lowest_order:.2f}\n")
    file.write(f"Median Order Revenue: {median_revenue:.2f}\n")
    file.write(f"Revenue Standard Deviation: {revenue_std:.2f}\n")
    file.write(f"75th Percentile Revenue: {revenue_75_percentile:.2f}\n\n")

    file.write("PRODUCT PERFORMANCE\n")
    file.write("-" * 30 + "\n")
    file.write(f"Best Product: {best_product}\n")
    file.write(f"Lowest Revenue Product: {worst_product}\n\n")

    file.write("TOP FIVE PRODUCTS BY REVENUE\n")
    file.write("-" * 30 + "\n")

    for index in top_indices:
        file.write(
            f"{unique_products[index]}: "
            f"{product_revenues[index]:.2f}\n"
        )

    file.write("\nCATEGORY PERFORMANCE\n")
    file.write("-" * 30 + "\n")

    for i, category in enumerate(unique_categories):
        file.write(f"{category}: {category_revenues[i]:.2f}\n")

    file.write(
        f"\nBest Category: "
        f"{unique_categories[best_category_index]}\n"
    )

    file.write("\nMONTHLY PERFORMANCE\n")
    file.write("-" * 30 + "\n")

    for i, month in enumerate(unique_months):
        file.write(f"{month}: {monthly_revenues[i]:.2f}\n")

    file.write(f"Best Month: {unique_months[best_month_index]}\n")

    file.write("\nREGIONAL PERFORMANCE\n")
    file.write("-" * 30 + "\n")

    for i, region in enumerate(unique_regions):
        file.write(f"{region}: {region_revenues[i]:.2f}\n")

    file.write(f"Best Region: {unique_regions[best_region_index]}\n")

print("=" * 45)
print("ECOMMERCE SALES PERFORMANCE ANALYZER")
print("=" * 45)

print(f"Total Orders: {len(order_ids)}")
print(f"Total Quantity Sold: {total_quantity}")
print(f"Total Revenue: {total_revenue:.2f}")
print(f"Average Order Revenue: {average_order_revenue:.2f}")
print(f"Highest Order Revenue: {highest_order:.2f}")
print(f"Lowest Order Revenue: {lowest_order:.2f}")
print(f"Median Revenue: {median_revenue:.2f}")

print("\nBest Product:", best_product)
print("Best Category:", unique_categories[best_category_index])
print("Best Month:", unique_months[best_month_index])
print("Best Region:", unique_regions[best_region_index])

print("\nReports generated successfully!")
print("Output folder:", OUTPUT_DIR)
