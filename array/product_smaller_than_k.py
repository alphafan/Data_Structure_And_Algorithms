""" Number of subarray with product smaller than k.  """


def numSubAarrys(nums, target):
    helper(nums, target, 0, [])


def helper(nums, target, index, partial):
    currentProduct = product(partial)
    if currentProduct < target:
        print(partial)
        for i in range(index, len(nums)):
            helper(nums, target, i + 1, partial + [nums[i]])


def product(nums):
    if len(nums) == 0:
        return 0
    result = 1
    for num in nums:
        result = result * num
    return result


test = [1, 2, 3, 4]
numSubAarrys(test, 19)