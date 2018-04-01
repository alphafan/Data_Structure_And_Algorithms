import random


def maxContinuousProduct(nums):
    maxEndingHere = minEndingHere = maximum = nums[0]
    for num in nums[1:]:
        maxEndingHere = max(maxEndingHere*num, minEndingHere*num, num)
        minEndingHere = min(minEndingHere*num, maxEndingHere*num, num)
        maximum = max(maximum, maxEndingHere)
    return maximum


n = [random.randint(-10, 20) for _ in range(10)]
print(n)
print('Max:', maxContinuousProduct(n))
