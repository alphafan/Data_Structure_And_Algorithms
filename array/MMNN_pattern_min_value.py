""" Increase M and Decrese N

2. Given a sequence of M and N with M representing increasing and N representing decreasing,
output the smallest number that follows this pattern.

Input : MMMM
Output : 12345

Input : NNNN
Output : 54321

Input : MMNM
Output : 2314

"""


def minNumber(pattern):
    # rightest N should be 1
    # M M N N M
    # 3 4 2 1 5
    pattern = list(pattern)
    number = ['*'] * len(pattern)
    count = 0
    for i, char in enumerate(pattern[::-1]):
        if char == 'N':
            count += 1
            number[-1-i] = str(count)
    for i, char in enumerate(pattern):
        if char == 'M':
            count += 1
            number[i] = str(count)
    return int(''.join(number))


print(minNumber('MMNNMM'))


