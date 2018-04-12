""" Segment Tree """


class SegmentTree(object):

    def __init__(self, nums):
        self.nums = nums
        self.tree = [None] * (pow(2, len(nums)) - 1)

    def _buildTree(self, start, end, index):
        if start == end:
            self.tree[index] = self.nums[start]
            return self.tree[index]

        middle = int((start+end)/2)
        self.tree[index] = self._buildTree(start, middle, 2*index+1) + \
            self._buildTree(middle+1, end, 2*index+2)

        return self.tree[index]


