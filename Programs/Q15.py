"""
Q15. Write a program using built-in functions on list, string, and
dictionary.
"""

# -------- LIST FUNCTIONS --------
numbers = [10, 20, 30, 40, 50]

print("List:", numbers)
print("Length:", len(numbers))
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Sum:", sum(numbers))

# -------- STRING FUNCTIONS --------
text = "Python Programming"

print("\nString:", text)
print("Length:", len(text))
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Count of 'o':", text.count('o'))
print("Replace 'Python' with 'Java':", text.replace("Python", "Java"))

# -------- DICTIONARY FUNCTIONS --------
student = {
    "name": "Rahul",
    "age": 20,
    "course": "BCA"
}

print("\nDictionary:", student)
print("Length:", len(student))
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

# Using get()
print("Get value of 'name':", student.get("name"))

# Clear dictionary
temp = student.copy()
temp.clear()
print("After clear():", temp)