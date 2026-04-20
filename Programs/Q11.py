"""
Q11. Write a program to count frequency of characters in a string.
"""

# # Taking input from user
# text = input("Enter a string: ")

# # Dictionary to store frequency
# freq = {}

# # Counting frequency
# for char in text:
#     if char in freq:
#         freq[char] += 1
#     else:
#         freq[char] = 1

# # Display result
# print("\nCharacter Frequency:")
# for key, value in freq.items():
#     print(key, ":", value)

# Another Method:-
#----------------------------------4

from collections import Counter

text = input("Enter a string: ")
freq = Counter(text)

print(freq)
