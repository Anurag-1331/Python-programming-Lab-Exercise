"""
Q29. Write a program using pandas to filter and group data.
"""

import pandas as pd

# Read CSV file
df = pd.read_csv("D:\Coding\python projects\Python Programming Lab Exercise\Programs\data.csv")

# Filter: students with Marks > 85
filtered_data = df[df["Marks"] > 85]
print("Filtered Data (Marks > 85):")
print(filtered_data)

# Group by Age and calculate average Marks
grouped_data = df.groupby("Age")["Marks"].mean()
print("\nGrouped Data (Average Marks by Age):")
print(grouped_data)