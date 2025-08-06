# E-commerce Sales Data Analysis

## Project Overview

This project aims to analyze an e-commerce transaction dataset. Through data cleaning, Exploratory Data Analysis (EDA), and customer segmentation (RFM), we aim to uncover valuable business insights.

## Data Source

The dataset used in this project contains real online retail transactions from December 1st, 2010, to December 9th, 2011.

* **Original Data**: `data.csv`

## Analysis Workflow

### 1. Data Cleaning

* Removed records with missing `CustomerID`.
* Removed returned orders (`Quantity` < 0) and free items (`UnitPrice` = 0).
* Converted `InvoiceDate` to a datetime format.
* Added a `TotalPrice` column (`Quantity` * `UnitPrice`).
* The cleaned data is saved as `cleaned_ecommerce_data.csv`.

### 2. Exploratory Data Analysis (EDA)

#### a. Order Analysis by Country

Analyzed the distribution of orders across different countries to identify key markets.

![Top 10 Countries by Number of Orders](picture/country_distribution.png)

#### b. Top Selling Products Analysis

Identified the top ten best-selling products by quantity.

![Top 10 Selling Products](picture/top_10_products.png)

#### c. Sales Trend Analysis

Analyzed the total sales for each month to observe seasonal trends.

![Monthly Sales Trend](picture/monthly_sales_trend.png)

### 3. Customer Segmentation (RFM Analysis)

Segmented customers based on Recency, Frequency, and Monetary value to understand customer value and behavior.

* **RFM Analysis Results**: `rfm_analysis.csv`

![Customer Segmentation based on RFM Analysis](picture/rfm_customer_segmentation.png)

## File Structure

```
.
├── data.csv                     # Original dataset
├── cleaned_ecommerce_data.csv   # Cleaned data
├── rfm_analysis.csv             # RFM analysis results
├── picture/                     # Directory for all analysis plots
│   ├── country_distribution.png
│   ├── top_10_products.png
│   ├── monthly_sales_trend.png
│   └── rfm_customer_segmentation.png
└── README.md                    # Project documentation

```