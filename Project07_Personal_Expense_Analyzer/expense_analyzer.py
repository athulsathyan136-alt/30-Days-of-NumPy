
import csv
import numpy as np
from pathlib import Path

# Project directories
BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data" / "expenses.csv"
OUTPUT_DIR = BASE_DIR / "outputs"

OUTPUT_DIR.mkdir(exist_ok=True)


def load_expenses():
    dates = []
    categories = []
    amounts = []

    with open(DATA_FILE, "r", newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)

        for row in reader:
            dates.append(row["Date"])
            categories.append(row["Category"])
            amounts.append(float(row["Amount"]))

    return dates, np.array(categories), np.array(amounts)


def analyze_expenses(dates, categories, amounts):
    total = np.sum(amounts)
    average = np.mean(amounts)
    highest = np.max(amounts)
    lowest = np.min(amounts)
    median = np.median(amounts)
    standard_deviation = np.std(amounts)

    highest_index = np.argmax(amounts)
    lowest_index = np.argmin(amounts)

    # Filter expenses above ₹500
    expensive_transactions = amounts[amounts > 500]

    # Sort expenses from highest to lowest
    sorted_expenses = np.sort(amounts)[::-1]

    # Category-wise calculations
    unique_categories, counts = np.unique(
        categories, return_counts=True
    )

    category_totals = {}

    for category in unique_categories:
        category_mask = categories == category
        category_totals[category] = np.sum(amounts[category_mask])

    # Save category summary
    category_file = OUTPUT_DIR / "category_summary.csv"

    with open(category_file, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Category", "Total_Expense"])

        for category, amount in category_totals.items():
            writer.writerow([category, amount])

    # Generate text report
    report_file = OUTPUT_DIR / "expense_summary.txt"

    with open(report_file, "w", encoding="utf-8") as file:
        file.write("PERSONAL EXPENSE ANALYZER\n")
        file.write("=" * 35 + "\n\n")

        file.write(f"Total transactions: {len(amounts)}\n")
        file.write(f"Total expenses: Rs. {total:.2f}\n")
        file.write(f"Average expense: Rs. {average:.2f}\n")
        file.write(f"Median expense: Rs. {median:.2f}\n")
        file.write(f"Highest expense: Rs. {highest:.2f}\n")
        file.write(f"Lowest expense: Rs. {lowest:.2f}\n")
        file.write(f"Standard deviation: Rs. {standard_deviation:.2f}\n\n")

        file.write("HIGHEST TRANSACTION\n")
        file.write(f"Date: {dates[highest_index]}\n")
        file.write(f"Category: {categories[highest_index]}\n")
        file.write(f"Amount: Rs. {highest:.2f}\n\n")

        file.write("LOWEST TRANSACTION\n")
        file.write(f"Date: {dates[lowest_index]}\n")
        file.write(f"Category: {categories[lowest_index]}\n")
        file.write(f"Amount: Rs. {lowest:.2f}\n\n")

        file.write("CATEGORY-WISE EXPENSES\n")

        for category, amount in category_totals.items():
            file.write(f"{category}: Rs. {amount:.2f}\n")

        file.write("\nEXPENSES ABOVE RS. 500\n")
        for amount in expensive_transactions:
            file.write(f"Rs. {amount:.2f}\n")

        file.write("\nTOP 5 EXPENSES\n")
        for amount in sorted_expenses[:5]:
            file.write(f"Rs. {amount:.2f}\n")

    # Display results
    print("\nPERSONAL EXPENSE ANALYZER")
    print("=" * 35)
    print(f"Transactions: {len(amounts)}")
    print(f"Total expenses: Rs. {total:.2f}")
    print(f"Average expense: Rs. {average:.2f}")
    print(f"Median expense: Rs. {median:.2f}")
    print(f"Highest expense: Rs. {highest:.2f}")
    print(f"Lowest expense: Rs. {lowest:.2f}")
    print(f"Standard deviation: Rs. {standard_deviation:.2f}")

    print("\nCATEGORY-WISE EXPENSES")

    for category, amount in category_totals.items():
        print(f"{category}: Rs. {amount:.2f}")

    print("\nExpenses above Rs. 500:")
    print(expensive_transactions)

    print("\nTop 5 expenses:")
    print(sorted_expenses[:5])

    print("\nReports saved successfully!")


def main():
    dates, categories, amounts = load_expenses()

    if len(amounts) == 0:
        print("No expense records found.")
        return

    analyze_expenses(dates, categories, amounts)


if __name__ == "__main__":
    main()
