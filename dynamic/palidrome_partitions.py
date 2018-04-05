""" Min Cut Palidromes """

from functools import lru_cache


@lru_cache(maxsize=1024)
def minPartitions(s, left, right):
    # Base case:
    #   1) s contains only one character
    #   2) s[left:right+1] is palidrome
    if right - left <= 0 or isPalidrome(s[left:right+1]):
        return 0
    # Else:
    #   1) cut after first char
    #   2) cut before last char
    return 1 + min(minPartitions(s, left+1, right),
                   minPartitions(s, left, right-1))


@lru_cache(maxsize=1024)
def isPalidrome(s):
    return s == s[::-1]


s = 'abcbcd'
print(s)
print(minPartitions(s, 0, len(s)-1))
