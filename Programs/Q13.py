"""
Q13. Write a program to perform tuple operations and demonstrate
immutability.
"""

# Creating a tuple
t = (10, 20, 30, 40, 50)

print("Original Tuple:", t)

# Tuple operations
print("\nTuple Operations:")

# Accessing elements
print("First element:", t[0])
print("Last element:", t[-1])

# Slicing
print("Sliced tuple (1 to 3):", t[1:4])

# Length
print("Length of tuple:", len(t))

# Concatenation
t2 = (60, 70)
new_tuple = t + t2
print("After concatenation:", new_tuple)

# Repetition
print("Tuple repeated twice:", t * 2)

# Demonstrating immutability
print("\nTrying to modify tuple...")
try:
    t[0] = 100   # This will cause error
except TypeError as e:
    print("Error:", e)