""" Convert array into Zig-Zag fashion

Given an array of distinct elements, rearrange the elements of array in zig-zag
fashion in O(n) time. The converted array should be in form a < b > c < d > e < f.

Example:
Input:  arr[] = {4, 3, 7, 8, 6, 2, 1}
Output: arr[] = {3, 7, 4, 8, 2, 6, 1}

Input:  arr[] =  {1, 4, 3, 2}
Output: arr[] =  {1, 4, 2, 3}

"""

import random


def zigZagArray(nums):
    i = 0
    while i < len(nums)-2:
        # numbers to re-order nums[i:i+2]
        nums[i:i+3] = reorder(nums[i:i+3])
        i += 2
    if i == len(nums) or nums[-1] > nums[i]:
        return nums
    nums[i], nums[-1] = nums[-1], nums[i]
    return nums


def reorder(nums):
    if nums[0] >= nums[1] and nums[0] >= nums[2]:
        nums[0], nums[1] = nums[1], nums[0]
    elif nums[2] >= nums[0] and nums[2] >= nums[1]:
        nums[1], nums[2] = nums[2], nums[1]
    return nums


test = [random.randint(1, 10) for _ in range(10)]
print(test)
print(zigZagArray(test))
