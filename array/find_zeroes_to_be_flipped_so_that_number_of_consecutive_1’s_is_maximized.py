""" Find zeroes to be flipped so that number of consecutive 1’s is maximized

https://www.geeksforgeeks.org/find-zeroes-to-be-flipped-so-that-number-of-consecutive-1s-is-maximized/
"""

import random


def numFlipped(nums):
    # 1, Find maximum continuous 0s
    # 2, Bit manipulation?
    l, r, maxFlipped = 0, 0, 0
    for i, num in enumerate(nums):
        if (nums[i] == 0 and i == 0) or (nums[i-1] == 1 and nums[i] == 0):
            l = i
        if (nums[i] == 0 and i == len(nums)-1) or nums[i] == 0 and nums[i+1] == 1:
            r = i + 1
            maxFlipped = max(maxFlipped, r-l)
    return maxFlipped


if __name__ == '__main__':
    n = [random.randint(0, 1) for _ in range(10)]
    print(n)
    print(numFlipped(n))
