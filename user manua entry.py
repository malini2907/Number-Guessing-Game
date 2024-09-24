import numpy as np
import pandas as pd

# NumPy operations
print("NumPy Operations:")

# Get user input for NumPy array
arr = np.array([int(x) for x in input("Enter numbers for the NumPy array (space-separated): ").split()])
print("Original array:", arr)

# Perform some calculations
print("Array mean:", np.mean(arr))
print("Array sum:", np.sum(arr))
print("Array squared:", np.square(arr))

# Create a 2D array (matrix)
rows = int(input("Enter number of rows for the matrix: "))
cols = int(input("Enter number of columns for the matrix: "))
matrix = np.array([input(f"Enter {cols} space-separated numbers for row {i+1}: ").split() for i in range(rows)], dtype=float)
print("\n2D array:")
print(matrix)

# Matrix operations
print("Matrix transpose:")
print(matrix.T)

# Pandas operations
print("\nPandas Operations:")

# Get user input for DataFrame
n = int(input("Enter number of people: "))
names = []
ages = []
cities = []

for i in range(n):
    names.append(input(f"Enter name for person {i+1}: "))
    ages.append(int(input(f"Enter age for person {i+1}: ")))
    cities.append(input(f"Enter city for person {i+1}: "))

# Create a DataFrame
df = pd.DataFrame({
    'Name': names,
    'Age': ages,
    'City': cities
})

print("Original DataFrame:")
print(df)

# Basic DataFrame operations
print("\nDataFrame info:")
df.info()
print("\nDataFrame description:")
print(df.describe())

# Filtering data
age_filter = int(input("Enter age to filter people older than: "))
print(f"\nPeople older than {age_filter}:")
print(df[df['Age'] > age_filter])

# Adding a new column
country = input("Enter country for all entries: ")
df['Country'] = country
print("\nDataFrame with new 'Country' column:")
print(df)

# Group by and aggregate
print("\nAverage age by city:")
print(df.groupby('City')['Age'].mean())
