""" Find smallest element in a rotated array """

import random


def smallestElement(nums):
    if len(nums) == 0:
        return
    if len(nums) == 1:
        return nums[0]
    start, end = 0, len(nums)
    while start <= end:
        mid = int((start+end)/2)
        if mid > start and nums[mid] < nums[mid-1]:
            return nums[mid]
        if mid < end and nums[mid+1] < nums[mid]:
            return nums[mid+1]
        if nums[mid] > nums[start]:
            start = mid + 1
        else:
            end = mid - 1


index = random.randint(0, 9)
test = [i for i in range(10)]
test = test[index:] + test[:index]
print(test)
print(smallestElement(test))

