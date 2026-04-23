"""
Q3. Write a program to demonstrate variable assignment and swapping values
"""

# Variable assignment
a = 10
b = 20

print("Before swapping:")
print("a =", a)
print("b =", b)

# Method 1: Swapping using a temporary variable
temp = a
a = b
b = temp

print("\nAfter swapping using temporary variable:")
print("a =", a)
print("b =", b)

# Reassign values again
a = 10
b = 20

# Method 2: Swapping without using a third variable (Python way)
a, b = b, a

print("\nAfter swapping without temporary variable:")
print("a =", a)
print("b =", b)