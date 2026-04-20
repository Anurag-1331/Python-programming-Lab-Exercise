"""
Q18. Write a program to write and append data to a file
"""

# Writing to a file (overwrites if file exists)
with open("sampleQ18.txt", "w") as file:
    file.write("Hello World\n")
    file.write("This is file writing example\n")

print("Data written to file successfully.")

# Appending to the same file
with open("sample.txt", "a") as file:
    file.write("This line is appended\n")

print("Data appended to file successfully.")