"""
Q19. Write a program to copy contents of one file to another.
"""

# Opening source file in read mode
with open("sourceQ19.txt", "r") as source:
    data = source.read()

# Opening destination file in write mode
with open("destinationQ19.txt", "w") as dest:
    dest.write(data)

print("File copied successfully.")