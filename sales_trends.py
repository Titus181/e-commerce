import pandas as pd
import matplotlib.pyplot as plt

# Load the cleaned dataset
df = pd.read_csv('data/cleaned_ecommerce_data.csv', parse_dates=['InvoiceDate'])

# --- Analyze Sales Trends ---

# Set InvoiceDate as the index
df.set_index('InvoiceDate', inplace=True)

# Resample by month and sum the TotalPrice to get monthly sales
monthly_sales = df['TotalPrice'].resample('M').sum()

# Plot the monthly sales trend
plt.figure(figsize=(12, 6))
monthly_sales.plot(kind='line')
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.grid(True)
plt.tight_layout()
plt.savefig('picture/monthly_sales_trend.png')

print("Analysis of sales trends is complete.")
print("A plot of the monthly sales trend has been generated.")

# Display the monthly sales data
print("\nMonthly Sales Data:")
print(monthly_sales)