"""
Q17. Write a program to read contents of a file using read(),
 readline(), and readlines().
"""

# Opening file in read mode
# file = open("sample.txt", "r")
with open ("sampleQ17.txt", "r") as file: 
# Using read()
    print("Using read():")
    content = file.read()
    print(content)

# Move file pointer to beginning
    file.seek(0)

# Using readline()
    print("\nUsing readline():")
    line1 = file.readline()
    line2 = file.readline()
    print(line1, end="")
    print(line2, end="")

# Move file pointer again
    file.seek(0)

# Using readlines()
    print("\nUsing readlines():")
    lines = file.readlines()
    print(lines)

# Closing file
    file.close()