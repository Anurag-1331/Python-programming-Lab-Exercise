"""
Q14. Write a program to perform dictionary operations (add, update, delete).
"""

# Creating a dictionary
student = {
    "name": "Rahul",
    "age": 20,
    "course": "BCA"
}

print("Original Dictionary:", student)

# Adding a new key-value pair
student["marks"] = 85
print("\nAfter adding (marks):", student)

# Updating an existing value
student["age"] = 21
print("After updating (age):", student)

# Deleting an element using del
del student["course"]
print("After deleting (course):", student)

# Deleting using pop()
student.pop("marks")
print("After popping (marks):", student)