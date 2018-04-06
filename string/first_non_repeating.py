""" Find the first non-repeating character """

from collections import Counter


def firstNonRepeating(s):

    charCount = Counter(s)

    for index, char in enumerate(s):
        if charCount[char] == 1:
            return index

    return -1
