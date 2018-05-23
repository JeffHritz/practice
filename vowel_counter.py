# vowel_counter.py - Jeff Hritz
"""
A simple module that counts the number of vowels in a user entered string.
"""

vowels = ['a', 'e', 'i', 'o', 'u']

string = input("Enter a string: ")

number = 0

for i in string:
    for v in vowels:
        if i.count(v) == 1:
            number += 1
        else:
            continue

print(number)






