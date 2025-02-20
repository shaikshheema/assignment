# -*- coding: utf-8 -*-
"""day8.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1hL62foGJ0g4PO969WcCMp29n3rBqPDwD
"""

'''Data Filtering
Extract all rows where sales are greater than 1000.
Find all sales records for a specific region (e.g., "East").'''

import pandas as pd

# Load the sales_data.csv file
df = pd.read_csv('Day_7_sales_data.csv')

# 1. Extract all rows where sales are greater than 1000
sales_greater_than_1000 = df[df['Sales'] > 1000]

# Display the filtered rows where sales are greater than 1000
print("Sales records where sales are greater than 1000:")
print(sales_greater_than_1000)

# 2. Find all sales records for a specific region (e.g., "East")
sales_east_region = df[df['Region'] == 'East']

# Display the sales records for the "East" region
print("\nSales records for the 'East' region:")
print(sales_east_region)

'''Data Processing
Add a new column, Profit_Per_Unit, calculated as Profit / Quantity.
Create another column, High_Sales, which labels rows as Yes if Sales > 1000,
'''

import pandas as pd

# Load the sales_data.csv file
df = pd.read_csv('Day_7_sales_data.csv')

# 1. Add a new column 'Profit_Per_Unit' calculated as Profit / Quantity
df['Profit_Per_Unit'] = df['Profit'] / df['Quantity']

# 2. Create a new column 'High_Sales' that labels rows as 'Yes' if Sales > 1000
df['High_Sales'] = df['Sales'].apply(lambda x: 'Yes' if x > 1000 else 'No')

# Display the updated DataFrame
print("Updated DataFrame with new columns:")
print(df)



