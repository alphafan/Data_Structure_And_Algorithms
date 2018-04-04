""" Longest Zig-Zag Sequence
"""


def longestZigzagSequence(nums):
    start, end, maxLength = 0, 1, 0
    nextIsLarger = nums[1] > nums[0]
    while end < len(nums):
        if nextIsLarger:
            if nums[end] >= nums[end-1]:
                nextIsLarger = False
                end += 1
                maxLength = max(maxLength, end-start)
            else:
                start = end-1
                nextIsLarger = False
        if not nextIsLarger:
            if nums[end] <= nums[end-1]:
                nextIsLarger = True
                end += 1
                maxLength = max(maxLength, end-start)
            else:
                # nums[start] <= nums[end]
                start = end-1
                nextIsLarger = True
    return maxLength


arr = [1, 11, 2, 10, 4, 5, 2, 1]
print(arr)
print(longestZigzagSequence(arr))
