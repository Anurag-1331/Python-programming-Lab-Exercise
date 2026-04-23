"""
Q28. Write a program using pandas to read a CSV file and perform
basic analysis
"""
import pandas as pd

# Read CSV file
df = pd.read_csv("D:\Coding\python projects\Python Programming Lab Exercise\Programs\data.csv")

# Display first 5 rows
print("First 5 rows:")
print(df.head())

# Basic information
print("\nData Info:")
df.info()

# Statistical summary
print("\nSummary Statistics:")
print(df.describe())

# Display column names
print("\nColumns:")
print(df.columns)

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())