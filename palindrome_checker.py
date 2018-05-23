# palindrome_checker.py
"""
A simple program that checks whether user input is a palindrome or not. Can be adapted to return a bool value
instead of a printed response to the user.
"""

string = input("Enter a word to check if it is a palindrome: ")
palindrome = string[::-1]
if string == palindrome:
    print("That is a palindrome!")
else:
    print("That isn't a palindrome.")
