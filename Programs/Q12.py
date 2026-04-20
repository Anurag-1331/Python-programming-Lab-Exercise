"""
Q12. Write a program to demonstrate list slicing and list manipulation.
"""

# Creating a list
numbers = [10, 20, 30, 40, 50, 60]

print("Original List:", numbers)

# List Slicing
print("\nList Slicing:")
print("First 3 elements:", numbers[:3])
print("Last 3 elements:", numbers[-3:])
print("Middle elements:", numbers[1:5])
print("Reversed list:", numbers[::-1])

# List Manipulation
print("\nList Manipulation:")

# Append
numbers.append(70)
print("After append (70):", numbers)

# Insert
numbers.insert(2, 25)
print("After insert (25 at index 2):", numbers)

# Remove
numbers.remove(40)
print("After removing 40:", numbers)

# Pop
numbers.pop()
print("After pop (last element removed):", numbers)

# Update element
numbers[0] = 5
print("After updating first element:", numbers)