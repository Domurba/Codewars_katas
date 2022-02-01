#2021-09-08 09:14:35.973000+00:00
"""Write a function that checks if a given string (case insensitive) is a [palindrome](https://en.wikipedia.org/wiki/Palindrome)."""

def is_palindrome(s):
    return s.lower() == s.lower()[::-1]