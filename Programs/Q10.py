"""
Q10. Write a program to perform string operations (slicing, con
catenation, reversing).
"""
# Taking input from user
text = input("Enter a string: ")

# Slicing
print("\nSlicing:")
print("First 3 characters:", text[:3])
print("Last 3 characters:", text[-3:])
print("Middle part:", text[1:-1])

# Concatenation
text2 = input("\nEnter another string: ")
concat = text + " " + text2
print("\nConcatenation:", concat)

# Reversing string
reverse = text[::-1]
print("\nReversed string:", reverse)