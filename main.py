import pandas as pd
import matplotlib.pyplot as plt


# Load the dataset
df = pd.read_csv('data.csv', encoding='ISO-8859-1')

# Display basic information about the dataset
print("Dataframe Info:")
df.info()

# Display the first few rows of the dataset
print("\nFirst 5 rows of the dataframe:")
print(df.head())


# --- Data Cleaning ---

# Drop rows with missing CustomerID
df.dropna(axis=0, subset=['CustomerID'], inplace=True)

# Convert CustomerID to integer
df['CustomerID'] = df['CustomerID'].astype(int)

# Convert InvoiceDate to datetime
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# Remove returns (Quantity < 0)
df = df[df['Quantity'] > 0]

# Remove items with UnitPrice == 0
df = df[df['UnitPrice'] > 0]

# Create a 'TotalPrice' column
df['TotalPrice'] = df['Quantity'] * df['UnitPrice']


# --- EDA: Sales by Country ---

# Group by country and count the number of invoices
country_counts = df['Country'].value_counts().sort_values(ascending=False)

# Plot the top 10 countries
plt.figure(figsize=(12, 6))
country_counts.head(10).plot(kind='bar')
plt.title('Top 10 Countries by Number of Orders')
plt.xlabel('Country')
plt.ylabel('Number of Orders')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('country_distribution.png')

# Save the cleaned data to a new CSV file
df.to_csv('cleaned_ecommerce_data.csv', index=False)

print("Data cleaning and initial analysis are complete.")
print("A plot of the top 10 countries by number of orders has been generated.")
print("The cleaned data has been saved to 'cleaned_ecommerce_data.csv'.")
print("\nCleaned Dataframe Info:")
df.info()

print("\nTop 5 rows of the cleaned dataframe:")
print(df.head())