""" Maximum increasing sum sub-sequence """

import sys
import unittest


def maxSumIncreaseSeq(nums):
    if len(nums) == 0:
        return []
    start, end = 0, 0
    maxStart, maxEnd, maxSum = 0, 0, -sys.maxsize
    for i in range(len(nums)):
        if i == 0 or nums[i - 1] > nums[i]:
            start = i
        if i > 0 and nums[i - 1] <= nums[i]:
            end = i
            currentSum = sum(nums[start:end + 1])
            if currentSum > maxSum:
                maxSum = currentSum
                maxStart, maxEnd = start, end
    return nums[maxStart:maxEnd + 1]


class TestMaxSumOfIncreaseSequence(unittest.TestCase):

    def test_max_sub_sequence_1(self):
        nums = [1, 3, 7, 2, 8, 9]
        result = maxSumIncreaseSeq(nums)
        assert result == [2, 8, 9]

    def test_max_sub_sequence_2(self):
        nums = [9, 8, 7, 6, 5, 4]
        result = maxSumIncreaseSeq(nums)
        assert result == [9]

    def test_max_sub_sequence_3(self):
        nums = [4, 4, 4, 6, 3, 5]
        result = maxSumIncreaseSeq(nums)
        assert result == [4, 4, 4, 6]

    def test_max_sub_sequence_4(self):
        nums = [1, 4, 4, 3]
        result = maxSumIncreaseSeq(nums)
        assert result == [1, 4, 4]

    def test_max_sub_sequence_5(self):
        nums = [1]
        result = maxSumIncreaseSeq(nums)
        assert result == [1]

    def test_max_sub_sequence_6(self):
        nums = [1, 1]
        result = maxSumIncreaseSeq(nums)
        assert result == [1, 1]

    def test_max_sub_sequence_7(self):
        nums = []
        result = maxSumIncreaseSeq(nums)
        assert result == []


if __name__ == '__main__':
    unittest.main()
