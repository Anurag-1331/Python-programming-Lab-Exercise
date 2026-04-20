"""
Q6. Write a program using for loop to print multiplication table
of a number.
"""

# Taking input from user
num = int(input("Enter a number: "))

# Printing multiplication table using for loop
print(f"\nMultiplication Table of: {num}")

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")