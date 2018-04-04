""" PKM Algorithm to get index of substring

"""


def index(string, pattern):
    kmpArray = kmp(pattern)
    i, j = 0, 0
    while i < len(string):
        startIndex = i-j
        while i < len(string) and j < len(pattern) and string[i] == pattern[j]:
            i += 1
            j += 1
        if j == len(pattern):
            return startIndex
        j -= kmpArray[j]
        i += 1
    return -1


def kmp(pattern):
    lsp = [0] * len(pattern)
    i, j = 0, 1
    while j < len(pattern):
        if pattern[j] != pattern[i]:
            lsp[j] = 0
            j += 1
            i = 0
        else:
            lsp[j] = lsp[j-1] + 1
            j += 1
            i += 1
    return lsp


string = 'abcabcdab'
pattern = 'abcd'
result = index(string, pattern)
print(result)
print(string.index(pattern))

