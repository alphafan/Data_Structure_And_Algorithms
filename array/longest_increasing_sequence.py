""" Longest Increasing Sequence in Array """

import random


def longestIncreasingSequence(nums):
    start, end, maxLength = 0, 0, 0
    for i in range(len(nums)):
        if i > 0 and nums[i] >= nums[i-1]:
            end = i
            maxLength = max(maxLength, end-start+1)
        else:
            start = i
    return maxLength


test = [random.randint(1, 10) for _ in range(10)]
print(test)
print(longestIncreasingSequence(test))
