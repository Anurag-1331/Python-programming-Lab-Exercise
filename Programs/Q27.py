"""
Q27. Write a program using numpy to perform array operations
(creation, indexing, arithmetic).
"""

import numpy as np

# Array creation
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([10, 20, 30, 40, 50])

print("Array 1:", arr1)
print("Array 2:", arr2)

# Indexing
print("First element of arr1:", arr1[0])
print("Last element of arr1:", arr1[-1])

# Arithmetic operations
print("Addition:", arr1 + arr2)
print("Subtraction:", arr2 - arr1)
print("Multiplication:", arr1 * arr2)
print("Division:", arr2 / arr1)