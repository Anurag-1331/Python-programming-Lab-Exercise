"""
Q9. Demonstrate use of break, continue, and pass in loops.
"""

# Demonstrating break
print("Using break:")
for i in range(1, 11):
    if i == 5:
        break # exit the loop when reach to the 5
    print(i) # print 1 2 3 4

# Demonstrating continue
print("\nUsing continue:")
for i in range(1, 11):
    if i == 5:
        continue # skip the number when reach to the 5
    print(i) # print 1 2 3 4 6 7  9 10

# Demonstrating pass
print("\nUsing pass:")
for i in range(1, 6):
    if i == 3:
        pass  # does nothing
    print(i) # print 1 2 3 4 5