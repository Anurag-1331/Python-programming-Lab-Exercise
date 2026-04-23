"""
Q25. Write a program demonstrating multiple exceptions handling.
"""

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except ValueError:
    print("Error: Invalid input. Please enter integers.")

except NameError:
    print("Error: Variable not defined.")

except Exception as e:
    print("Unknown error:", e)

finally:
    print("Program finished.")