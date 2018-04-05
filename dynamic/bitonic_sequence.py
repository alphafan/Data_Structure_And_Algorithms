""" Longest Increasing Sequence """


def maxBitonicSeq(nums):
    increase = [1] * len(nums)
    for i in range(1, len(nums)):
        if nums[i] >= nums[i - 1]:
            increase[i] = increase[i - 1] + 1

    decrease = [1] * len(nums)
    for i in range(len(nums) - 2, -1, -1):
        if nums[i] >= nums[i + 1]:
            decrease[i] = decrease[i + 1] + 1

    bitonic = [i + d - 1 for i, d in zip(increase, decrease)]
    maxLength = max(bitonic)

    return maxLength


nums = [1, 2, 3, 4, 3, 2, 1]
result = maxBitonicSeq(nums)
print(result)
