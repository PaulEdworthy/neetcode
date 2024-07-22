# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
from collections import Counter


def is_anagram(s: str, t: str) -> bool:
    # # Submitted solution 59ms runtime
    # s = ''.join(sorted(s))
    # t = ''.join(sorted(t))
    # return s == t

    # # Optimized solution 35ms runtime
    return Counter(s) == Counter(t)


is_anagram("anagram", "nagaram")  # True
is_anagram("rat", "car")  # False
