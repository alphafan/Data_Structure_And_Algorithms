""" Ugly Number

Ugly numbers are numbers whose only prime factors are 2, 3 or 5.
The sequence 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, … shows the first 11 ugly numbers.
By convention, 1 is included.

Given a number n, the task is to find n’th Ugly number.

Input  : n = 7
Output : 8

Input  : n = 10
Output : 12

Input  : n = 15
Output : 24

Input  : n = 150
Output : 5832
"""

import time


def uglyNumber(n):
    i, count = 1, 0
    while True:
        if isUglyNumber(i):
            count += 1
            if count == n:
                return i
        i += 1


def isUglyNumber(n):
    # bottom-up solution ?
    # uglyNumber = pre ugly number * 2 + pre ugly number * 3 + pre ugly number * 5
    # 1
    # 2, 3, 5
    # 4, 6, 10
    # 9, 15
    # 25
    if n == 1:
        return True
    if n % 5 == 0:
        return isUglyNumber(n/5)
    elif n % 3 == 0:
        return isUglyNumber(n/3)
    elif n % 2 == 0:
        return isUglyNumber(n/2)
    else:
        return False


start = time.time()
print(uglyNumber(500))
end = time.time()
print(end-start)
