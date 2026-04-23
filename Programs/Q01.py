"""
Q1. Write a program to demonstrate different numeric data types
(int, float) and type conversion.
"""

# int
a = 10

# float
b = 5.5

print(f"Integer value: {a}")
print(f"float value: {b}")

# Type Conversion -> two types of type conversion possible in Python

# 1. Implicit Conversion : Python automatically converts int → float when needed
result1 = a+b
print(f"result is {result1}") # result is 15.5
# here int -> float converted and added 

# 2. Explicit Conversion -> also known as Type Casting
# Python maually converts int and float using int() & float() function 

result2 = int(b)
print(f"After explicit conversion (float to int): {result2}")
# here float converted into integer

result3 = float(a)
print(f"After explicit conversion (int to float): {result3}")
# here int converted into float