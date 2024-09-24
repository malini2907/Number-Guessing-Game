import pandas as pd
import numpy as np

# Step 1: Load the dataset
file_path = r'C:\\Users\\admin\\Desktop\\Python\\VideoGamesSales.csv'
df = pd.read_csv(file_path)
print("After loading the dataset:")
print(df.head())

# Step 2: Remove duplicate rows
df = df.drop_duplicates()
print("\nAfter removing duplicate rows:")
print(df.head())

# Step 3: Fill missing values in 'Region' with 'North'
df['Region'] = df['Region'].fillna('North')
print("\nAfter filling missing values in 'Region':")
print(df.head())

# Step 4: Clean 'NA_Sales' column (remove '$' and convert to numbers)
df['NA_Sales'] = df['NA_Sales'].replace('[$]', '', regex=True)
df['NA_Sales'] = pd.to_numeric(df['NA_Sales'], errors='coerce')
print("\nAfter cleaning 'NA_Sales' column:")
print(df.head())

# Step 5: Replace missing 'NA_Sales' values with the average sales
average_sales = df['NA_Sales'].mean()
df['NA_Sales'] = df['NA_Sales'].fillna(average_sales)
print("\nAfter replacing missing 'NA_Sales' values with the average sales:")
print(df.head())

# Step 6: Standardize 'Country' names (replace 'USA' with 'United States' and capitalize all country names)
df['Country'] = df['Country'].replace({'USA': 'United States'})
df['Country'] = df['Country'].str.title()
print("\nAfter standardizing 'Country' names:")
print(df.head())

# Step 7: Rename columns to be more understandable
df = df.rename(columns={
    'NA_Sales': 'National Sales',
    'Global_Sales': 'Global Sales',
    'NA_Profit': 'National Profit',
    'Global_Profit': 'Global Profit'
})
print("\nAfter renaming columns:")
print(df.head())

# Step 8: Cap 'National Sales' at the 95th percentile to limit outliers
sales_cap = df['National Sales'].quantile(0.95)
df['National Sales'] = np.where(df['National Sales'] > sales_cap, sales_cap, df['National Sales'])
print("\nAfter capping 'National Sales' at the 95th percentile:")
print(df.head())

# Final output
print("\nFinal cleaned DataFrame:")
print(df.head())

