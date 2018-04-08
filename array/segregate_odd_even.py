""" Segregate Odd and Even Values """

import random


def segregate(nums):
    start, end = 0, len(nums) - 1
    for i in range(len(nums)):
        print(nums)
        while nums[i] % 2 == 1:
            swap(nums, i, start)
            print(nums)
            start += 1
            if start == end:
                return nums
        while nums[i] % 2 == 0:
            swap(nums, i, end)
            print(nums)
            end -= 1
            if start == end:
                return nums
    return nums


def swap(nums, i, j):
    nums[i], nums[j] = nums[j], nums[i]


test = [random.randint(0, 10) for i in range(10)]
print(segregate(test))

