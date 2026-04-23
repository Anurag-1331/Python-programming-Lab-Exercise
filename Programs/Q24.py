"""
Q24. Write a program to handle exceptions using try-except blocks.
"""
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b
    print("Result:", result)

except (ZeroDivisionError, ValueError) as e:
    print("Error occurred:", e)

finally:
    print("Execution completed.")