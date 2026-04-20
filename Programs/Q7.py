"""
Q7. Write a program to iterate through string, list, and dictionary
using loops.
"""

# String iteration
text = "Hello"

print("Iterating through string:")
for char in text:
    print(char)

# List iteration
numbers = [10, 20, 30, 40, 50]

print("\nIterating through list:")
for num in numbers:
    print(num)

# Dictionary iteration
student = {
    "name": "Rahul",
    "age": 20,
    "course": "BCA"
}

print("\nIterating through dictionary (keys):")
for key in student:
    print(key)

print("\nIterating through dictionary (values):")
for value in student.values():
    print(value)

print("\nIterating through dictionary (key-value pairs):")
for key, value in student.items():
    print(key, ":", value)