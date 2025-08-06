import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt

# Load the cleaned dataset
df = pd.read_csv('data/cleaned_ecommerce_data.csv', parse_dates=['InvoiceDate'])

# --- RFM Analysis ---

# --- 1. Calculate R, F, M values ---

# Set a reference date (the day after the last transaction)
snapshot_date = df['InvoiceDate'].max() + dt.timedelta(days=1)

# Calculate R, F, M
rfm = df.groupby('CustomerID').agg({
    'InvoiceDate': lambda date: (snapshot_date - date.max()).days,
    'InvoiceNo': 'nunique',
    'TotalPrice': 'sum'
})

# Rename the columns
rfm.rename(columns={'InvoiceDate': 'Recency',
                    'InvoiceNo': 'Frequency',
                    'TotalPrice': 'MonetaryValue'}, inplace=True)


# --- 2. Calculate RFM scores ---

# Create labels and assign scores from 1 to 4
r_labels = range(4, 0, -1)
f_labels = range(1, 5)
m_labels = range(1, 5)

# Create R, F, M quartiles
r_quartiles = pd.qcut(rfm['Recency'], q=4, labels=r_labels)
f_quartiles = pd.qcut(rfm['Frequency'].rank(method='first'), q=4, labels=f_labels) # Use rank to handle non-unique bin edges
m_quartiles = pd.qcut(rfm['MonetaryValue'], q=4, labels=m_labels)


# Assign the quartiles to the RFM dataframe
rfm = rfm.assign(R=r_quartiles, F=f_quartiles, M=m_quartiles)

# --- 3. Create RFM segment and RFM score ---

# Concatenate RFM quartile scores to create RFM score
def join_rfm(x):
    return str(x['R']) + str(x['F']) + str(x['M'])

rfm['RFM_Segment'] = rfm.apply(join_rfm, axis=1)
rfm['RFM_Score'] = rfm[['R','F','M']].sum(axis=1)


# --- 4. Create customer segments based on RFM score ---

# Define segment mapping
def segment_customer(df):
    if df['RFM_Score'] >= 11:
        return 'Best Customers'
    elif df['RFM_Score'] >= 9:
        return 'Loyal Customers'
    elif df['RFM_Score'] >= 6:
        return 'Potential Loyalists'
    elif df['RFM_Score'] >= 5:
        return 'At-Risk Customers'
    else:
        return 'Lost Customers'

# Create a new column "Segment"
rfm['Segment'] = rfm.apply(segment_customer, axis=1)

# --- 5. Visualize the segments ---
segment_counts = rfm['Segment'].value_counts().sort_values(ascending=False)

plt.figure(figsize=(10, 6))
segment_counts.plot(kind='bar', color='skyblue')
plt.title('Customer Segmentation based on RFM Analysis')
plt.xlabel('Segment')
plt.ylabel('Number of Customers')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('picture/rfm_customer_segmentation.png')
plt.close()

# Save the RFM analysis results to a CSV file
rfm.to_csv('data/rfm_analysis.csv')

print("RFM analysis is complete.")
print("A plot of customer segmentation has been generated and saved to the 'picture' directory.")
print("The RFM analysis data has been saved to 'rfm_analysis.csv'.")

# Display the head of the RFM dataframe and the segment counts
print("\nFirst 5 rows of the RFM Analysis:")
print(rfm.head())

print("\nCustomer Segment Counts:")
print(segment_counts)