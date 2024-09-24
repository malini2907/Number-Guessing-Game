import pandas as pd
import numpy as np

# Step 1: Load the dataset
file_path = input("Enter the path to the CSV file (e.g., C:\\Users\\admin\\Desktop\\Python\\VideoGamesSales.csv): ")
df = pd.read_csv(file_path)
print("Initial DataFrame:")
print(df.head())

# Step 2: Remove duplicate rows
input("Press Enter to remove duplicate rows...")
df = df.drop_duplicates()
print("\nAfter removing duplicates:")
print(df.head())

# Step 3: Fill missing values in 'Region' with a user-provided value
fill_value = input("Enter a value to fill missing 'Region' values (default is 'North'): ") or 'North'
df['Region'] = df['Region'].fillna(fill_value)
print("\nAfter filling missing values in 'Region':")
print(df.head())

# Step 4: Clean 'NA_Sales' column (remove '$' and convert to numbers)
input("Press Enter to clean 'NA_Sales' column...")
df['NA_Sales'] = df['NA_Sales'].replace('[$]', '', regex=True)
df['NA_Sales'] = pd.to_numeric(df['NA_Sales'], errors='coerce')
print("\nAfter cleaning 'NA_Sales' column:")
print(df.head())

# Step 5: Replace missing 'NA_Sales' values with the average sales
input("Press Enter to replace missing 'NA_Sales' values with the average sales...")
average_sales = df['NA_Sales'].mean()
df['NA_Sales'] = df['NA_Sales'].fillna(average_sales)
print("\nAfter replacing missing 'NA_Sales' values with the average sales:")
print(df.head())

# Step 6: Standardize 'Country' names
input("Press Enter to standardize 'Country' names...")
df['Country'] = df['Country'].replace({'USA': 'United States'})
df['Country'] = df['Country'].str.title()
print("\nAfter standardizing 'Country' names:")
print(df.head())

# Step 7: Rename columns to be more understandable
input("Press Enter to rename columns...")
df = df.rename(columns={
    'NA_Sales': 'National Sales',
    'Global_Sales': 'Global Sales',
    'NA_Profit': 'National Profit',
    'Global_Profit': 'Global Profit'
})
print("\nAfter renaming columns:")
print(df.head())

# Step 8: Cap 'National Sales' at the 95th percentile to limit outliers
input("Press Enter to cap 'National Sales' at the 95th percentile...")
sales_cap = df['National Sales'].quantile(0.95)
df['National Sales'] = df['National Sales'].clip(upper=sales_cap)
print("\nAfter capping 'National Sales' at the 95th percentile:")
print(df.head())

# Final output
input("Press Enter to display the final cleaned DataFrame...")
print("\nFinal cleaned DataFrame:")
print(df.head())

