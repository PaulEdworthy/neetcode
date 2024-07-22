# Given a string s consisting of words and spaces,
# return the length (an int) of the last word in the string.

def length_of_last_word(s: str):
    return len(s.strip().split()[-1])
# This is a 99th percentile solution for runtime!


s = 'Hello World'  # 5
t = "   fly me   to   the moon  "  # 4
length_of_last_word(s)
length_of_last_word(t)
