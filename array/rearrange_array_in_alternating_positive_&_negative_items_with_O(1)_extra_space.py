""" Rearrange array in alternating positive & negative items with O(1) extra space

Given an array of positive and negative numbers, arrange them in an alternate fashion such that every positive number is
followed by negative and vice-versa maintaining the order of appearance.
Number of positive and negative numbers need not be equal. If there are more positive numbers they appear at the end of
the array. If there are more negative numbers, they too appear in the end of the array.

Example:

Input:  arr[] = {1, 2, 3, -4, -1, 4}
Output: arr[] = {-4, 1, -1, 2, 3, 4}

Input:  arr[] = {-5, -2, 5, 2, 4, 7, 1, 8, 0, -8}
output: arr[] = {-5, 5, -2, 2, -8, 4, 7, 1, 8, 0}
This question has been asked at many places (See this and this)

The above problem can be easily solved if O(n) extra space is allowed. It becomes interesting due to the limitations
that O(1) extra space and order of appearances.
The idea is to process array from left to right. While processing, find the first out of place element in the remaining
unprocessed array. An element is out of place if it is negative and at odd index, or it is positive and at even index.
Once we find an out of place element, we find the first element after it with opposite sign. We right rotate the
subarray between these two elements (including these two).

"""

import random


def rearrangeArray(nums):
    swapIndex, currentIndex = 0, 0
    nextIsNegative = True
    while currentIndex < len(nums):
        if nextIsNegative:
            while currentIndex < len(nums) and nums[currentIndex] >= 0:
                currentIndex += 1
            if currentIndex != len(nums):
                swap(nums, currentIndex, swapIndex)
                swapIndex += 1
                nextIsNegative = False
                currentIndex = swapIndex
        else:
            while currentIndex < len(nums) and nums[currentIndex] <= 0:
                currentIndex += 1
            if currentIndex != len(nums):
                swap(nums, currentIndex, swapIndex)
                swapIndex += 1
                nextIsNegative = True
                currentIndex = swapIndex
        print(nums)
    # Right shift 0s
    for i, num in enumerate(nums):
        if num == 0:
            nums = nums[:i] + nums[i+1:] + [num]
    print(nums)


def swap(nums, i, j):
    nums[i], nums[j] = nums[j], nums[i]


test = [random.randint(-10, 10) for _ in range(10)]
rearrangeArray(test)
