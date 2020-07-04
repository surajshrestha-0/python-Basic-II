"""
Create a function, is_palindrome, to determine if a supplied word is the same if the letters are reversed.
"""


def is_palindrome(word):
    word = word.lower()
    if word == word[::-1]:
        print("The string is a palindrome")
    else:
        print("The string is not a palindrome")


is_palindrome('Madam')
is_palindrome('one')
