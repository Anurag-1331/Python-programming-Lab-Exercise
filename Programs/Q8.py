"""
Q8. Write a program using while loop to compute sum of first N
natural numbers.
"""

# Taking input from user
n = int(input("Enter a number: "))

# Initialize variables
i = 1
sum = 0

# While loop to calculate sum
while i <= n:
    sum += i
    i += 1

# Display result
print("Sum of first", n, "natural numbers is:", sum)