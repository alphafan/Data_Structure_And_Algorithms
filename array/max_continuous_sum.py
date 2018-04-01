import sys
import random


def maxContinuousSum(nums):
    maxSoFar = -sys.maxsize
    maxEndingHere = 0
    for num in nums:
        maxEndingHere += num
        if maxSoFar < maxEndingHere:
            maxSoFar = maxEndingHere
        if maxEndingHere < 0:
            maxEndingHere = 0
    return maxSoFar


n = [random.randint(-10, 20) for _ in range(10)]
print(n)
print('Max:', maxContinuousSum(n))
