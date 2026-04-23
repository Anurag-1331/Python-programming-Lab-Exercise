"""
Q30. Write a program using matplotlib to plot line and bar graphs.
"""

import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

# Line graph
#----------------------
plt.plot(x, y)
plt.title("Line Graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

# Bar graph
#-----------------------
plt.bar(x, y)
plt.title("Bar Graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()


# also some types of graph used in python :--
#************************************************

# Histogram
plt.bar(x, y)
plt.title("Histogram")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

# Pie Chart
plt.bar(x, y)
plt.title("Pie Chart")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

# Scatter Plot
plt.bar(x, y)
plt.title("Scatter Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()