"""
Q31. Write a program combining numpy, pandas, and matplotlib
for simple data analysis
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Create data using NumPy
data = np.array([50, 60, 70, 80, 90])

# Step 2: Convert to Pandas DataFrame
df = pd.DataFrame(data, columns=["Marks"])

# Step 3: Basic analysis
print("Data:")
print(df)

print("\nMean:", np.mean(data))
print("Max:", np.max(data))
print("Min:", np.min(data))

# Step 4: Plot using Matplotlib
plt.plot(df["Marks"])
plt.title("Marks Analysis")
plt.xlabel("Index")
plt.ylabel("Marks")
plt.show()