import numpy as np
import pandas as pd

# NumPy operations
print("NumPy Operations:")
# Create a NumPy array
arr = np.array([1, 2, 3, 4, 5])
print("Original array:", arr)

# Perform some calculations
print("Array mean:", np.mean(arr))
print("Array sum:", np.sum(arr))
print("Array squared:", np.square(arr))

# Create a 2D array
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\n2D array:")
print(matrix)

# Matrix operations
print("Matrix transpose:")
print(matrix.T)

# Pandas operations
print("\nPandas Operations:")
# Create a DataFrame
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 28],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']})
print("Original DataFrame:")
print(df)

# Basic DataFrame operations
print("\nDataFrame info:")
df.info()

print("\nDataFrame description:")
print(df.describe())

# Filtering data
print("\nPeople older than 30:")
print(df[df['Age'] > 30])

# Adding a new column
df['Country'] = 'USA'
print("\nDataFrame with new 'Country' column:")
print(df)

# Group by and aggregate
print("\nAverage age by city:")
print(df.groupby('City')['Age'].mean())
