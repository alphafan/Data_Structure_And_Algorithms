"""
Given n and an array of strings, print the string that contains the digits (1, 2, 3), if there are multiple strings that satisfies the conditions, print them in ascending order.
"""


def containsDigits(strings):
    result = []
    for string in strings:
        if '1' in string and '2' in string and '3' in string:
            result.append(string)
    result.sort()
    return result


test = ['123456', '1395', '1721298', '102030', '3215', '123']
print(containsDigits(test))

