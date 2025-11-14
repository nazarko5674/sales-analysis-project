import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Generate synthetic data
np.random.seed(42)

days = pd.date_range(start="2025-01-01", periods=30, freq="D")

sales = np.random.randint(200, 1000, size=30)
expenses = np.random.randint(100, 600, size=30)
profit = sales - expenses

df = pd.DataFrame({
    "Date": days,
    "Sales": sales,
    "Expenses": expenses,
    "Profit": profit
})

print("\nSales Data:")
print(df.head())

# Plot 1: Sales & Expenses
plt.figure(figsize=(12, 6))
plt.plot(df["Date"], df["Sales"], label="Sales")
plt.plot(df["Date"], df["Expenses"], label="Expenses")
plt.title("Sales vs Expenses")
plt.xlabel("Date")
plt.ylabel("Amount")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("sales_vs_expenses.png")
plt.close()

# Plot 2: Profit Chart
plt.figure(figsize=(12, 6))
plt.bar(df["Date"], df["Profit"])
plt.title("Daily Profit")
plt.xlabel("Date")
plt.ylabel("Profit")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("profit_chart.png")
plt.close()

print("\nCharts generated:")
print(" - sales_vs_expenses.png")
print(" - profit_chart.png")

# Save data
df.to_csv("sales_data.csv", index=False)
print("\nData saved to sales_data.csv")

