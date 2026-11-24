
import numpy as np

# ======================================
# 1. LOAD STOCK PRICE DATA
# ======================================

data = np.genfromtxt(
    "data/stock_prices.csv",
    delimiter=",",
    skip_header=1
)

days = data[:, 0].astype(int)
prices = data[:, 1:]

stock_names = np.array([
    "TechNova",
    "GreenEnergy",
    "AutoDrive",
    "HealthPlus",
    "CloudWorks"
])

print("\n===== STOCK MARKET ANALYZER =====")

# ======================================
# 2. PRICE ANALYSIS
# ======================================

average_prices = np.mean(prices, axis=0)
highest_prices = np.max(prices, axis=0)
lowest_prices = np.min(prices, axis=0)

print("\n===== PRICE SUMMARY =====")

for i in range(len(stock_names)):
    print("\nStock:", stock_names[i])
    print("Average:", average_prices[i])
    print("Highest:", highest_prices[i])
    print("Lowest:", lowest_prices[i])

# ======================================
# 3. DAILY PRICE CHANGES
# ======================================

price_changes = np.diff(prices, axis=0)

print("\n===== DAILY PRICE CHANGES =====")
print(price_changes)

# ======================================
# 4. DAILY PERCENTAGE RETURNS
# ======================================

returns = (
    np.diff(prices, axis=0)
    / prices[:-1]
) * 100

print("\n===== DAILY RETURNS =====")
print(returns)

# ======================================
# 5. AVERAGE RETURNS
# ======================================

average_returns = np.mean(returns, axis=0)

print("\n===== AVERAGE RETURNS =====")

for i in range(len(stock_names)):
    print(stock_names[i], ":", average_returns[i], "%")

# ======================================
# 6. VOLATILITY ANALYSIS
# ======================================

volatility = np.std(returns, axis=0)

print("\n===== STOCK VOLATILITY =====")

for i in range(len(stock_names)):
    print(stock_names[i], ":", volatility[i])

# ======================================
# 7. BEST AND WORST STOCK
# ======================================

best_position = np.argmax(average_returns)
worst_position = np.argmin(average_returns)

print("\n===== PERFORMANCE RANKING =====")

print("Best stock:", stock_names[best_position])
print("Worst stock:", stock_names[worst_position])

# ======================================
# 8. CORRELATION ANALYSIS
# ======================================

correlation = np.corrcoef(
    returns,
    rowvar=False
)

print("\n===== STOCK CORRELATION =====")
print(correlation)

# ======================================
# 9. PORTFOLIO ANALYSIS
# ======================================

weights = np.array([
    0.30,
    0.20,
    0.20,
    0.15,
    0.15
])

portfolio_returns = np.dot(
    returns,
    weights
)

average_portfolio_return = np.mean(
    portfolio_returns
)

portfolio_volatility = np.std(
    portfolio_returns
)

print("\n===== PORTFOLIO ANALYSIS =====")

print("Portfolio weights:", weights)
print("Average portfolio return:",
      average_portfolio_return, "%")

print("Portfolio volatility:",
      portfolio_volatility)

# ======================================
# 10. RETURN DISTRIBUTION
# ======================================

print("\n===== RETURN PERCENTILES =====")

print("25th percentile:",
      np.percentile(returns, 25, axis=0))

print("50th percentile:",
      np.percentile(returns, 50, axis=0))

print("90th percentile:",
      np.percentile(returns, 90, axis=0))

# ======================================
# 11. SAVE STOCK ANALYSIS
# ======================================

stock_report = np.column_stack((
    stock_names,
    average_prices.astype(str),
    highest_prices.astype(str),
    lowest_prices.astype(str),
    average_returns.astype(str),
    volatility.astype(str)
))

np.savetxt(
    "outputs/stock_analysis.csv",
    stock_report,
    delimiter=",",
    fmt="%s",
    header="Stock,Average_Price,Highest_Price,Lowest_Price,Average_Return,Volatility",
    comments=""
)

# ======================================
# 12. SAVE PORTFOLIO RETURNS
# ======================================

portfolio_report = np.column_stack((
    days[1:],
    portfolio_returns
))

np.savetxt(
    "outputs/portfolio_returns.csv",
    portfolio_report,
    delimiter=",",
    fmt="%.4f",
    header="Day,Portfolio_Return_Percent",
    comments=""
)

print("\nReports saved successfully!")
