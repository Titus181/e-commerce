import pandas as pd
import matplotlib.pyplot as plt

# Load the cleaned dataset
df = pd.read_csv('data/cleaned_ecommerce_data.csv')

# --- Analyze Top Selling Products ---

# Group by product and sum the quantities
top_products = df.groupby(['StockCode', 'Description'])['Quantity'].sum().sort_values(ascending=False)

# Get the top 10 products
top_10_products = top_products.head(10)

# Plot the top 10 products
plt.figure(figsize=(12, 6))
top_10_products.sort_values(ascending=True).plot(kind='barh')
plt.title('Top 10 Selling Products')
plt.xlabel('Total Quantity Sold')
plt.ylabel('Product')
plt.tight_layout()
plt.savefig('picture/top_10_products.png')

print("Analysis of top selling products is complete.")
print("A plot of the top 10 selling products has been generated.")

# Display the top 10 products as a table
print("\nTop 10 Selling Products:")
print(top_10_products)