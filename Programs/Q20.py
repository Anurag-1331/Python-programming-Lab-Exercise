"""
Q20. Write a program to demonstrate file pointer operations using
seek().
"""

# Open file in read mode
with open("sampleQ20.txt", "r") as file:
    
    # Read first 5 characters
    data1 = file.read(5)
    print("First 5 characters:", data1)

    # Move pointer to beginning
    file.seek(0)
    data2 = file.read(5)
    print("After seek(0), first 5 characters again:", data2)

    # Move pointer to 10th position
    file.seek(10)
    data3 = file.read(5)
    print("After seek(10), next 5 characters:", data3)