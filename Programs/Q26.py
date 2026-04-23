"""
Q26. Write a program using finally and custom exceptions.
"""

class NegativeNumberError(Exception):
    pass

try:
    num = int(input("Enter a positive number: "))

    if num < 0:
        raise NegativeNumberError("Negative numbers are not allowed.")

    print("You entered:", num)

except NegativeNumberError as e:
    print("Custom Exception:", e)

except ValueError:
    print("Error: Please enter a valid integer.")

finally:
    print("Program execution completed.")