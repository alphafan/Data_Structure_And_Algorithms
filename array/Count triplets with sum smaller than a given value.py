""" Count triplets with sum smaller than a given value

https://www.geeksforgeeks.org/count-triplets-with-sum-smaller-that-a-given-value/

Given an array of distinct integers and a sum value.
Find count of triplets with sum smaller than given sum value.
Expected Time Complexity is O(n2).

Examples:

Input : arr[] = {-2, 0, 1, 3}
        sum = 2.
Output : 2
Explanation :  Below are triplets with sum less than 2
               (-2, 0, 1) and (-2, 0, 3)

Input : arr[] = {5, 1, 3, 4, 7}
        sum = 12.
Output : 4
Explanation :  Below are triplets with sum less than 4
               (1, 3, 4), (1, 3, 5), (1, 3, 7) and
               (1, 4, 5)
"""

import random


def numTriplets(nums, platform):
    if len(nums) < 3:
        return 0
    count = 0
    nums = sorted(nums)
    for idx1 in range(0, len(nums)-2):
        idx2 = idx1 + 1
        idx3 = len(nums) - 1
        while idx2 < idx3:
            currentSum = sum([nums[idx1], nums[idx2], nums[idx3]])
            if currentSum < platform:
                count += 1
                print([nums[idx1], nums[idx2], nums[idx3]])
                idx2 += 1
            else:
                idx3 -= 1
    return count


test = [random.randint(-5, 10) for _ in range(10)]
print(test)
numTriplets(test, 10)
