"""
Partition problem is to determine whether a given set can be partitioned into two subsets such that the sum of elements in both subsets is same.

Examples

arr[] = {1, 5, 11, 5}
Output: true
The array can be partitioned as {1, 5, 5} and {11}

arr[] = {1, 5, 3}
Output: false
The array cannot be partitioned into equal sum sets.
"""


def canPartition(nums):
    # sum of partial can be sum(nums)/2
    sumNums = sum(nums)
    if sumNums % 2 == 1 or len(nums) < 2:
        return False
    return subsetSum(nums, sumNums/2, 0, [])


def subsetSum(nums, target, startIndex, partial):
    currentSum = sum(partial)
    if currentSum == target:
        return True
    for i in range(startIndex, len(nums)):
        if subsetSum(nums, target, i+1, partial + [nums[i]]):
            return True
    return False


nums = [1, 5, 3, 5]
print(canPartition(nums))
