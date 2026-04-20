"""
Q5. Write a program using nested if to classify a number (positive,
negative, zero).
"""

# Taking input from user
num = float(input("Enter a number: "))

# Nested if to classify number
if num >= 0:
    if num == 0:
        print("The number is Zero")
    else:
        print("The number is Positive")
else:
    print("The number is Negative")


# we can also use another method instead of this one

# if (num>0):
#     print("The number is Positive")
# elif(num<0):
#     print("The number is Negative")
# else:
#     print("The number is Zero")
