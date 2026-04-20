"""
Q16. Write functions to organize a program that performs basic
operations on strings and lists.
"""

# -------- STRING FUNCTIONS --------
def string_operations(text):
    print("\nString Operations:")
    print("Original String:", text)
    print("Length:", len(text))
    print("Uppercase:", text.upper())
    print("Reversed:", text[::-1])


# -------- LIST FUNCTIONS --------
def list_operations(lst):
    print("\nList Operations:")
    print("Original List:", lst)
    print("Length:", len(lst))
    print("Maximum:", max(lst))
    print("Minimum:", min(lst))
    print("Sum:", sum(lst))


# -------- MAIN PROGRAM --------
# Taking input
text = input("Enter a string: ")

numbers = list(map(int, input("Enter list elements (space-separated): ").split()))

# Calling functions
string_operations(text)
list_operations(numbers)