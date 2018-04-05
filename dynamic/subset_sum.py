""" Subset sum """

import random


def subsetSum(nums, target):
    # Create and init cache
    cache = [[False for _ in range(target + 1)] for _ in range(len(nums))]
    for i in range(len(nums)):
        for j in range(target + 1):
            if j == 0:
                cache[i][j] = True
    cache[0][nums[0]] = True

    for i in range(1, len(nums)):
        for j in range(target + 1):
            if cache[i - 1][j] and j + nums[i] <= target:
                cache[i][j] = True
                cache[i][j + nums[i]] = True

    return cache[-1][target]


test = [random.randint(0, 10) for _ in range(5)]
print(test)
print(subsetSum(test, 17))
