# To lowercase, remove all non-alphanumeric chars
import re


def is_palindrome(s: str):  # return True
    s = re.sub(r'[^a-zA-Z0-9]+', '', s).lower()
    return s == s[::-1]


s = "A man, a plan, a canal: Panama"  # True
t = "race a car"  # False
u = " "  # True
is_palindrome("ab_a")
